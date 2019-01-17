changed_lines = None

# Écriture dans le fichier html_file.html
with open("./file_generated.html", "w") as sorted_file:
    # Interprétation des caractères spéciaux
    sorted_file.write("""<meta charset="UTF-8"/>\n\n""")
    # Lecture du fichier test_file.md
    with open("./input_file.md") as open_file:
        for lines in open_file:
            lines = "  " + lines
            print(lines)
            # Convertion des titres Markdown
            if lines.startswith("  # ") == True:
                changed_lines = lines.replace("  # ", "<h1>")
                changed_lines = changed_lines.replace("\n", "</h1>\n")
                sorted_file.write(changed_lines)
            elif (
                lines.startswith("  ## ") == True
                or lines.startswith("    ## ") == True
            ):
                changed_lines = lines.replace("  ## ", "<h2>")
                changed_lines = changed_lines.replace("\n", "</h2>\n")
                sorted_file.write(changed_lines)
            elif lines.startswith("  ### ") == True:
                changed_lines = lines.replace("  ### ", "<h3>")
                changed_lines = changed_lines.replace("\n", "</h3>\n")
                sorted_file.write(changed_lines)
            else:
                sorted_file.write(lines)
