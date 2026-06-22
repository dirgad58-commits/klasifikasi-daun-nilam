import sys

with open('c:/Dirga/klasifikasi_nilam_deploy/app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

css_code = """
st.markdown('''
<div id='main-card'></div>
<style>
div.element-container:has(#main-card) + div.element-container > div[data-testid="stVerticalBlock"] {
    background: #ffffff !important;
    padding: 40px 35px !important;
    border-radius: 24px !important;
    box-shadow: 0 15px 40px -5px rgba(15, 23, 42, 0.1) !important;
    border: 1px solid #e2e8f0 !important;
    margin-top: 20px !important;
    margin-bottom: 25px !important;
}
</style>
''', unsafe_allow_html=True)

main_container = st.container()
with main_container:
"""

new_lines = lines[:190]
new_lines.append(css_code)

skip = False
for i, line in enumerate(lines[190:]):
    if 'st.markdown("""' in line and lines[190+i+1].strip() == '<style>':
        skip = True
    
    if skip:
        if '""", unsafe_allow_html=True)' in line:
            skip = False
        continue
        
    if line.strip():
        new_lines.append('    ' + line)
    else:
        new_lines.append(line)

# Since I went till the end of lines, I don't need extend
with open('c:/Dirga/klasifikasi_nilam_deploy/app.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Done!')
