from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# In-memory database to hold neighborhood messages
neighborhood_messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=neighborhood_messages)

@app.route('/post_message', methods=['POST'])
def post_message():
    message = request.form.get('message')
    username = request.form.get('username')
    neighborhood_messages.append({"username": username, "message": message})
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)

