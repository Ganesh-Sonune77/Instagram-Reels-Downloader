from flask import Flask, render_template, request, redirect, send_from_directory, flash
import os
import traceback
from download_reels import download_single_reel

app = Flask(__name__)
app.secret_key = 'your-secret-key'

DOWNLOAD_FOLDER = 'static/reels'
CAPTIONS_FOLDER = os.path.join(DOWNLOAD_FOLDER, 'captions')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        urls_input = request.form['insta_url']
        urls = [url.strip() for url in urls_input.split('\n') if url.strip()]
        try:
            for url in urls:
                download_single_reel(url, DOWNLOAD_FOLDER, CAPTIONS_FOLDER)
            return redirect('/downloads')
        except Exception:
            flash(f"⚠️ Error: {traceback.format_exc()}", 'danger')
    return render_template('index.html')

@app.route('/downloads')
def show_downloads():
    files = os.listdir(DOWNLOAD_FOLDER)
    return render_template('downloads.html', files=files)

@app.route('/reels/<filename>')
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
