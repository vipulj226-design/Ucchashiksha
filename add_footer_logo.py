import os
import glob

def add_footer_logo():
    logo_html = '''
        <div class="container footer-logo-container" style="text-align: center; margin-bottom: 40px; padding-bottom: 30px; border-bottom: 1px solid rgba(0,0,0,0.1);">
            <img src="assets/logo.jpg" alt="Uccha Shiksha Logo" style="max-height: 80px; width: auto; max-width: 100%; object-fit: contain;">
        </div>'''
    
    html_files = glob.glob('C:/Users/VIPUL/.gemini/antigravity/playground/cryo-triangulum/ucchashiksha/*.html')
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # For contact-us.html
        if '<footer class="footer" style="background-color: white; color: #333;">' in content:
            if 'footer-logo-container' not in content:
                content = content.replace('<footer class="footer" style="background-color: white; color: #333;">', 
                                          '<footer class="footer" style="background-color: white; color: #333;">' + logo_html)
        
        # For others
        elif '<footer class="footer">' in content:
            if 'footer-logo-container' not in content:
                content = content.replace('<footer class="footer">', 
                                          '<footer class="footer">' + logo_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Logo successfully injected into all footers.")

if __name__ == '__main__':
    add_footer_logo()
