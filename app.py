import sys
import subprocess
import re
from flask import Flask ,render_template,request,redirect,send_file,Flask,send_from_directory
app=Flask(__name__,static_url_path='/static')
@app.route("/", methods=["GET","POST"])
def index():

           


    return render_template("index.html",transcript=transcript,graphJSON=graphSON)
def topwords(counts):
    topcount=dict()
    for k,v in counts.items():
        if v  >> 1:
            if len(k)>=3:
               topcount[k]=v 
            
    return topcount        
if __name__=="__main__" :
    app.run(debug=True,threaded=True)  
