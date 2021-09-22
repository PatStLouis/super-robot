from flask import current_app as app
from flask import render_template, redirect, url_for, request, flash, session
from app.main import bp
from .forms import LoginForm
from pprint import pprint


@bp.route("/", methods=["GET"])
def index():
    return redirect(url_for("main.login"))


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        code = form.code.data
        users = app.config['USERS']
        password = app.config['GUAC_PASSWORD']
        for user in users:
            if code == user:
                username = users[user]
        try:
            session["url"] = f"https://guac.hackmoi.ca/#/yourConnection?username={username}&password={password}"
            return redirect(url_for("main.interface"))
        except:
            return redirect(url_for("main.login"))
    return render_template("pages/login.jinja", form=form)


@bp.route("/interface", methods=["GET"])
def interface():
    try:
        return render_template("pages/interface.jinja", url=session["url"])
    except:
        return redirect(url_for("main.login"))