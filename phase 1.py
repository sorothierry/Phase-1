


import tkinter as tk
from tkinter import messagebox

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("TIC-TAC-TOE")

# Définir la liste des chiffres de 1 à 9
chiffres = list(range(1, 10))

# Initialiser la variable mark
mark = ''

# Initialiser la variable count
count = 0

# Créer la liste panels avec 10 éléments
panels = ['panel'] + list(range(1, 10))

# Afficher la fenêtre Tkinter
root.mainloop()