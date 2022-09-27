from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import DataRequired
from wtforms import TextField, PasswordField


app = Flask(__name__)
app.secret_key = "this is a secret key"


class LoginForm(FlaskForm):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)