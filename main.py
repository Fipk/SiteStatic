# Importation des librairies
import markdown2
import argparse

def convert_MdFile_to_HTMLFile(inputFile, outputFile):
    """
    Fonction gérant la conversion des fichiers Markdown en fichiers HTML
    """
    # Création et écriture du fichier HTML
    with open(f"./{outputFile}.html", "w") as output_file:
        # Ouverture du fichier et lecture du fichier Marckdown
        with open(f"./{inputFile}", "r") as input_file:
            # Ajout de l'en-tête
            output_file.write("<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='utf-8'/>\n\t<title>MDtoHTML</title>\n\t<link rel='stylesheet' type='text/css' href='main.css'/>\n</head>\n<body>\n")
            # Conversion du fichier Markdown en HTML
            for lines in input:
                output_file.write(markdown2.markdown(lines))
            # Fermeture des balises "body" et "/html"
            output_file.write("</body>\n</html>")

print("Générateur de site statique.\n")

# Création du manuel de l'application
parser = argparse.ArgumentParser(description="Convert a markdown folder to an HTML folder")
parser.add_argument("-i",
    "--input-directory",
    help="open the folder containing the markdown files to convert",
    action="store_true",)
parser.add_argument("-o",
    "--output-directory",
    help="create the folder containing the files converted to HTML",
    action="store_true",)
args = parser.parse_args()

print("Les fichiers Markdown ont bien été convertis en HTML.")

# Appel de la fonction de conversion
convert_MdFile_to_HTMLFile(args.input, args.output)
