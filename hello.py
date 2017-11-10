
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/analgesics")
def analgesics():
	return render_template("analgesics.html")

@app.route("/pcare")
def pcare():
	print ("1")
	return render_template("pcare.html")

@app.route("/login")
def loadlogin():
	return render_template("login.html")
	user=str(request.form['username'])
	key=str(request.form['passkey'])
	
	
@app.route("/contact")
def cont():
	return render_template("contact.html")

@app.route("/about")
def abt():
	return render_template("about.html")

@app.route("/offers")
def offr():
	return render_template("offers.html")

@app.route("/products")
def prod():
	return render_template("products.html")

@app.route("/checkout")
def check():
	return render_template("checkout.html")

@app.route("/register")
def reg():
	return render_template("registered.html")

@app.route("/antibiotics")
def biot():
	return render_template("antibiotics.html")

if __name__ == "__main__":
    app.run()