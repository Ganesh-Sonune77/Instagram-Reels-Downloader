📥 Instagram Reels Downloader (Flask + yt-dlp)

A lightweight Flask web app that lets you download Instagram reels easily using yt-dlp.
It automatically saves each reel with a unique index (reel1.mp4, reel2.mp4, …), extracts captions, and stores them neatly.

🚀 Features

✅ Download Instagram reels by pasting links.

✅ Multiple reel URLs at once (newline-separated).

✅ Auto-increment file names (reel1.mp4, reel2.mp4, etc.).

✅ Captions extracted from metadata and saved as .txt files.

✅ .info.json files auto-deleted after processing.

✅ Simple and responsive web interface.

✅ Ready for local or deployment use.

📂 Project Structure
├── app.py                 # Flask web server
├── download_reels.py      # Core reel downloading + caption extraction
├── requirements.txt       # Dependencies
├── static/
│   ├── reels/             # Downloaded reels (.mp4)
│   ├── titles/            # Extracted captions (.txt)
│   └── ... (assets, if any)
├── templates/
│   ├── index.html         # Input form UI
│   └── downloads.html     # Download list UI

⚙️ Installation

Clone the repo

git clone https://github.com/Ganesh-Sonune77/Instagram-Reels-Downloader.git
cd reels-downloader


Create & activate a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run the Flask app

python app.py


Open in browser:

http://127.0.0.1:5000

🖥️ Usage

Paste one or multiple Instagram reel URLs into the input box.
(Example reels provided in demo.txt).

Hit Download.

Reels are saved under:

Videos → static/reels/reelX.mp4

Captions → static/titles/reelX.txt

Visit /downloads to browse & download files.

🛠️ Tech Stack

Flask – Web framework

yt-dlp – Reel downloader

Python 3.8+

📜 License

MIT License © 2025 Ganesh-Sonune77
