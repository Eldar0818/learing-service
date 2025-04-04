from flask import Flask, render_template
from data import products_list

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", products=products_list)

@app.route("/create")
def create():
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)
