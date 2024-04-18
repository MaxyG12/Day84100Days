from flask import Flask, request, redirect
from replit import db

app = Flask(__name__, static_url_path='/static')


db["david"] = {"password" : "Baldy1"}
db["katie"] = {"password" : "k8t"}

@app.route('/login', methods=["POST"])
def login():
  form = request.form
  try:
    if db[request.form["username"]] ["password"]== request.form["password"]:
      return redirect("/yup")
    else:
      return redirect("/nope")
  except:
    return redirect("/nope")


@app.route("/nope")
def nope():
  return """<img src="static/nerdy.gif" height="100">"""

@app.route("/yup")
def yup():
  page = """<img src="static/yup.gif" height="100">"""
  f = open("change.html", "r")
  page += f.read()
  f.close()
  return page

@app.route("/changePass", methods=["POST"])
def change():
  form = request.form
  db[request.form["username"]] ["password"]= request.form["newPassword"]
  return f"""Password changed to {request.form['newPassword']}"""

@app.route('/')
def index():
  page = ""
  f = open("login.html", "r")
  page = f.read()

  return page

app.run(host='0.0.0.0', port=81)
  