from flask import Flask,render_template, request,redirect,flash,session
from oapp import app
from oapp.models import db,Admin,Contact


@app.route("/admin/login",methods=['GET','POST'])
def adminlogin():
    if request.method=='GET':
        return render_template("admin/login.html")
    else:
        username= request.form.get('username')
        pwd= request.form.get('password')
        chk= db.session.query(Admin).filter(Admin.admin_name==username,Admin.admin_password==pwd).count()
        if chk:
            session['admin_loggedin']=True
            return redirect('/admin/dashboard')
        else:
            flash('Incorrect credentials')
            return redirect('/admin/login')
        

@app.route('/admin/logout')
def admin_logout():
    if session.get('admin_loggedin'):
        session.pop('admin_loggedin',None)
        flash('You have logged out successfully...',category="success")
    return redirect('/admin/login')



@app.route("/admin/dashboard")
def adminhome():
     userdeets = db.session.query(Contact).all()
     if session.get('admin_loggedin')==None:
        flash("Access Denied",category="danger")
        return redirect('/admin/login')
     return render_template("admin/admin_dashboard.html", userdeets= userdeets)


