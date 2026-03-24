import re
from bs4 import BeautifulSoup
import os

courses_file = r'C:\Users\VIPUL\.gemini\antigravity\playground\cryo-triangulum\ucchashiksha\courses.html'
universities_file = r'C:\Users\VIPUL\.gemini\antigravity\playground\cryo-triangulum\ucchashiksha\universities.html'

def process_file(filepath, header_title, header_subtitle, group_class):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove old inline styles
    style_tags = soup.find_all('style')
    for style in style_tags:
        style.decompose()

    # Find main
    main_tag = soup.find('main')
    
    # Extract groups
    groups = main_tag.find_all('div', class_=group_class)
    
    # Build new main
    new_main = soup.new_tag('main', attrs={'class': 'container', 'style': 'padding: 40px 20px; text-align: left;'})
    
    header_div = soup.new_tag('div', attrs={'style': 'text-align: center; margin-bottom: 50px;'})
    h1 = soup.new_tag('h1', attrs={'style': 'color: var(--primary-color); font-size: 2.5rem; margin-bottom: 20px;'})
    h1.string = header_title
    p = soup.new_tag('p', attrs={'style': 'font-size: 1.1rem; color: #555; max-width: 800px; margin: 0 auto;'})
    p.string = header_subtitle
    
    header_div.append(h1)
    header_div.append(p)
    new_main.append(header_div)
    
    grid = soup.new_tag('div', attrs={'class': 'card-grid', 'style': 'grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); margin-top: 40px;'})
    
    for idx, group in enumerate(groups):
        card = soup.new_tag('div', attrs={'class': 'premium-card'})
        h3_orig = group.find('h3')
        
        h3 = soup.new_tag('h3', attrs={'style': 'color: var(--accent-blue); font-size: 1.4rem; margin-bottom: 15px; border-bottom: 2px solid var(--accent-blue); padding-bottom: 10px; display: inline-block;'})
        if h3_orig:
            h3.string = h3_orig.text
            card.append(h3)
            
        desc = group.find('p')
        if desc:
            p_new = soup.new_tag('p', attrs={'style': 'font-size: 1.05rem; color: #555; line-height: 1.6;'})
            p_new.string = desc.text
            card.append(p_new)
            
        ul = group.find('ul')
        if ul:
            ul_new = soup.new_tag('ul', attrs={'style': 'list-style-type: none; padding: 0;'})
            for li in ul.find_all('li'):
                li_new = soup.new_tag('li', attrs={'style': 'margin-bottom: 10px; padding-left: 25px; position: relative; color: #555;'})
                check = soup.new_tag('span', attrs={'style': 'position: absolute; left: 0; top: 0; color: #25D366; font-weight: bold;'})
                check.string = '✓'
                li_new.append(check)
                li_new.append(" " + li.text.strip())
                ul_new.append(li_new)
            card.append(ul_new)
            
        # Special styling for last card if it's the Abroad card in courses
        if group_class == 'course-group' and idx == len(groups) - 1:
            card['style'] = 'grid-column: 1 / -1; text-align: center; background-color: var(--primary-color); color: white;'
            h3['style'] = 'color: white; font-size: 1.8rem; margin-bottom: 15px; border-bottom: none;'
            if ul_new:
                for li in ul_new.find_all('li'):
                    li['style'] = 'margin-bottom: 10px; padding-left: 25px; position: relative; color: white;'
                    li.find('span')['style'] = 'position: absolute; left: 0; top: 0; color: white; font-weight: bold;'

        grid.append(card)
        
    new_main.append(grid)
    
    # Replace old main with new main
    wrapper = soup.find('div', style=re.compile('min-height: calc.*'))
    if wrapper:
        wrapper.replace_with(new_main)
    else:
        main_tag.replace_with(new_main)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filepath}")

# Update Courses
process_file(courses_file, "All Courses List and Details", "Discover the wide array of courses we offer. From secondary certifications to advanced doctorates, find the perfect program for your academic journey.", 'course-group')

# Update Universities
process_file(universities_file, "Universities Recognized by Uccha Shiksha", "Indian Higher Education Advisory Service is Authorized by these Universities belonging to all states. These include Government, Deemed, and Private Universities.", 'state-group')

