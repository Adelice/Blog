from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
from ..models import User



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