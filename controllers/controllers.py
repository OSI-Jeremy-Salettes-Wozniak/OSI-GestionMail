class Controllers:

    def __init__(self, models, views):
        self.model = models
        self.views = views

    def run(self):
        """
        Lance l'application
        """
        # TEST
        self.model.testModels()
        print("Controllers")

        # Appelez les methodes de liaison entre les modeles et les vues
        self.add_imap_account()
    

    # def les methodes de laison du modele et de la vue
    def add_imap_account(self):
        # Retourne valeur du formulaire
        values = self.views.get_imap_account()
        # Ajoute compte dans file imapdata.csv
        self.model.add_imap_account(values)
        # print(values)
        print(self.model.add_imap_account(values))



































































    # def affichage_app(self):
    #     """
    #     Affiche la page d'accueil
    #     """
    #     newView = self.views
    #     newView.app_screen()
        
    # def add_imap_account(self):
    #     """
    #     Ajoute un compte imap
    #     """
    #     # associer une variable à chaque champ du formulaire
    #     imap_server = self.views.get_imap_account_info()['imap_server']
    #     imap_port = self.views.get_imap_account_info()['imap_port']
    #     imap_adress = self.views.get_imap_account_info()['imap_adress']
    #     imap_password = self.views.get_imap_account_info()['imap_password']
    #     imap_folder = self.views.get_imap_account_info()['imap_folder']
    #     # ajouter le compte imap dans la base de données
    #     self.model.add_imap_account(imap_server, imap_port, imap_adress, imap_password, imap_folder)
