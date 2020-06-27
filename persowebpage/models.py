# # models.py
# from puppycompanyblog import db, login_manager # from __init__.py
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
# from datetime import datetime
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)
#
# class User(db.Model, UserMixin):
#
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     profile_image = db.Column(db.String(64), nullable = False, default='default_profile.png')
#     email = db.Column(db.String(64), unique=True, index=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     password_hash = db.Column(db.String(128))
#
#     posts = db.relationship('BlogPost', backref='author', lazy=True) #author a a blog post is a user
#
#     def __init__(self, email, username, password):
#         self.email = email
#         self.username = username
#         self.password_hash = generate_password_hash(password)
# 
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#     def __repr__(self):
#         return f'Username: {self.username}'
#
#
# class BlogPost(db.Model):
#     # users = db.relationship(User)
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False) # come to table names users and id attribute
#     date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
#     title = db.Column(db.String(140), nullable=False)
#     test = db.Column(db.Text, nullable=False)
#
#     def __init__(self, title, text, user_id):
#         self.title = title
#         self.text = text
#         self.user_id = user_id
#
#     def __repr__(self):
#         return f'post ID: {self.id} -- Date: {self.date}'
