from flask import Flask,request,render_template,redirect,session,url_for
from werkzeug.security  import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.secret_key="your_secret_key"

#configure sqlalchemy to work with flask

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///users.db"#name of db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

#create database for my application
db=SQLAlchemy(app)
#how to put info into database:--->
#database model
#create a clss model
#model is going to represent a single row
class User(db.Model):
    #inherit from db ,model is from sqlalchemy
    #3 header names for our database(3 columns)
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),unique=True,nullable=False)
    password_hash=db.Column(db.String(50),nullable=False)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template("index.html")




@app.route("/login",methods=["POST"])
def login():
    #collect info from the form
    username=request.form["username"]
    password=request.form["password"]
    #create an object of the model(class) and make a query  to our database to check for username
    user=User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session["username"]=username
        return redirect(url_for('dashboard'))
    else:
        return render_template("index.html")


 #register
@app.route("/register",methods=["POST"])
def register():
    username=request.form["username"]
    password=request.form["password"]
    user=User.query.filter_by(username=username).first()

    if user:
        return render_template ("index.html",error="user already here")
    else:
        new_user=User(username=username)
        new_user.set_password(password)
        #send it to the database
        db.session.add(new_user)
        db.session.commit()
        #create a new session and redirect user to the dashboard
        session["username"]=username
        return redirect(url_for('dashboard'))


@app.route("/dashboard")
def dashboard():
    if "username"in session:       
        return render_template("dashboard.html",username=session['username'])
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    session.pop("username", None)  # remove username from session
    return redirect(url_for("home"))

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)