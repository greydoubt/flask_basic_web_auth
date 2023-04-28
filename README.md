# flask_basic_web_auth
generic site to restrict access to a password

Uses the hashlib module to hash the password with an MD5 hash function, which is not recommended for secure password storage. In practice, you would want to use a stronger hash function like SHA-256 or bcrypt.

Also use a random salt for each user's password. The salt is stored in the user database along with the hashed password. When the user logs in, we retrieve the salt for their account, combine it with the entered password, hash it, and compare the resulting hash with the stored hash.

Note that this is still just an example and not a production-ready implementation of a login system. It's important to use secure password storage techniques and follow best practices when implementing a real login system.


#### 
Uses the official Python 3.9 slim-buster image as the parent image. We set the working directory to /app, copy the requirements.txt file into the container, and install the required packages using pip. We then copy the rest of the application code into the container.

We set the FLASK_APP environment variable to app.py so that Flask knows which module to run as the application. We expose port 5000, which is the default port that Flask uses for serving web traffic. Finally, we use the CMD instruction to run the flask run command with the --host=0.0.0.0 option, which allows the Flask app to be accessed from outside the container.

To build the Docker image, navigate to the directory that contains the Dockerfile and run the following command:

*docker build -t my-flask-app .*

This will build the Docker image with the tag my-flask-app. You can replace my-flask-app with any other name that you want to use for the image.

To run the Docker container, use the following command:

*docker run -p 5000:5000 my-flask-app*

This will start the container and map port 5000 on the host to port 5000 in the container, so that you can access the Flask app by navigating to http://localhost:5000 in your web browser.

Note that this is just a basic example and you may need to modify the Dockerfile to suit your specific needs, such as adding additional dependencies or configuring the Flask app with environment variables.
