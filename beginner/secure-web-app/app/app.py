from flask import Flask, render_template, redirect, url_for, session
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = "SecretKey"
bcrypt = Bcrypt(app)

# Check username exists
def check_user(name, password):
    with open("app/static/database.db", "r") as file:
            for line in file:
                users = (line.strip())
                if users.replace("U:", "") == name:
                    return False
    with open("app/static/database.db", "a") as file:
        file.write(f"U:{name}\n")

        pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")
        file.write(f"P:{pw_hash}\n")
        return True
    
# Check password exists
def check_pass(name, password):
    with open("app/static/database.db", "r") as file:
            for line in file:
                users = (line.strip())
                if users.replace("U:", "") == name:
                    current_line = file.readline()
                    pw_hash = current_line.strip().replace("P:", "")
                    return bcrypt.check_password_hash(pw_hash, password)

# Register Form
class RegisterForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Login Form
class LoginForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.after_request
def add_security_headers(resp):
    resp.headers["Content-Security-Policy"]="default-src \'self\'"
    resp.headers["X-Frame-Options"]="DENY"
    resp.headers["X-Content-Type-Options"]="nosniff"
    resp.headers["Referrer-Policy"]="no-referrer"
    return resp

# HTML Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if "user" in session:
        return redirect(url_for("dashboard"))
    name = None
    password = None
    form = RegisterForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        if check_user(name, password):
            return redirect(url_for("login"))
        else:
            form.name.data = ''
            error = "Username already exists."
            return render_template("register.html", name = name, password = password, form = form, error = error)
    return render_template("register.html", name = name, password = password, form = form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("dashboard"))
    name = None
    password = None
    form = LoginForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        if check_pass(name, password):
            session["user"] = name
            print(session)
            return redirect(url_for("dashboard"))
        else:
            form.name.data = ''
            error = "Password is incorrect."
            return render_template("login.html", name = name, password = password, form = form, error = error)
    return render_template("login.html", name = name, password = password, form = form)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

# Debug Mode
if __name__ == "__main__":
    app.run(debug=True)