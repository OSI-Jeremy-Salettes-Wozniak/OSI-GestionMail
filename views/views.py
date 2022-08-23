from cProfile import label
from dataclasses import dataclass
import tkinter as tk
from turtle import left

CONST = {
    "title": "Gestion de compte mail",
    "width": 1000,
    "height": 600,
    "bg_principal_windows": "#262626",
    "fg_principal_windows": "#ffffff",
    "police" : ("consolas", 12),
    }
class View():

    """ View de l'application """

    def __init__(self):
        """ Initialisation de la vue """
        self.root = tk.Tk()
        self.root.title(CONST["title"])
        self.root.geometry("{}x{}".format(CONST["width"], CONST["height"]))
        self.root.resizable(False, False)
        self.root.configure(background=CONST["bg_principal_windows"])
        # police consola
        self.root.option_add("*Font", CONST["police"])

    def run(self):
        """ Lance l'application """
        try:
            # Ajouter les functions de la vue
            self.vue_terminal()
            self.vue_imap()
            self.vue_action()
            # Lancement de la vue
            self.root.mainloop()
        except Exception as e:
            print(e)
            self.root.destroy()
            self.root.quit()

# FUNCTION D'OPTIMISATION DE LA VUE
    def label(self, message, background="#ffffff", foreground="#000000"):
        """ Affiche un message dans la vue """
        label = tk.Label(self.root, text=message, bg=background, fg=foreground)
        return label

    def label_parent(self, parent, message, background="#ffffff", foreground="#000000"):
        """ Affiche un message dans la vue """
        label = tk.Label(parent, text=message, bg=background, fg=foreground)
        return label

    def text(self, height, width, background, foreground):
        """ Affiche un text dans la vue """
        text = tk.Text(self.root, height=height, width=width, bg=background, fg=foreground)
        return text

    def button(self, text, width, height, command):
        """ Affiche un bouton dans la vue """
        button = tk.Button(self.root, text=text, width=width, height=height, command=command)
        return button
    def button_parent(self, parent, text, width, height, command):
        """ Affiche un bouton dans la vue """
        button = tk.Button(parent, text=text, width=width, height=height, command=command)
        return button

    def frame(
        self, 
        width, 
        height, 
        background="#ffffff", 
        foreground="#000000"):
        """ Affiche un frame dans la vue """
        frame = tk.Frame(self.root, width=width, height=height, bg=background, borderwidth=1)
        return frame

    def entry(self, parent, width, background, foreground):
        """ Affiche un entry dans la vue """
        entry = tk.Entry(parent, width=width, bg=background, fg=foreground)
        return entry
# VUE
    def vue_terminal(self, list_message=["Console d'affichage des actions..."]):
        """ 
        Affiche un message dans la vue 

        Parametres:
            - message: message à afficher
        """        
        # Création du text
        self.text_terminal = self.text(0, 0, "black", "white")
        self.text_terminal.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #création du scrollbar
        self.scrollbar = tk.Scrollbar(self.text_terminal)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.text_terminal.yview)
        self.text_terminal.config(yscrollcommand=self.scrollbar.set)


        # Ajout des messages dans la console
        for message in list_message:
            self.text_terminal.insert(tk.END, message + "\n")
            self.text_terminal.see(tk.END)
            self.text_terminal.yview(tk.END)
            self.text_terminal.update()  

    def vue_imap(self, data=[
        ['imap_id | imap_server | imap_port | imap_adress | imap_password | imap_folder'], 
        ['--------------------------------------------------------------------------------']
        ]):
        """ Affiche les données de la data sous la forme CSV"""
        # Création du text
        self.text_imap = self.text(10, 80, "white", "black")
        self.text_imap.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        # lis les données de la data
        for line in data:
            self.text_imap.insert(tk.END, line[0] + "\n")
            self.text_imap.see(tk.END)
            self.text_imap.yview(tk.END)
            self.text_imap.update()
    def vue_action(self):
        # Ajoute les buttons d'action d'ajout, de suppression et de modification des comptes imap
        # Label avec le message d'action mail
        self.label_action = self.label("Action mail", background="#262626", foreground="white")
        self.label_action.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.button_ajouter = self.button("Ajouter", 10, 1, self.action_ajouter)
        self.button_supprimer = self.button("Supprimer", 10, 1, self.action_suppression)
        self.button_modifier = self.button("Modifier", 10, 1, self.action_modifier)
        self.button_ajouter.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.button_supprimer.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.button_modifier.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        # Ajoute les boutons de suppression de tout les messages et recuperation des mails
        # label avec le message d'action mail
        self.label_action = self.label("Action multiple", background="#262626", foreground="white")
        self.label_action.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.button_supprimer_tout = self.button("Supprimer tout", 10, 1, self.action_suppression)
        self.button_recuperation = self.button("Recuperation", 10, 1, self.action_recuperation)
        self.button_supprimer_tout.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.button_recuperation.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

    
        
