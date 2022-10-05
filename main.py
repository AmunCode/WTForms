from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import DataRequired
from wtforms import TextField, PasswordField, SubmitField, validators, ValidationError

app = Flask(__name__)
app.secret_key = "this is a secret key"


def valid_email(form, field):
    if '@' not in field and '.' not in str(field):
        raise ValidationError('Invalid email address!')


class LoginForm(FlaskForm):
    username = TextField(label='Username', validators=[DataRequired(),
                                                       validators.Length(min=8, message='username is too short'),
                                                       validators.Email(message='not valid email format')])
    password = PasswordField(label='Password', validators=[DataRequired(),
                                                           validators.Length(min=8,
                                                                             message='Password must be at least  8 characters long.')])
    submit = SubmitField(label='log In')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)