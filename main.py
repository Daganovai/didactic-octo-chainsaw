from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = 'AIzaSyA6q4x6i3yGQ2ZkyHPAnQRrGHQUc-IPGxs'  # Замените на ваш API ключ
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

@app.route('/proxy-request', methods=['POST'])
def proxy_request():
    data = request.json
    try:
        response = requests.post(API_URL, json=data)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
