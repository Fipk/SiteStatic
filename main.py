# Importation des librairies
import markdown2
import argparse
import os

def convert_MdFile_to_HTMLFile(inputFile, outputFile):
    """
    Fonction gérant la conversion des fichiers Markdown en fichiers HTML
    """
    # Création d'une liste avec tous les fichiers Markdown
    folder = os.listdir(inputFolder)
    for files in folder:
        f = open(f'{inputFolder}/{files}', "r")
        titleFile = os.path.splitext(files)[0]
        print("Les fichiers Markdown ont bien été convertis en HTML.")
        HTMLFile = open(f"{outputFolder}/{titleFile}.html", "w")
            # Ajout de l'en-tête
            HTMLFile.write("<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='utf-8'/>\n\t<title>MDtoHTML</title>\n\t<link rel='stylesheet' type='text/css' href='main.css'/>\n</head>\n<body>\n")
            # Conversion du fichier Markdown en HTML
            HTMLFile.write(markdown2.markdown(f.read()))
            # Fermeture des balises "body" et "/html"
            HTMLFile.write("\n</body>\n</html>")

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

# Appel de la fonction de conversion
convert_MdFile_to_HTMLFile(args.input, args.output)
