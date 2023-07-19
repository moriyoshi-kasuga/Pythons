import os
from datetime import datetime

import pytz
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from flask import Flask, redirect, render_template, request

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SECRET_KEY"] = os.urandom(24)
db.init_app(app)

login_manager = LoginManager()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.now(pytz.timezone("Asia/Tokyo"))
    )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(12), nullable=False)


login_manager.init_app(app)
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        if current_user.is_authenticated:
            posts = Post.query.all()
            return render_template("index.html", posts=posts)
        else:
            return render_template("not_login_index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        assert password is not None
        user = User(
            username=username,
            password=generate_password_hash(password, method="sha256"),
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    else:
        return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        assert password is not None
        user = User.query.filter_by(username=username).first()
        # FIX: ここでユーザー名がない場合に対処しよう
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect("/")
        else:
            return redirect("/login")
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route("/delete/<int:id>")
@login_required
def delete(id: int):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id: int):
    post = Post.query.get(id)
    if request.method == "GET":
        return render_template("update.html", post=post)
    else:
        post.title = request.form.get("title")
        post.body = request.form.get("body")
        db.session.commit()
        return redirect("/")


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("create.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
