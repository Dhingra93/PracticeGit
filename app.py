## Flask app routing 
from flask import Flask,render_template,request,redirect,url_for,jsonify

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

@app.route('/fail/<int:score>')
def fail(score):
    return "The person faile with the score : "+str(score)
 

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='GET':
        return render_template('form.html')
    else:
        maths=float(request.form('maths'))
        science=float(request.form('science'))
        history=float(request.form('history'))

        average_marks=(maths+science+history)/3
        
    #return render_template(url_for(results.html,results=average_marks))

@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()
    dt=dict(data)
    return jsonify(float(dt['a'])+float(dt['b']))


if __name__=="__main__":
    app.run(debug=True)