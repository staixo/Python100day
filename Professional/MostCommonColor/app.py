from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from PIL import Image
from collections import Counter

def analyze_colors(file_path):
    image = Image.open(file_path)
    image = image.convert('RGB')
    colors = image.getdata()

    color_counts = Counter(colors)
    most_common_colors = color_counts.most_common(10)  # Adjust the number as needed

    return [color[0] for color in most_common_colors]


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/henripeters/Documents/Projetperso/Python100day/Professional/MostCommonColor/static/uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file uploaded', 400

    file = request.files['image']
    if file.filename == '':
        return 'No file selected', 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        colors = analyze_colors(file_path)

        return render_template('result.html', colors=colors)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


if __name__ == '__main__':
    app.run(debug=True)
