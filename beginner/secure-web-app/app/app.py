from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = "SecretKey"

# Register Form
class RegisterForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

# HTML Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    name = None
    password = None
    form = RegisterForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        form.name.data = ''
        return render_template("home.html")
    return render_template("register.html",
                           name = name,
                           password = password,
                           form = form)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Debug Mode
if __name__ == "__main__":
    app.run(debug=True)