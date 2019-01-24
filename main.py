import http.server

PORT = 8080
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["./dossier_site_statique"]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()


changed_lines = None
number_asterix = 0

# Écriture dans le fichier html_file.html
with open("./dossier_site_statique/file_generated.html", "w") as sorted_file:
    # Interprétation des caractères spéciaux
    sorted_file.write("""<meta charset="UTF-8"/>\n\n""")
    # Lecture du fichier test_file.md
    with open("./input_file.md") as open_file:
        for lines in open_file:
            lines = "  " + lines
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
                # Conversion de la mise en gras
                for element in lines:
                    if element == "*":
                        number_asterix += 1
                    else:
                        number_asterix
                if number_asterix == 2:
                    changed_lines = lines.replace(" *", "<strong>")
                    changed_lines = lines.replace("*", "</strong>")
                    sorted_file.write(changed_lines)
                else:
                    changed_lines = lines.replace("*", "<li>")
                    sorted_file.write(changed_lines)
                # else:
                #    sorted_file.write(lines)
