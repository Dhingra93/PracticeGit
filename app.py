## Flask app routing 
from flask import Flask

#starting point  
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>My first Welcome Page</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "My first Index Page"

##Variable Rule 
@app.route('/success/<int:score>')
def success(score):
    return "The person passed with the score : "+str(score)

if __name__=="__main__":
    app.run(debug=True)