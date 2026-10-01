from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 允許你的前端 (fronted) 跨網域存取資料

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "這是來自後端的資料！"})

if __name__ == '__main__':
    app.run(port=8080)