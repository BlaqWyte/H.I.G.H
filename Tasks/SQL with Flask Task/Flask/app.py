from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/kizz", methods =["POST", "GET"])
def login():
    if (request.method == "POST"):
        email = request.form["mail"]
        password = request.form["pass"]
        print ("Email= ", email,"Password" password)
        return ("sucessfully logged in")
    return render_template("login.html")
 
if __name__ == "__main__":
    app.run()