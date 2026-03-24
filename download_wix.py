import os
import glob
import requests
from bs4 import BeautifulSoup
import hashlib
from urllib.parse import urlparse

def download_and_replace():
    directory = r'C:\Users\VIPUL\.gemini\antigravity\playground\static-stellar\ucchashiksha'
    assets_dir = os.path.join(directory, 'assets')
    os.makedirs(assets_dir, exist_ok=True)
    html_files = glob.glob(os.path.join(directory, '*.html'))

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'html.parser')
        modified = False

        for img in soup.find_all('img'):
            src = img.get('src')
            if src and src.startswith('http'):
                url_hash = hashlib.md5(src.encode('utf-8')).hexdigest()[:8]
                parsed = urlparse(src)
                ext = '.jpg'
                if '.png' in parsed.path.lower(): ext = '.png'
                if '.webp' in parsed.path.lower(): ext = '.webp'
                filename = f"external_{url_hash}{ext}"
                local_path = os.path.join(assets_dir, filename)

                if not os.path.exists(local_path):
                    try:
                        print(f"Downloading {src}")
                        # Provide a User-Agent to avoid quick blocks
                        headers = {'User-Agent': 'Mozilla/5.0'}
                        r = requests.get(src, stream=True, headers=headers, timeout=10)
                        if r.status_code == 200:
                            with open(local_path, 'wb') as out_f:
                                for chunk in r.iter_content(1024):
                                    out_f.write(chunk)
                            print(f"Saved to {local_path}")
                        else:
                            print(f"Failed {r.status_code}")
                    except Exception as e:
                        print(f"Error {e}")

                img['src'] = f"assets/{filename}"
                modified = True

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated {filepath}")

if __name__ == "__main__":
    download_and_replace()
