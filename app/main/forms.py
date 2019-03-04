from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
from ..models import User,Subscription



class AddPostForm(FlaskForm):
    author=TextAreaField('Author', validators=[Required()])
    content = TextAreaField('Post', validators = [Required()])  
    submit = SubmitField('SUBMIT')  
class CommentForm(FlaskForm):
    content = TextAreaField('Comment' , validators=[Required()])
    # username=TextAreaField('Username', validators=[Required()])
    submit = SubmitField('SUBMIT')
class SubscriptionForm(FlaskForm):
    email = TextAreaField('Add Your Email' ,validators=[Required()]) 
    submit= SubmitField('SUBMIT') 
    def validate_email(self,data_field):
            if Subscription.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')  


class UpdateForm(FlaskForm):
    author=TextAreaField('Add a New Author' ,validators=[Required()]) 
    content=TextAreaField('Add New Post' , validators=[Required()]) 
    submit= SubmitField('SUBMIT')              