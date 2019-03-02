from flask import render_template,request,redirect,url_for,abort
from ..models import  User,Post
from . import main
from .forms import AddPostForm,CommentForm
from ..import db,photos
from flask_login import login_required,current_user
# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

   
    title = 'Home - Welcome to Blogpost'
    search_posts=Post.get_posts()


    return render_template('index.html', title = title,posts=search_posts)


@main.route('/post/new/', methods = ['GET','POST'])
@login_required
def add_post():
    form = AddPostForm()
   
    if form.validate_on_submit():
      
       content = form.content.data

       new_post=Post(content=content, user=current_user)
       new_post.save_post()

       return redirect(url_for('main.index'))
    search_posts = Post.query.all()
    title = 'Please add your post'
    return render_template('posts.html' , title = title,post_form=form )