from flask import Flask, render_template
# from waitress import Serve

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    # return " Welcome to my page created by python "
    return render_template("index.html")

@app.route("/home")
def  home_page():
    
    return " Welcome to my home page"


if __name__ == "__main__":
#    serve(app,host= "0.0.0.0", debug = True)
    app.run(host= "0.0.0.0")
