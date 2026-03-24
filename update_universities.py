import re

filepath = r'C:\Users\VIPUL\.gemini\antigravity\playground\cryo-triangulum\ucchashiksha\universities.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# remove old style
text = re.sub(r'<style>.*?</style>', '', text, flags=re.DOTALL)

# extract main and inner states
main_match = re.search(r'<main.*?>(.*?)</main>', text, flags=re.DOTALL)
if main_match:
    main_inner = main_match.group(1)
    
    # parse the header
    h1 = re.search(r'<h1>(.*?)</h1>', main_inner).group(1)
    p_match = re.search(r'<p.*?>(.*?)</p>', main_inner, flags=re.DOTALL)
    p = p_match.group(1).strip() if p_match else ""
    
    new_main = f'''<main class="container" style="text-align: left;">
            <div style="text-align: center; margin-bottom: 50px;">
                <h1 style="color: var(--primary-color); font-size: 2.5rem; margin-bottom: 20px;">{h1}</h1>
                <p style="font-size: 1.1rem; color: #555; max-width: 800px; margin: 0 auto; line-height: 1.6;">{p}</p>
            </div>
            
            <div class="card-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
'''
    
    states = re.findall(r'<div class="state-group">(.*?)</div>', main_inner, flags=re.DOTALL)
    for i, state in enumerate(states):
        h3_match = re.search(r'<h3>(.*?)</h3>', state)
        if not h3_match:
            continue
        h3 = h3_match.group(1)
        
        lis = re.findall(r'<li>(.*?)</li>', state, flags=re.DOTALL)
        
        is_last = (i == len(states) - 1)
        
        if is_last:
            new_main += f'''
                <div class="premium-card" style="grid-column: 1 / -1; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; background-color: var(--primary-color); color: white;">
                    <div style="flex: 1; min-width: 300px;">
                        <h3 style="color: white; font-size: 1.8rem; margin-bottom: 15px; border-bottom: none;">{h3}</h3>
'''
            for li in lis:
                new_main += f'                        <p style="font-size: 1.05rem; opacity: 0.9; margin-bottom: 10px; line-height: 1.5;">{li.strip()}</p>\n'
            new_main += '''                    </div>
                    <a href="contact-us.html" class="btn-primary" style="background-color: white; color: var(--primary-color); margin-top: 20px;">Get More Info</a>
                </div>
'''
        else:
            new_main += f'''
                <div class="premium-card">
                    <h3 style="color: var(--accent-blue); font-size: 1.4rem; margin-bottom: 15px; border-bottom: 2px solid var(--accent-blue); padding-bottom: 10px; display: inline-block;">{h3}</h3>
                    <ul style="list-style-type: none; padding: 0;">
'''
            for li in lis:
                new_main += f'                        <li style="margin-bottom: 10px; padding-left: 25px; position: relative; line-height: 1.5; color: #555;"><span style="position: absolute; left: 0; top: 0; color: #25D366; font-weight: bold;">✓</span> {li.strip()}</li>\n'
            new_main += '''                    </ul>
                </div>
'''

    new_main += '''            </div>
        </main>'''
        
    text = re.sub(r'<div style="background-color: #ffffff; padding: 40px.*?<main.*?</main>\n    </div>', f'<div style="background-color: var(--bg-primary); padding: 40px 20px; min-height: calc(100vh - 100px);">\n        {new_main}\n    </div>', text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
print("Universities updated successfully")
