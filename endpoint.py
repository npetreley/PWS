"""endpoint.py is a web service listener for updates to a contact's presence

Copyright (c) 2018 Cisco and/or its affiliates.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import json
import subprocess
from lxml import etree
from flask import Flask, request

# We use "flask" to create the web service to respond to presence notifications
# We use "requests" to execute REST operations to get presenced status
# We use "lxml" to manipulate XML into data that "requests" can use
# We use "json" to read in json files with data such as server, username, password

app = Flask(__name__)

# This endpoint web service responds to a GET REST request
# that notifies us that a presence status has changed

@app.route('/pws',methods=['GET'])
def pws():
	id = str(request.args.get('id'))
	etype = str(request.args.get('eventType'))
	print("id ="+id+" etype="+etype+"\n")
	print("Processing Notification\n")
	subprocess.run("python3 get_subscribed_presence.py "+id+" "+etype, shell=True)
	return('id = '+id+' etype='+etype)

@app.errorhandler(404)
def not_found(error):
	return(error)

# Get the host IP address for this web service

with open('serverparams.json') as json_file:
	data = json.load(json_file)
	for p in data['params']:
		HOST = p['HOST']

app.run(host=HOST, port=8080)
