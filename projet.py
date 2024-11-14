import tkinter as tk
from tkinter import Menu

# Création de la fenêtre principale
waberi = tk.Tk()
waberi.title(" Interface avec Menu" )
waberi.geometry("640x480 ")  # Taille de la fenêtre

# Création de la barre de menus
Menu_bar = Menu(root)

# Création des menus
Menu_fichier = Menu(menu_bar, tearoff=0)
Menu_creation = Menu(menu_bar, tearoff=0)
Menu_affichage = Menu(menu_bar, tearoff=0)
Menu_execution = Menu(menu_bar, tearoff=0)
Menu_edition = Menu(menu_bar, tearoff=0)

# Ajout des menus à la barre de menus
Menu_bar.add_cascade(label= "Fichier ", menu=menu_fichier)
Menu_bar.add_cascade(label= "Créations ", menu=menu_creation)
Menu_bar.add_cascade(label= 'Affichage ', menu=menu_affichage)
Menu_bar.add_cascade(label= 'Exécution ', menu=menu_execution)
Menu_bar.add_cascade(label= 'Édition ', menu=menu_edition)


# Configurer la barre de menu dans la fenêtre principale
Root.config(menu=menu_bar)

# Lancement de la boucle principale
Root.mainloop()