# ACTION
    def action_suppression(self):
        """ Supprime un compte imap """
        # Affiche une fenetre qui demande la confirmation l'id du compte à supprimer
        self.fenetre_suppression = tk.Toplevel(self.root)
        self.fenetre_suppression.title("Suppression")
        self.fenetre_suppression.geometry("200x100")
        self.fenetre_suppression.resizable(False, False)

        # Demande le id du compte à supprimer
        self.label_suppression = self.label_parent(self.fenetre_suppression, "ID à supprimer", background="#262626", foreground="white")
        self.label_suppression.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entry_suppression = self.entry(self.fenetre_suppression, 10, "white", "black")
        self.entry_suppression.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # créer un bouton supprimer et retourner simplement
        self.button_supprimer = self.button("Supprimer", 10, 1, lambda: self.action_suppression(self.entry_suppression.get()))
        self.button_supprimer.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.button_retour = self.button("Retour", 10, 1, self.fenetre_suppression.destroy)
        self.button_retour.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # def action_suppression(self, id):
    #     """ supprime le compte imap """
    #     return id



    def action_modifier(self):
        """ Action de modification des mails """
        print("Action de modification des mails")

    def action_ajouter(self):
        """ Action d'ajout des mails """
        # Création de la fenetre d'ajout de compte imap
        self.fenetre_ajout = tk.Toplevel(self.root)
        self.fenetre_ajout.title("Ajout de compte imap")
        self.fenetre_ajout.geometry("300x400")
        self.fenetre_ajout.resizable(False, False)
        self.fenetre_ajout.config(background="white")

        # Création des labels Et des entries
        self.label_server = self.label_parent(self.fenetre_ajout, "Server", "#262626", "white")
        self.label_server.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entry_server = self.entry(self.fenetre_ajout, 10, "white", "black")
        self.entry_server.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.label_port = self.label_parent(self.fenetre_ajout, "Port", "#262626", "white")
        self.label_port.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entry_port = self.entry(self.fenetre_ajout, 10, "white", "black")
        self.entry_port.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.label_adress = self.label_parent(self.fenetre_ajout, "Adress", "#262626", "white")
        self.label_adress.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entry_adress = self.entry(self.fenetre_ajout, 10, "white", "black")
        self.entry_adress.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.label_password = self.label_parent(self.fenetre_ajout, "Password", "#262626", "white")
        self.label_password.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entry_password = self.entry(self.fenetre_ajout, 10, "white", "black")
        self.entry_password.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.label_folder = self.label_parent(self.fenetre_ajout, "Folder", "#262626", "white")
        self.label_folder.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entry_folder = self.entry(self.fenetre_ajout, 10, "white", "black")
        self.entry_folder.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # stocker les données dans un dictionnaire
        self.dictionnaire = {
            "server": self.entry_server.get(),
            "port": self.entry_port.get(),
            "adress": self.entry_adress.get(),
            "password": self.entry_password.get(),
            "folder": self.entry_folder.get()
        }
        
        # Création du bouton ajouter
    
        self.button_ajouter = self.button_parent(self.fenetre_ajout, "Ajouter", 10, 1, self.ajouter_compte(self.dictionnaire))
        self.button_ajouter.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def fermeture_fenetre_ajout(self):
        """ Ferme la fenetre d'ajout de compte imap """
        self.fenetre_ajout.destroy()
        

    def ajouter_compte(self, list_entry):
        """ Ajoute un compte imap dans la liste des comptes """
        list_entry = list_entry
        

    def action_recuperation(self):
        """ Action de recuperation des mails """
        print("Action de recuperation des mails")

    def action_suppression_tout(self):
        """ Action de suppression de tout les mails """
        print("Action de suppression de tout les mails")
        
        