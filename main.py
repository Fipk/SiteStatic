from markdown2 import Markdown

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
