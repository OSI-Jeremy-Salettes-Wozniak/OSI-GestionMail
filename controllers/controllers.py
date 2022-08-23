class Controllers:

    def __init__(self, models, views):
        self.model = models
        self.views = views

    def run(self):
        """
        Lance la vue l'application
        """
        self.views.run()

    def action_ajouter(self):
        """
        Ajoute un compte imap
        """
        dictionnaire_imap_account = self.views.action_ajouter()
        self.model.ajouter_imap_account(dictionnaire_imap_account)
        