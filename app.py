import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route để hiển thị giao diện HTML
@app.route('/')
def index():
    return render_template('index.html')

# Route để xử lý yêu cầu từ giao diện
@app.route('/predict', methods=['POST'])
def ask():
    question = request.form.get('message')  # Lấy dữ liệu từ form
    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Trả về dữ liệu giả lập để kiểm tra
    return jsonify({"answer": f"Your question was: {question}"})

if __name__ == '__main__':
    app.run(debug=True)
