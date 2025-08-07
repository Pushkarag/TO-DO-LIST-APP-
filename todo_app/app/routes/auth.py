from flask import Blueprint, redirect,render_template,request,url_for,flash,session

auth_bp= Blueprint('auth',__name__)

USER_CREDENTIALS = {    'username':'admin',
    'password':'1234'   
}


@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        
        
        if username==USER_CREDENTIALS['username'] and password==USER_CREDENTIALS['password']:
            session['user']=username
            flash('login successful', 'success')
        else:
            flash ('invalid username or password','danger') 
    return render_template('login.html')

def logout():
    session.pop('user',None)           
    flash ("logged out",'info')
    return redirect(url_for('auth.login'))