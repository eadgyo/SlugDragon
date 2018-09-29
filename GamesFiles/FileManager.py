class FileManager:
    def __init__(self) :
        pass

    def readFile(self, name) :
        fichier = open(name, "r")
        liste = []

        for ligne in fichier :
            L = str(ligne)
            liste.append(L)
        fichier.close()
        
        return liste

    def saveFile(self, name, text) :
        fichier = open(name, 'a')
        fichier.write(' \n' + text)
        fichier.close()