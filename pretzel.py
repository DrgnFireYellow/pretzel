import argparse
from pathlib import Path
import directives

argumentparser = argparse.ArgumentParser("pretzel", description="Convert a Pretzel presentation to an html file.")
argumentparser.add_argument("file")
args = argumentparser.parse_args()

presentationfile = open(args.file)

presentationcontents = presentationfile.readlines()

output = '<!DOCTYPE html><html><style>html {scroll-snap-type: y mandatory;} .slide {height: 100vh; scroll-snap-align: start;} img {width: 50vw}</style>'

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
