from markdown2 import Markdown
import argparse

parser = argparse.ArgumentParser(
    description="Convert a markdown folder to an HTML folder"
)
parser.add_argument(
    "-i",
    "--input",
    help="open the folder containing the markdown files to convert",
    action="store_true",
)
parser.add_argument(
    "-o",
    "--output",
    help="create the folder containing the files converted to HTML",
    action="store_true",
)
args = parser.parse_args()
if args.input:
    print("Open folder is '{}'".format(__file__))
if args.output:
    print("Create folder is '{}'".format(__file__))

md = Markdown()

# Écriture dans le fichier HTML
with open("./index.html", "w") as exit_file:
    exit_file.write("<meta charset='UTF-8'/>\n")
    # Lecture du fichier Markdown
    with open("./input_file.md", "r") as open_file:
        for lines in open_file:
            print(lines)
            # Gestion des titres indentés
            if lines.startswith("  ##") == True:
                lines = lines.replace("  ## ", "<h2>")
                lines = lines.replace("\n", "</h2>\n")
            # Gestion des liens URL
            if (
                lines.startswith("http") == True
                or lines.startswith("* http") == True
            ):
                lines = lines.replace("http", '<a href="http')
                lines = lines.replace("\n", '">hyperlien</a>\n')
            elif lines.startswith("un texte") == True:
                exit_file.write("<p>")
                lines = lines.replace("http", '<a href="http')
                lines = lines.replace(
                    ".com et encore du texte",
                    '.com">hyperlien</a> et encore du texte</p>',
                )
            lines = md.convert(lines)
            exit_file.write(lines)
