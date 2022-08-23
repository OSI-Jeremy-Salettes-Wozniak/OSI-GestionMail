# Importation des bibliotheque
import csv
import os
import tkinter as tk
import imaplib

# Importation des modeles, views et controllers
from models.models import  ImapModel
from views.views import View
from controllers.controllers import Controllers

class App:
    """
    Application de gestion de compte imap
    """

    def __init__(self):
        """
        Initialisation de l'application

        attributs:
            - controller: Controllers
            - model: ImapModel
            - view: View
            

        """
        self.model = ImapModel()
        self.view = View()
        self.controller = Controllers(self.model, self.view)

    def run(self):
        """
        Lance l'application
        """
        self.controller.run()

if __name__ == "__main__":
    app = App()
    app.run()


