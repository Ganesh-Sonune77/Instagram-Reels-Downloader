import subprocess
import os
import json
import shutil
import sys

def get_yt_dlp_path():
    yt_dlp_path = shutil.which('yt-dlp')
    if yt_dlp_path:
        return yt_dlp_path

    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"], check=True)
        yt_dlp_path = shutil.which('yt-dlp')
        if yt_dlp_path:
            return yt_dlp_path
    except Exception as pip_error:
        print(f"❌ pip install failed: {pip_error}")

    fallback_path = os.path.expanduser(r"~\yt-dlp.exe")
    if os.path.isfile(fallback_path):
        return fallback_path

    embedded_path = os.path.join(os.path.dirname(__file__), 'yt-dlp.exe')
    if os.path.isfile(embedded_path):
        return embedded_path

    raise FileNotFoundError("🚫 'yt-dlp' not found. Auto-install and fallback paths failed.")

def get_next_index(path, prefix, ext):
    existing = [f for f in os.listdir(path) if f.startswith(prefix) and f.endswith(ext)]
    numbers = [int(f[len(prefix):-len(ext)].lstrip('_')) for f in existing if f[len(prefix):-len(ext)].lstrip('_').isdigit()]
    return max(numbers + [0]) + 1

def download_single_reel(reel_url, reels_path, titles_path_unused):
    yt_dlp_path = get_yt_dlp_path()
    os.makedirs(reels_path, exist_ok=True)
    os.makedirs('static/titles', exist_ok=True)  # Fixed path

    index = get_next_index(reels_path, 'reel', '.mp4')
    base_name = f"reel{index}"
    output_template = os.path.join(reels_path, f"{base_name}.%(ext)s")

    command = [
        yt_dlp_path,
        '--no-mtime',
        '--write-info-json',
        '-o', output_template,
        reel_url
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"❌ yt-dlp download failed for {reel_url}: {e}")

    # Caption Extraction and JSON deletion
    json_file = f"{base_name}.info.json"
    info_path = os.path.join(reels_path, json_file)
    if os.path.isfile(info_path):
        try:
            with open(info_path, 'r', encoding='utf-8') as f:
                info = json.load(f)
            caption = info.get('description', '').strip()
            if caption:
                caption_file_path = os.path.join('static/titles', f"{base_name}.txt")
                with open(caption_file_path, 'w', encoding='utf-8') as cf:
                    cf.write(caption)
            # Delete JSON only after successful caption extraction
            os.remove(info_path)
        except Exception as ex:
            print(f"⚠️ Caption extraction or JSON deletion failed for {json_file}: {ex}")
