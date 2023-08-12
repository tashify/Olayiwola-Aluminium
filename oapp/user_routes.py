
from flask import Flask,render_template,request,redirect,flash,session

from sqlalchemy.sql import text

from oapp import app,csrf
from oapp.models import db,Contact

@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html',pagename='Olayiwola Aluminum - Your Trusted Aluminum Solutions Provider')

@app.route('/service/')
def service():
    return render_template('services.html',pagename='Olayiwola Aluminum Service')


#start
@app.route('/project/shower_cubicle')
def project_shower_cubicle():
    return render_template('projects.html',pagename='Olayiwola Aluminum Project-Shower Cubicle')

@app.route('/project/door')
def project_door():
    return render_template('Door.html',pagename='Olayiwola Aluminum Project-Door')

@app.route('/project/railing')
def project_railing():
    return render_template('Railing.html',pagename='Olayiwola Aluminum Project-Railing')

@app.route('/project/window')
def project_window():
    return render_template('Window.html',pagename='Olayiwola Aluminum Project-Window')

@app.route('/project/others')
def project_others():
    return render_template('Others.html',pagename='Olayiwola Aluminum Project-Others')

@app.route('/project/supply')
def project_supply():
    return render_template('Supply.html',pagename='Olayiwola Aluminum Project-Supply')
#end


#start
@app.route('/blog/')
def blog():
    return render_template('blog.html',pagename='Olayiwola Aluminum Blog')

@app.route('/blog/article1')
def article_one():
    return render_template('article.html',pagename='Olayiwola Aluminum Blog')

@app.route('/blog/article2')
def article_two():
    return render_template('news.html',pagename='Olayiwola Aluminum Blog')
#end


@app.route('/about/')
def about():
    return render_template('about.html',pagename='About Olayiwola Aluminum')

@app.route('/contact/', methods=['POST','GET'])
def contact():
    if request.method=='GET':
        return render_template('contact.html',pagename='Contact Olayiwola Aluminum')
    else:
        username = request.form.get('username')
        email = request.form.get('mail')
        phone = request.form.get('phone')
        message = request.form.get('msg')
        c =Contact(cont_name=username,cont_email=email,cont_phone=phone,cont_msg=message)
        db.session.add(c)
        db.session.commit()
        return redirect('/contact/')
    
    
    






