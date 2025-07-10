from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=3,max=15)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password',message='Password must match')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')