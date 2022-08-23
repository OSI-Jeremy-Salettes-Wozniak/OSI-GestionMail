import csv
import os
import imaplib

class ImapModel(object):

    def __init__(self) -> None:
        
        pass

    def testModels(self):
        print("testModels")

    def add_imap_account(self, values):
        print("add_imap_account")














































































    # # def __init__(self, imap_server="", imap_port=None, imap_adress="", imap_password="", imap_folder=""):
    # #     self.imap_server = imap_server
    # #     self.imap_port = imap_port
    # #     self.imap_adress = imap_adress
    # #     self.imap_password = imap_password
    # #     self.imap_folder = imap_folder
    # #     self.id_imap = None

    # # def connection(self):
    # #     """
    # #     open connection to the imap server
    # #     """
    # #     self.server = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
    # #     self.connection = self.server.login(self.imap_adress, self.imap_adress)
    # #     if self.connection[0] == "OK":
    # #         print("Vous etes connect : " + self.imap_adress)
    # #     else:
    # #         print("Erreur de connection")
    # #     return self.connection

    # # def deconnection(self):
    # #     """
    # #     close connection to the imap server
    # #     """
    # #     self.server.close()
    # #     self.server.logout()

    # # def add_imap_account(self, name_protocol=""):
    # #     """
    # #     save data
    # #     """
    # #     try:
    # #         # Créer un dossier data dans le dossier courant si il n'existe pas et créer un fichier imapdata.csv dans le dossier data si il n'existe pas
    # #         if not os.path.exists("data"):
    # #             os.makedirs("data")
    # #         if not os.path.exists("data/imapdata.csv"):
    # #             with open("data/imapdata.csv", "w") as f:
    # #                 header_imap_data = "id_imap, name_protocol, imap_server, imap_port, imap_adress, imap_password, imap_folder"
    # #                 f.write(header_imap_data + "\n")
    # #         # Ecrire les données dans le fichier imapdata.csv
    # #         with open("data/imapdata.csv", "a") as f:
    # #             # pour chaque ligne on créer un id_imap qu'on incrémente de 1
    # #             self.id_imap = len(open("data/imapdata.csv").readlines())
    # #             # si adresse mail existe deja dans le fichier on ne créer pas une nouvelle ligne
    # #             if self.imap_adress in open("data/imapdata.csv").read():
    # #                 print("Adresse mail existe deja")  
    # #             else:
    # #                 line_imap_data = str(self.id_imap) + "," + name_protocol + "," + self.imap_server + "," + str(self.imap_port) + "," + self.imap_server + "," + self.imap_password + "," + self.imap_folder
    # #                 f.write(line_imap_data + "\n")
    # #                 print("Donnees enregistrees")
    # #     except Exception as e:
    # #         print(e)

    # # def delete(self):
    # #     """
    # #     delete data
    # #     """
    # #     try:
    # #         # supprimer la ligne correspondant à l'adresse mail dans le fichier imapdata.csv
    # #         with open("data/imapdata.csv", "r") as f:
    # #             lines = f.readlines()
    # #             for line in lines:
    # #                 if self.imap_adress in line:
    # #                     lines.remove(line)
    # #                     with open("data/imapdata.csv", "w") as f:
    # #                         f.writelines(lines)
    # #                         print("Donnees supprimées")
    # #     except Exception as e:
    # #         print(e)

    # # def get(self):
    # #     """
    # #     get data
    # #     """
    # #     try:
    # #         # lire les données dans le fichier imapdata.csv
    # #         with open("data/imapdata.csv", "r") as f:
    # #             lines = f.readlines()
    # #             for line in lines:
    # #                 if self.imap_adress in line:
    # #                     print(line)
    # #     except Exception as e:
    # #         print(e)

    # # def update(self, name_protocol, imap_host, imap_port, imap_adress, imap_password, imap_folder):
    #     """
    #     update data
    #     """
    #     try:
    #         # modifier les données dans le fichier imapdata.csv
    #         with open("data/imapdata.csv", "r") as f:
    #             lines = f.readlines()
    #             for line in lines:
    #                 if self.imap_adress in line:
    #                     lines.remove(line)
    #                     line_imap_data = str(self.id_imap) + "," + name_protocol + "," + imap_host + "," + str(imap_port) + "," + imap_adress + "," + imap_password + "," + imap_folder
    #                     lines.append(line_imap_data)
    #                     with open("data/imapdata.csv", "w") as f:
    #                         f.writelines(lines)
    #                         print("Donnees modifiees")
    #     except Exception as e:
    #         print(e)