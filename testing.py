from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/",methods=["GET"])
def main():
    return "Hello, I am a service now ! Thanks you !! UwU"

if(__name__=="__main__"):
    app.run(debug=True)
