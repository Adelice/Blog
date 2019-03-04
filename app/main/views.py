from flask import render_template,request,redirect,url_for,abort
from ..models import  User,Post,Comment,Quote,Subscription
from ..request import get_quote
from . import main
from .forms import AddPostForm,CommentForm,SubscriptionForm,UpdateForm
from ..import db,photos
from flask_login import login_required,current_user
from ..email import mail_message
# Views

@main.route('/' , methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    form=SubscriptionForm()
    if form.validate_on_submit():
        email=form.email.data
        new_subscriber=Subscription(email=email)
        db.session.add(new_subscriber)
        db.session.commit()
        mail_message("Thank you for subscribing!! We can't wait to send you quotes","email/welcome_user",new_subscriber.email,new_subscriber=new_subscriber)
        return redirect(url_for('main.index'))

   
    title = 'Home - Welcome to MyBlogpost'
    search_posts=Post.get_posts()
    quote=get_quote()


    return render_template('index.html', title = title,posts=search_posts,quote=quote,form=form)


@main.route('/post/new/', methods = ['GET','POST'])
@login_required
def add_post():
    form = AddPostForm()
   
    if form.validate_on_submit():
      
       content = form.content.data
       author = form.author.data

       new_post=Post(content=content, author=author)
       new_post.save_post()
       subscribers=Subscription.query.all()
       for subscriber in subscribers:
          mail_message("New Quote","email/notify",subscriber.email,subscriber=subscriber,new_post=new_post)

       return redirect(url_for('main.index'))
    search_posts = Post.query.all()
    title = 'Please add your post'
    return render_template('posts.html' , title = title,post_form=form )
@main.route('/post/<int:id>')
def single_post(id):
    post=Post.query.filter_by(id=id).first()
    comments=Comment.get_comments(id=id)
    return render_template('post.html',post=post,comments=comments) 
@main.route('/new/comment/<int:id>' , methods = ['GET', 'POST'])    
def add_comment(id):
    post=Post.query.filter_by(id=id).first()
    user=User.query.filter_by(id=id).first()
    if post is None:
        abort(404)
    form=CommentForm()
    if form.validate_on_submit():
        content=form.content.data 
       
        new_comment=Comment(content=content,post=post,user=user )
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('comments.html',comment_form=form) 
@main.route('/delete/comment/<int:id>' , methods = ['GET', 'POST']) 
def delete_comment(id):
    comment=Comment.query.filter_by(id=id).first()   
    if comment is not None:
        comment.delete_comment()

        return redirect(url_for('main.index'))
   
@main.route('/delete/post/<int:id>' ,methods= ['GET', 'POST'])
@login_required
def delete_post(id):
    post=Post.query.filter_by(id=id).first()
    if post is not None:
        post.delete_post(id)
        return redirect(url_for('main.index'))
@main.route('/update/post/<int:id>' , methods= ['GET','POST'])
@login_required
def update_post(id):
    post=Post.query.filter_by(id=id).first()
    if post is None:
        abort(404)
    form=UpdateForm() 
    if form.validate_on_submit():
        post.author=form.author.data
        post.content=form.content.data

        db.session.add(post)
        db.session.commit()  
        return redirect(url_for('main.index'))
    return render_template('update.html',update_form=form)     