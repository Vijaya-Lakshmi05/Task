from flask import Flask,render_template,request,redirect,url_for
import sqlite3

app = Flask( __name__)

def check_user(username,password):
    conn=sqlite3.connect('user.db')
    cur=conn.cursor()
    cur.execute('select username,password from student where username=?,password=?',(username,password))
    
    data=cur.fetchall
    if len(data)!=0:
        return True
    else:
        return False
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register' , methods=['POST','GET'])
def login():
    new_user = request.form['username']
    new_pwd=request.form['password']
    new_email=request.form['email']
    new_phone=request.form['phone']

    conn=sqlite3.connect('user.db')
    cur=conn.cursor()

    cur.execute('INSERT INTO student (username,password,email,phone) values(?,?,?,?)',(new_user,new_pwd,new_email,new_phone))
    conn.commit()

    return render_template('index.html',info="successfully added student details")

@app.route('/login-form', methods=["GET","POST"])
def login_user():
 
    if request.method=='POST':  
        username=request.form['userName']
        password=request.form['userPassword']
        if check_user(username,password):
            return render_template('home.html')
        else:
            return render_template('index.html')
            
       
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

