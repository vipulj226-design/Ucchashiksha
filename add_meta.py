import os
import glob
from bs4 import BeautifulSoup

def add_meta_tags():
    directory = r'C:\Users\VIPUL\.gemini\antigravity\playground\static-stellar\ucchashiksha'
    html_files = glob.glob(os.path.join(directory, '*.html'))

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        head = soup.find('head')
        
        if head:
            # Check if favicon already exists
            if not soup.find('link', rel='icon'):
                favicon = soup.new_tag('link', rel='icon', href='assets/logo.jpg', type='image/jpeg')
                head.append(favicon)
                
            # Check if og:image exists
            if not soup.find('meta', property='og:image'):
                og_image = soup.new_tag('meta', property='og:image', content='assets/logo.jpg')
                head.append(og_image)
                
            if not soup.find('meta', property='og:title'):
                title = soup.find('title')
                og_title_content = title.text if title else 'Uccha Shiksha | Higher Education Advisory Service'
                og_title = soup.new_tag('meta', property='og:title', content=og_title_content)
                head.append(og_title)
                
            if not soup.find('meta', property='og:description'):
                desc = soup.find('meta', attrs={'name': 'description'})
                og_desc_content = desc['content'] if desc else 'Higher Education Advisory Service'
                og_desc = soup.new_tag('meta', property='og:description', content=og_desc_content)
                head.append(og_desc)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated {filepath}")

if __name__ == "__main__":
    add_meta_tags()
