from pygments import highlight
from pygments.lexers import CppLexer
from pygments.formatters import HtmlFormatter

code = '''
Total garlic count is: 156226
Total garlic count should be: 200000
'''

formatter = HtmlFormatter(style="friendly", full=True, linenos=True)
html_output = highlight(code, CppLexer(), formatter)

# Save to file
with open("highlighted_code.html", "w") as f:
    f.write(html_output)
