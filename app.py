from flask import Flask, render_template, request, send_file, redirect, url_for, session
import psutil
#import requests
import json
import time
import subprocess
import sys
import os
import socket

app = Flask(__name__)

@app.route("/")
def func():
    html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/>"    
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())   
 

@app.route("/load")
def load():
    load = psutil.cpu_percent()
    return str(load)

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0',port="8080")
