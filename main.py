from flask import Flask, jsonify, render_template, request
import dropbox
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

class TransferData:
    def _init_(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_upload(file_from, file_to)
@app.route('/<fileName>',methods=['POST'])
def postvideo(fileName):
    transferData = TransferData('OF6GR3NX3fQAAAAAAAAAAS8S3eIa51ubPKoTKeeDFCvbnEiAUawjecXHPi0aVwfA')
    file_from = request.data
    if(len(fileName)>0):
        file_to = '/test_dropbox/'+fileName+'.mp4'
        transferData.upload_file(file_from, file_to)
        return jsonify('success')
    else:
        return jsonify('error')
