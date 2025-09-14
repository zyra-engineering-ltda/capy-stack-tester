from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    logo_path = os.path.join(app.static_folder, 'images', 'logo.png')
    logo_url = None
    if os.path.exists(logo_path):
        logo_url = url_for('static', filename='images/logo.png')
    return render_template('index.html', logo_url=logo_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
