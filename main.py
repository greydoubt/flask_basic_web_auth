from flask import Flask, render_template, request, redirect, url_for
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')

# User database - this is just an example, in practice, you would use a real database
users = {
    'admin': {
        'salt': 'abc123',
        'hash': '1a79a4d60de6718e8e5b326e338ae533',
    },
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            salt = users[username]['salt']
            hash_ = users[username]['hash']
            password_hash = hashlib.md5((password + salt).encode()).hexdigest()
            
            if password_hash == hash_:
                return redirect(url_for('success'))
        
        return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
