from flask import Flask, render_template, request, send_file, redirect, url_for, session
import requests
import json
import time
import subprocess
import sys
import os
import socket

app = Flask(__name__)

ipAddressWebServer1 = "13.79.217.165:8080"
ipAddressWebServer2 = "40.69.204.130:8080"

# 0 - is RoundRobin, 1 - Weighted Round Robin
strategy = 1

# 0 - ipAddressWebServer1, 1 - ipAddressWebServer2
roundRobin = 0

loadWebServer1 = 0
loadWebServer2 = 0


@app.route('/', methods=["GET"])
def qwerty():
    response = loadBanacer()
    return str(response)


@app.route("/changeStrategy", methods = ["GET"])
def zxcvb():
    if strategy == 0:
        strategy = 1
    else:
        strategy = 0
    return 0

def loadBanacer():
    # Route for RoundRobin
    if strategy == 0:
        ipAddressWebServer = ""
        if roundRobin == 0:
            ipAddressWebServer = ipAddressWebServer1
            roundRobin = 1
        else:
            ipAddressWebServer = ipAddressWebServer2
            roundRobin = 0
        response = requests.get("http://" + ipAddressWebServer + "/")
        return str(response.content)
    if strategy == 1:
        loadWebServer1 = requests.get("http://" + ipAddressWebServer1 + "/load")
        loadWebServer2 = requests.get("http://" + ipAddressWebServer2 + "/load")
        if loadWebServer1 > loadWebServer2:
            ipAddressWebServer = ipAddressWebServer2
        else:
            ipAddressWebServer = ipAddressWebServer1
        response = requests.get("http://" + ipAddressWebServer + "/")
        return str(response.content)
    
if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0',port="8080")
