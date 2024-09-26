from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/admin', methods=['GET'])
def proxy():
    url = "https://peeker.acectf.site/admin"
    headers = {
        'referer': 'http://127.0.0.1'
    }
    response = requests.get(url, headers=headers)
    return response.text

if __name__ == '__main__':
    app.run(port=5000)