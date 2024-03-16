import html

def heading(*args):
    text = ""
    for arg in args:
        text += arg + " "
    return f"<h1>{html.escape(text)}</h1>"

def small(*args):
    text = ""
    for arg in args:
        text += arg + " "
    return f"<small>{html.escape(text)}</small>"

def image(source: str):
    return f'<img src="{html.escape(source)}"><br>'

def primarycolor(color: str):
    return '<style>body {color: %s;}</style>' % color

def secondarycolor(color: str):
    return '<style>body {background-color: %s;}</style>' % color

def font(font: str):
    return '<style>body {font-family: %s;}</style>' % font

def justify(value: str):
    return '<style>body {text-align: %s;}</style>' % value

def code(sourcefile: str, language: str):
    with open(sourcefile) as source:
        return f'<pre><code class="language-{html.escape(language)}">{html.escape(source.read())}</code></pre>'