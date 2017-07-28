import ocr
import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

_uploadfolder = 'bills'
_allowedextensions = set(['jpg','jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = _uploadfolder


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    json_object = ocr.subprocess_main_call("bills/"+file.filename)

    return jsonify(json_object)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
'''
import socket
import sys
import time
import datetime
import ocr

_host = 'localhost'
_port = 3002
_serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
_serversocket.bind((_host, _port))
_serversocket.listen(10)
i = 1

while True:
	_csock, _caddr = _serversocket.accept()


	#_fileid = datetime.datetime.fromtimestamp(time.time()).strftime('%Y/%m/%d_%H/%M/%S')
	_file = open(str(i) + '.jpg','wb')
	i += 1

	while (True):
		l = _csock.recv(1024)
		while (l):
			_file.write(l)
			l = _csock.recv(1024)

		_file.close()

	json_object = ocr.subprocess_main_call("image_" + _fileid + ".jpg")
	_csock.send(json_object)
	_csock.close()

_serversocket.close()

'''
