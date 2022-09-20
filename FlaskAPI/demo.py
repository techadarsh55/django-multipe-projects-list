from flask import *

f = Flask(__name__)

@f.route("/")
def home():
    return "<h1>Hello Welcome to api</h1>"

@f.route("/check/<int:no>")
def check_no(no):
    d={}
    if no%2==0:
        d["Number"]=no
        d["status"]=True
        d["description"]="This is Even NUmber"
    else:
        d["Number"]=no
        d["status"]=False
        d["description"]="This is Odd NUmber"
    return jsonify(d)
  
@f.route("/name")
def show():
    name = input("Enter the Name: ")
    email = input("Enter the Email: ")
    contact = int(input("Entet the Contact:"))
    age = int(input("Enter the age:"))
    data = {'Name':name,'Email':email,'Contact':contact,'Age':age}
    
    if name is None and email is None:
        return "<h2>please filled the all deatils</h2>"
    else:
        return f"<h2>{name}</h2><h2>{email}</h2><h2>{contact}</h2><h2>{age}</h2>" and data

if __name__ == "__main__":
    f.run(debug=True,host="0.0.0.0")
