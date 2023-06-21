from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    text = request.form['text']
    if text:
        return jsonify({'status': 'success', 'text': text})
    else:
        return jsonify({'status': 'error', 'message': 'No text provided.'})

if __name__ == '__main__':
    app.run(debug=True)
