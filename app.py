from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# Path to the static directory containing 13 folders with images
STATIC_DIR = "static"

@app.route('/')
def index():
    # Get all folders inside the static directory
    folders = [folder for folder in os.listdir(STATIC_DIR) if os.path.isdir(os.path.join(STATIC_DIR, folder))]
    return render_template('index.html', folders=folders)

@app.route('/slider/<folder_name>')
def slider(folder_name):
    folder_path = os.path.join(STATIC_DIR, folder_name)
    
    if not os.path.exists(folder_path):
        return "Folder not found", 404

    images = [img for img in os.listdir(folder_path) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return render_template('slider.html', images=images, folder=folder_name)

if __name__ == '__main__':
    app.run(debug=True)
