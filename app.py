# Importation des bibliotheque
import csv
import os
import tkinter as tk
import imaplib

# Importation des modeles
from models.models import  ImapModel
# Importation des views
from views.views import View
# Importation des controllers
from controllers.controllers import Controllers

# Création de la classe App
class App:

    """
    Application de gestion de compte imap
    """

    def __init__(self):
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


