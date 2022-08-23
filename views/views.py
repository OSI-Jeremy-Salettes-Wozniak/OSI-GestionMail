import tkinter as tk
from turtle import left

class View():
    
#### DEMARRAGE DE LA VUE ####
    def __init__(self):
        """ Constructeur de la classe View """
        self.master = tk.Tk()
        self.master.title("Programme de gestion des mail")
        self.master.geometry("1200x1000")
        # configuration de la fenetre
        self.master.configure(bg="white")
        self.run()

    def run(self):
        """ Lance l'application """
        self.terminal()
        self.imap_data()
        # Créer dans le controller les boutons avec la function qui doit être appelé
        # EN TEST
        self.button(self.quit, "Recuperer les mails")
        self.button(self.allDelete, "Supprimer tout les messages")
        self.button(self.quit, "Quitter")
        # EN TEST
        self.master.mainloop()

#### FUNCTION D'OPTIMISATION



#### FUNCTION D'AFFICHAGE
    def terminal(self, list_message=["Bienvenue dans la console d'affichage..."]):
        """ Affiche un message dans la console """
        # Création de la bordure frame de la console terminal
        self.frame_terminal = tk.Frame(self.master, bg="white", relief=tk.SUNKEN, borderwidth=1)
        self.frame_terminal.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        # Création du texte frame de la console terminal
        self.console_terminal = tk.Text(self.frame_terminal, bg="black", fg="#ffffff", relief=tk.SUNKEN, borderwidth=1)
        self.console_terminal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # height doit faire la taille des frames
        self.console_terminal.configure(height=20, width=100)
        
        # Ajout des messages dans la console
        for message in list_message:
            self.console_terminal.insert(tk.END, message)
            self.console_terminal.insert(tk.END, "\n")
        # Scrollbar de la console terminal
        self.scrollbar_terminal = tk.Scrollbar(self.frame_terminal, command=self.console_terminal.yview)
        self.scrollbar_terminal.pack(side=tk.LEFT, fill=tk.Y)
        self.console_terminal.config(yscrollcommand=self.scrollbar_terminal.set)
        self.console_terminal.config(state=tk.DISABLED)
        self.console_terminal.config(font=("Consolas", 12))
        # Faire défiler la console terminal
        self.console_terminal.yview(tk.END)
        self.console_terminal.config(state=tk.NORMAL)
        self.console_terminal.see(tk.END)
        self.console_terminal.config(state=tk.DISABLED)      

    def button(self, function, text):
        """ Création d'un bouton """
        return tk.Button(self.master, text=text, command=function, bg="white", fg="black", relief=tk.RAISED, borderwidth=1).pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def entry(self, text):
        """ Création d'une entrée """
        return tk.Entry(self.master, text=text, bg="white", fg="black", relief=tk.RAISED, borderwidth=1)

    def quit(self):
        """ Quitter l'application """
        self.master.destroy()

    def allDelete(self):
        """ Supprime tous les messages """
        pass

    def imap_data(self, data_imap=[["test", "test"], ["test", "test"]]):
        """ Affiche les données de imapdata.csv dans le dossier data """
        # Création de la frame contenant les données du compte imap side left both expand
        self.frame_imap_data = tk.Frame(self.master, bg="white", relief=tk.SUNKEN, borderwidth=1)
        self.frame_imap_data.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        # Création du texte frame des données du compte imap
        self.console_imap_data = tk.Text(self.frame_imap_data, bg="white", fg="black", relief=tk.SUNKEN, borderwidth=1)
        self.console_imap_data.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        # Ajoute une entête id_imap, imap_server, imap_adress, imap_password, imap_port, imap_folder
        self.console_imap_data.insert(tk.END, "id_imap | imap_server | imap_adress | imap_password | imap_port | imap_folder\n")
        self.console_imap_data.insert(tk.END, "--------------------------------------------------------------------------------\n")
        
        # Ajout des messages dans la console
        for message in data_imap:
            # Ajout des case à cocher pour la selection des comptes imap
            self.console_imap_data.insert(tk.END, message)
            self.console_imap_data.insert(tk.END, "\n")
            

        # Scrollbar de la console imap data
        self.scrollbar_imap_data = tk.Scrollbar(self.frame_imap_data, command=self.console_imap_data.yview)
        self.scrollbar_imap_data.pack(side=tk.LEFT, fill=tk.Y)
        self.console_imap_data.config(yscrollcommand=self.scrollbar_imap_data.set)
        self.console_imap_data.config(state=tk.DISABLED)
        self.console_imap_data.config(font=("Consolas", 12))
        
        # Faire défiler la console imap data
        self.console_imap_data.yview(tk.END)
        self.console_imap_data.config(state=tk.NORMAL)
        self.console_imap_data.see(tk.END)
        self.console_imap_data.config(state=tk.DISABLED)

        # Affiche les boutons de modification, suppression et ajout sour la console imap data
        self.button(self.add, "Ajouter")
        self.button(self.modify, "Modifier")
        self.button(self.delete, "Supprimer")

    def modify(self):
        """ Modifie un compte imap """
        pass

    def delete(self):
        """ Supprime un compte imap """
        pass

    def add(self):
        """ Ajoute un compte imap """
        pass



        
if __name__ == "__main__":
    views = View()
    views.run()
