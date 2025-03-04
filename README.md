# Django Project Account Starter Files
A template for starting new django projects with a custom user account system already built for you!
## About
This project sets up the account system implemented in William S. Vincent's book Django For Beginners. The goal of this template is to quickstart the development process and start with writing django code instead of adding an account system.
The account system includes password change, password reset, and adds an age field on top of the default username, email, and password fields.

## Setup
1. After cloning this repository startup a python virtual environment and install requirements.txt with `python -m pip install -r requirements.txt`.
2. Create a db.sqlite3 file in the project directory and a .env file where you should generate a secret key (which can be done with `python -c "import secrets; print(secrets.token_urlsafe())"`) and add it to the .env file as `SECRET_KEY=your_generated_key`
3. Next, go into the templates directory and change the default 'base.html' and 'home.html' templates to match your project (Or just change the title and nav header fields to appropriate names).
4. Continue

### Attribution
Basically all of the code comes from William S. Vincent's book Django 4.0 for Beginners. The source code from the book can be found at [this repo](https://github.com/wsvincent/djangoforbeginners_40)
