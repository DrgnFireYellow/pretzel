import argparse
from pathlib import Path
import directives
import webbrowser
import os

argumentparser = argparse.ArgumentParser("pretzel", description="Convert a Pretzel presentation to an html file.")
argumentparser.add_argument("file")
args = argumentparser.parse_args()

presentationfile = open(args.file)

presentationcontents = presentationfile.readlines()

output = '<!DOCTYPE html><html><link href="https://unpkg.com/prismjs@v1.x/themes/prism.css" rel="stylesheet" /><script src="https://unpkg.com/prismjs@v1.x/components/prism-core.min.js"></script><script src="https://unpkg.com/prismjs@v1.x/plugins/autoloader/prism-autoloader.min.js"></script><style>html {scroll-snap-type: y mandatory; scrollbar-width: none;} .slide {height: 100vh; scroll-snap-align: start;} img {width: 50vw}</style>'

for line in presentationcontents:
    if line.startswith("@"):
        if line.strip() == "@startslide":
            output += '<div class="slide">'
        elif line.strip() == "@endslide":
            output += "</div>"
        else:
            linedata = line.strip().split()
            output += eval(f"directives.{linedata[0].strip('@')}")(*linedata[1:])
    else:
        output += f"<p>{line}</p>"
output += "</html>"

presentationfile.close()

with open(Path(args.file).stem + ".html", "w") as outputfile:
    outputfile.write(output)

webbrowser.open("file://" + os.path.realpath(Path(args.file).stem + ".html"))