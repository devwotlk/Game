from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User  # Import the User model from models.py

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to something secure
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://your_username:your_password@localhost/rpg_auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and login manager
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Index route
@app.route('/')
def index():
    if current_user.is_authenticated:
        return f'Hello, {current_user.acc_name}! <br> <a href="/logout">Logout</a>'
    return '<a href="/login">Login</a> <br> <a href="/register">Register</a>'

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        acc_name = request.form['name']
        acc_email = request.form['email']
        acc_password = request.form['password']

        # Check if user already exists
        existing_user = User.query.filter_by(acc_email=acc_email).first()
        if existing_user:
            flash('Email address already exists')
            return redirect(url_for('register'))

        # Create new user
        hashed_password = generate_password_hash(acc_password, method='sha256')
        new_user = User(acc_name=acc_name, acc_email=acc_email, acc_password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! You can now log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        acc_email = request.form['email']
        acc_password = request.form['password']

        user = User.query.filter_by(acc_email=acc_email).first()

        if user and check_password_hash(user.acc_password_hash, acc_password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your email and password.')

    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Dashboard route (only for logged-in users)
@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome to your dashboard, {current_user.acc_name}! <a href="/logout">Logout</a>'

if __name__ == '__main__':
    app.run(debug=True)
