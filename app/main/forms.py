from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
from ..models import User



class AddPostForm(FlaskForm):
    title=TextAreaField('Author', validators=[Required()])
    content = TextAreaField('Post', validators = [Required()])  
    
    submit = SubmitField('SUBMIT')  
class CommentForm(FlaskForm):
    comment = TextAreaField('Post comment' , validators=[Required()])
    submit = SubmitField('submit')