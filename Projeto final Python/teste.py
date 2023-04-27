from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("teste.html")

def startbot():
    print("ok")
    return exec(open("app.py").read())

if __name__ == "__main__":
    app.run()