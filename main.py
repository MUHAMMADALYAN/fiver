from flask import Flask, jsonify, render_template, request
import dropbox
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_upload(file_from, file_to)

@app.route('/<fileName>', methods=['POST'])
def postvideo(fileName):
    try:
        transferData = TransferData('aUsaG2MmUQwAAAAAAAAAAdHIYJ488NOgUu0kqoy0LalHNNzErxlUfcZGwKyvAz0_')
        file_from = request.data
        if (len(fileName) > 0):
            file_to = '/videos/' + fileName + '.mp4'
            transferData.upload_file(file_from, file_to)
            return jsonify('success')
        else:
            return jsonify('error')
    except Exception as e:
        return jsonify(e)
