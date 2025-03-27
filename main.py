from flask import Flask, render_template, request, redirect
import os
from os import path

global whichfilename;
whichfilename = "LoginAccounts.doc"
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/info", methods=["POST"])
def GetInfo():
    global username
    global userpasswd
    username = request.form.get('txtusername')
    userpasswd = request.form.get('txtpassword')
    if(username == "" or userpasswd == ""):
        return render_template("index.html")
    else:
        CreateCheckFile()
        return render_template("index2.html", username = username, password = userpasswd)

def CreateCheckFile():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(whichfilename))
    if(fileexist == False):
        status = "new"
    else:
        status = "edit"

    WriteToFile(status)

def WriteToFile(whichstatus):
    if(whichstatus == "new"):
        logacctfile = open(whichfilename, "x")
        logacctfile.close()
        logacctfile = open(whichfilename, "w")
    else:
        logacctfile = open(whichfilename, "a")

    logacctfile.write(username + " " + userpasswd)
    ReadFromFile()

def ReadFromFile():
    logacctfile = open(whichfilename, "r")
    username_passwords = logacctfile.readlines()
    print(username_passwords)

if __name__ == "__main__":
    app.run()
