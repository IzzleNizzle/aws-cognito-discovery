import os
from flask import Flask, session, redirect, send_file
from datetime import timedelta

from app.izauth.cognito import authenticate_with_cognito, logout

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SESSION_SECRET")
app.permanent_session_lifetime = timedelta(minutes=1)
app.config["SESSION_PERMANENT"] = False


@app.route("/")
@authenticate_with_cognito
def index():
    print(f'index: Logged in as {session["uuid"]}')
    return send_file("./index.html", mimetype="text/html")


@app.route("/sign-in-redirect")
@authenticate_with_cognito
def sign_in_redirect():
    print(f'sign_in_redirect: Logged in as {session["uuid"]}')
    return redirect("/")


@app.route("/logout")
def user_logout():
    logout()
    return "OK"
