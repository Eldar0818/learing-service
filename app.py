from flask import Flask, abort, render_template
from data import products_list

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", products=products_list)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/product/<string:pid>")
def product_info(pid):
    product = next((pd for pd in products_list if pd["id"] == pid), None)
    if product is None:
        abort(404)
        
    return render_template("information.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
