from flask_login import current_user
from flask_wtf import FlaskForm
from post_it_note.models import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class RegistrationForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                    validators=[DataRequired(), Length(min=6, max=64)])
    confirm_password = PasswordField('Confirm password', 
                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That E-mail is already registered')


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                    validators=[DataRequired(), Length(min=6, max=64)])
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That E-mail is already registered')


class RequestResetForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that E-mail')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', 
                    validators=[DataRequired(), Length(min=6, max=64)])
    confirm_password = PasswordField('Confirm password', 
                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset password')