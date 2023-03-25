#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Yanis 03/03/2023


import os
import random
import string   
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox


# Fonction pour générer un mot de passe maître
def generate_master_password():
    key = Fernet.generate_key()
    with open('master.key', 'wb') as f:
        f.write(key)

# Fonction pour lire le mot de passe maître
def read_master_password():
    with open('master.key', 'rb') as f:
        return f.read()

# Création du fichier de stockage des mots de passe chiffrés
def create_password_file():
    with open('passwords.txt', 'w'):
        pass

# Fonction de chiffrement
def encrypt_password(password):
    key = read_master_password()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Fonction de déchiffrement
def decrypt_password(encrypted_password):
    key = read_master_password()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    return decrypted_password.decode()

# Fonction pour enregistrer un nouveau mot de passe
def save_password(website, username, password):
    with open('passwords.txt', 'a') as f:
        f.write(f"{website}, {username}, {encrypt_password(password).decode()}\n")
    messagebox.showinfo("Enregistrement réussi", "Mot de passe enregistré avec succès!")

# Fonction pour afficher les mots de passe déchiffrés
def view_passwords():
    passwords = []
    with open('passwords.txt', 'r') as f:
        for line in f:
            website, username, password = line.strip().split(',')
            passwords.append((website, username, decrypt_password(password.encode())))

    if passwords:
        password_list_window = tk.Toplevel(window)
        password_list_window.title("Liste des mots de passe")
        password_list_window.geometry("600x400")


        scrollbar = tk.Scrollbar(password_list_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        password_list = tk.Listbox(password_list_window, yscrollcommand=scrollbar.set)
        password_list.pack(expand=True, fill=tk.BOTH)

        for website, username, password in passwords:
            password_list.insert(tk.END, f"Site Web: {website}, Nom d'utilisateur: {username}, Mot de passe: {password}")

        scrollbar.config(command=password_list.yview)

    else:
        messagebox.showinfo("Pas de mots de passe", "Vous n'avez pas encore enregistré de mots de passe.")

# Fonction pour générer un mot de passe aléatoire
def generate_random_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Fonction appelée lorsque le bouton Enregistrer est cliqué
def on_save_button_click():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    save_password(website, username, password)
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Fonction appelée lorsque le bouton Générer est cliqué
def on_generate_button_click():
    password = generate_random_password()  # appelle la fonction pour générer un mot de passe aléatoire
    password_entry.delete(0, tk.END)  # supprime le contenu de l'entry pour le mot de passe
    password_entry.insert(0, password)  # insère le mot de passe généré dans l'entry pour le mot de passe

# Fonction appelée lorsque le bouton Enregistrer est cliqué
def on_save_button_click():
    website = website_entry.get()  # récupère le nom du site web dans l'entry correspondante
    username = username_entry.get()  # récupère le nom d'utilisateur dans l'entry correspondante
    password = password_entry.get()  # récupère le mot de passe dans l'entry correspondante
    save_password(website, username, password)  # appelle la fonction pour enregistrer le mot de passe
    website_entry.delete(0, tk.END)  # supprime le contenu de l'entry pour le nom du site web
    username_entry.delete(0, tk.END)  # supprime le contenu de l'entry pour le nom d'utilisateur
    password_entry.delete(0, tk.END)  # supprime le contenu de l'entry pour le mot de passe
    

while True:
    username = input("Nom d'utilisateur: ")
    password = input("Mot de passe: ")
    if username == "YNTA" and password == "YNTA":
        print("C'est ouvert !")
        break
    else:
        print("Nom d'utilisateur ou mot de passe incorrect !")
        

    # Vérifier si les fichiers existent, sinon les créer
if not os.path.isfile('master.key'):
    generate_master_password()
if not os.path.isfile('passwords.txt'):
    create_password_file()


# Création de la fenêtre principale
window = tk.Tk()  # crée une instance de la classe Tk de la bibliothèque tkinter
window.title("Gestionnaire de mots de passe")  # définit le titre de la fenêtre
window.iconbitmap("ciphersafe.ico")

# Création des widgets de l'interface graphique
website_label = tk.Label(window, text="Nom du site web:")  # crée un label pour le nom du site web
website_label.grid(column=0, row=0)  # place le label dans la fenêtre

website_entry = tk.Entry(window)  # crée un entry pour le nom du site web
website_entry.grid(column=1, row=0)  # place l'entry dans la fenêtre

username_label = tk.Label(window, text="Nom d'utilisateur:")  # crée un label pour le nom d'utilisateur
username_label.grid(column=0, row=1)  # place le label dans la fenêtre

username_entry = tk.Entry(window)  # crée un entry pour le nom d'utilisateur
username_entry.grid(column=1, row=1)  # place l'entry dans la fenêtre

password_label = tk.Label(window, text="Mot de passe:")  # crée un label pour le mot de passe
password_label.grid(column=0, row=2)  # place le label dans la fenêtre

password_entry = tk.Entry(window)  # crée un entry pour le mot de passe
password_entry.grid(column=1, row=2)  # place l'entry dans la fenêtre

generate_button = tk.Button(window, text="Générer", command=on_generate_button_click)  # crée un bouton pour générer un mot de passe
generate_button.grid(column=2, row=2)  # place le bouton dans la fenêtre

save_button = tk.Button(window, text="Enregistrer", command=on_save_button_click)  # crée un bouton pour enregistrer le mot de passe
save_button.grid(column=1, row=3)  #

# Crée un bouton pour enregistrer le mot de passe
save_button = tk.Button(window, text="Enregistrer", command=on_save_button_click)
save_button.grid(column=1, row=3)

# Crée un bouton pour enregistrer le mot de passe
save_button = tk.Button(window, text="Mot de passe enregistré", command=view_passwords)
save_button.grid(column=0, row=3)

# Crée un bouton pour quitter l'application
quit_button = tk.Button(window, fg = 'red', text="Quitter", command=window.quit)
quit_button.grid(column=2, row=3)

# Lance la boucle principale
window.mainloop()