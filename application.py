import os

from flask import Flask, request, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("1.html")









@app.route("/new", methods=["POST","GET"])
def new():
   return render_template("register.html",error="")



@app.route("/registered", methods=["POST"])
def registered():
    name=request.form.get("name")
    
    password=request.form.get("password")
    person = db.execute("SELECT * FROM users WHERE name = :name", {"name": name}).fetchall()
    if person is None or len(person)==0:
        db.execute("INSERT INTO users (name, password) VALUES (:name, :password)",
                  {"name": name, "password": password})
        db.commit()
        return render_template("success.html")
        
    else :
        return render_template("failure.html") 















@app.route("/login", methods=["POST","GET"])
def login():
    return render_template("log.html")

@app.route("/check", methods=["POST", ])
def op():
    name=request.form.get("name")
    
    password = request.form.get("password")
    persons = db.execute("SELECT* FROM users ").fetchall()
    
    
    if persons is None :
        
        return render_template("ui.html") 
    else :
        
        for person in persons :
            
            if name == person.name and password == person.password :
                
                
                return render_template("name.html",name=name)
               
    return render_template("ui.html") 













if __name__ == '__main__':
    app.run(debug=True)