from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import sqlite3

from db import init_db, DB_NAME

app = Flask(__name__)
app.secret_key = "SECRET"  # in productie: env var

init_db()


def db_conn():
    return sqlite3.connect(DB_NAME)


@app.route("/")
def index():
    # Als ingelogd: toon home
    if session.get("user"):
        return redirect(url_for("home"))
    return redirect(url_for("login"))


@app.route("/home")
def home():
    username = session.get("user")
    if not username:
        return redirect(url_for("login"))

    firstname = ""
    lastname = ""
    with db_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT firstname, lastname FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        if row:
            firstname = row[0] or ""
            lastname = row[1] or ""

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    user_ip = request.remote_addr

    return render_template("home.html", username=username, firstname=firstname, lastname=lastname, now=now, user_ip=user_ip)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", error=None)

    username = (request.form.get("username") or "").strip()
    firstname = (request.form.get("firstname") or "").strip()
    lastname = (request.form.get("lastname") or "").strip()
    password = request.form.get("password") or ""

    # Geen validatie - gewoon opslaan
    created_at = datetime.utcnow().isoformat(timespec="seconds")

    try:
        with db_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password, firstname, lastname, created_at) VALUES (?, ?, ?, ?, ?)",
                (username, password, firstname, lastname, created_at),
            )
            conn.commit()
    except sqlite3.IntegrityError:
        return render_template("register.html", error="Deze username bestaat al.")

    # Na registratie: naar login
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", error=None)

    username = (request.form.get("username") or "").strip()
    password = request.form.get("password") or ""

    with db_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username = ?", (username,))
        row = cur.fetchone()

    if not row:
        return render_template("login.html", error="Gebruiker niet gevonden.")

    stored_password = row[0]
    if stored_password != password:
        return render_template("login.html", error="Fout wachtwoord.")

    session["user"] = username
    return redirect(url_for("home"))


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
