import sqlite3
from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route('/')
def demo1():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signup')
def sign():
    return render_template('signup.html')   
conn=sqlite3.connect('usersDB.db') 
print("Database opened")

# conn.execute('CREATE TABLE users(user TEXT,email TEXT,pswd TEXT,npswd TEXT)')
# print ("Table created")
# conn.close()

@app.route('/register', methods=['POST', 'GET'])
def register():
    msg=""
    if request.method == "POST":
        try:
            user = request.form['user']
            email = request.form['email']
            pswd = request.form['pswd']
            npswd= request.form['npswd']
            with sqlite3.connect("usersDB.db") as conn:
                cur = conn.cursor()
                cur.execute('INSERT INTO users(user,email,pswd,npswd) values(?,?,?,?)',(user,email,pswd,npswd))
                conn.commit()
                msg="User Added"
        except:
            con.rollback()
            msg="Not added"
        finally:
            return render_template('check.html', info=msg)
            conn.close()



if __name__=='__main__':
    app.run(debug=True)