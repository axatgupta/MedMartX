
import sqlite3
conn=sqlite3.connect("creden.db") #database connected

rec=conn.execute("SELECT * FROM credentials;")

from flask import Flask,render_template,request,session,redirect
app = Flask(__name__)
app.secret_key = 'yolo'
@app.route("/")
def hello():
	session['query']=''
	return render_template("index.html")

@app.route("/logout")
def logout1():
	session['username']=''
	session['query']=''
	return render_template("index.html")
    
@app.route("/analgesics")
def analgesics():
	return render_template("analgesics.html")

@app.route("/pcare")
def pcare():
	print ("1")
	return render_template("pcare.html")

flag=0
@app.route("/login", methods=['GET','POST'])
def yolo():
	if request.method=="POST":

		user=str(request.form['username'])
		key=str(request.form['passkey'])
		flag=0
		for row in rec:
			if str(row[0])==user and str(row[1])==key:
				session['username']=str(row[2])+str(row[3])
				return redirect("http://localhost:5000")
			

		if flag==0:
			session['query']="Incorrect Credentials, Please try again"
			return render_template("login.html")
	 	
		
@app.route("/signin")
def loadlogin():
	return render_template('login.html')

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

@app.route("/register",methods=['POST','GET'])
def reg():
	message=''
	if request.method=="POST":
		print(request.form)
		fname=str(request.form['fname'])
		lname=str(request.form['lname'])
		email=str(request.form['email'])
		p1=str(request.form['pwdi'])
		p2=str(request.form['pwdf'])
		add=str(request.form['address'])
		mnum=str(request.form['mnum'])

		#inserting values
		if(p1==p2):
			conn.execute("insert into credentials values(?,?,?,?,?,?)",(email,p1,fname,lname,mnum,add))
			message="You have been successfully Registered!"
			session['query']=message
			return render_template("login.html")
		else:
			message="Error! please try again"
			return render_template("registered.html",msg=message)

		
	return render_template("registered.html")
	conn.commit()
@app.route("/antibiotics")
def biot():
	return render_template("antibiotics.html")

if __name__ == "__main__":
    app.run()


conn.close()