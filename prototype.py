import tkinter
import ctypes
import tkinter as tk
import customtkinter as ctk
from connexiondb import connexion_db
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from sqlalchemy import create_engine, text
from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel

session_factory = connexion_db()


try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass


def two_funcs(f1, f2):
    def execute(*args, **kwargs):
        try:
            result = f1(*args, **kwargs)
            if result:
                f2(*args, **kwargs)
        except Exception as e:
            print("Erreur :", e)
    return execute


def formulaire_connexion():
    fenetre.update_idletasks()
    largeur = fenetre.winfo_width()
    hauteur = fenetre.winfo_height()
    x = fenetre.winfo_x()
    y = fenetre.winfo_y()
    fenetre.withdraw()
    fenetre_connexion = tk.Toplevel(fenetre)
    fenetre_connexion.title("Connexion")
    fenetre_connexion.geometry(f"{largeur}x{hauteur}+{x}+{y}")
    fenetre_connexion.configure(bg="#576238")

    def annuler():
        fenetre_connexion.update_idletasks()
        largeur = fenetre_connexion.winfo_width()
        hauteur = fenetre_connexion.winfo_height()
        x = fenetre_connexion.winfo_x()
        y = fenetre_connexion.winfo_y()
        fenetre.geometry(f"{largeur}x{hauteur}+{x}+{y}")
        fenetre.deiconify()
        fenetre_connexion.destroy()

    # choix d'onglets

    tabview = ctk.CTkTabview(fenetre_connexion, corner_radius=50, segmented_button_fg_color="black",
                             segmented_button_unselected_color="black", text_color="#f0eadc", fg_color="black", border_width=10)
    tabview.pack(fill="y", expand=False, padx=20, pady=30)

    # COMPTE CLIENT

    tabview.add("Se connecter en tant que \n client")
    nom_client_label = customtkinter.CTkLabel(tabview.tab(
        "Se connecter en tant que \n client"), text="Nom")
    nom_client_label.pack(pady=2)
    nom_client = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n client"), width=200, height=40)
    nom_client.pack(pady=2)
    prénom_client_label = customtkinter.CTkLabel(tabview.tab(
        "Se connecter en tant que \n client"), text="prénom")
    prénom_client_label.pack(pady=2)
    prénom_client = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n client"), width=200, height=40)
    prénom_client.pack(pady=2)
    mots_de_passe_client_label = customtkinter.CTkLabel(tabview.tab(
        "Se connecter en tant que \n client"), text="Mots de passe")
    mots_de_passe_client_label.pack(pady=2)
    mots_de_passe_client = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n client"), width=200, height=40)
    mots_de_passe_client.pack(pady=2)
    num_téléphone_client_label = customtkinter.CTkLabel(tabview.tab(
        "Se connecter en tant que \n client"), text="Numéro de téléphone")
    num_téléphone_client_label.pack(pady=2)
    num_téléphone_client = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n client"), width=200, height=40)
    num_téléphone_client.pack(pady=2)

    def valider_connexion_client():
        nom_client = nom_client.get().strip()
        prenom_client = prénom_client.get().strip()
        mots_de_passe_client = mots_de_passe_client.get().strip()
        num_téléphone_client = num_téléphone_client.get().strip()
        if not nom_client or not prenom_client or not mots_de_passe_client or not num_téléphone_client:
            messagebox.showwarning(
                "Erreur", "veuillez remplir tous les champs")
            return
        session = session_factory()
        try:
            session.execute(
                text("""
                            INSERT INTO acheteur (nom, prénom, mots_de_passe, num_téléphone)
                            VALUES (:nom, :prénom, :mots_de_passe, :num_téléphone)
                        """),
                {
                    "nom": nom_client,
                    "prénom": prenom_client,
                    "mots_de_passe": mots_de_passe_client,
                    "num_téléphone": num_téléphone_client
                },
            )
            session.commit()
            messagebox.showinfo(
                "compte créé", f"Bienvenue {nom_client} {prenom_client}.")
        except Exception as e:
            session.rollback()
            messagebox.showerror(
                "erreur", f"impossible d'ajouter le compte : {e}")
        finally:
            session.close()

    def espace_client():
        d = 1

    # BOUTTON CLIENTS

    button = customtkinter.CTkButton(
        tabview.tab("Se connecter en tant que \n client"), text="Créer un compte", command=valider_connexion_client)
    button.pack(side="right", padx=20, pady=20)
    button.configure(width=200, height=60,
                     fg_color="#2872a1", corner_radius=10)
    button = customtkinter.CTkButton(
        tabview.tab("Se connecter en tant que \n client"), text="Annuler", command=annuler)
    button.pack(side="left", padx=20, pady=20)
    button.configure(width=200, height=60,
                     fg_color="#fb3640", corner_radius=10)

    # COMPTE REVENDEUR

    tabview.add("Se connecter en tant que \n revendeur")
    nom_revendeur_label = customtkinter.CTkLabel(
        tabview.tab("Se connecter en tant que \n revendeur"), text="Nom")
    nom_revendeur_label.pack(pady=2)
    nom_revendeur = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n revendeur"), width=200, height=40)
    nom_revendeur.pack(pady=2)
    prénom_revendeur_label = customtkinter.CTkLabel(tabview.tab(
        "Se connecter en tant que \n revendeur"), text="Prénom")
    prénom_revendeur_label.pack(pady=2)
    prénom_revendeur = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n revendeur"), width=200, height=40)
    prénom_revendeur.pack(pady=2)
    mots_de_passe_revendeur_label = customtkinter.CTkLabel(
        tabview.tab("Se connecter en tant que \n revendeur"), text="Mots_de_passe")
    mots_de_passe_revendeur_label.pack(pady=2)
    mots_de_passe_revendeur = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n revendeur"), width=200, height=40)
    mots_de_passe_revendeur.pack(pady=2)
    num_téléphone_revendeur_label = customtkinter.CTkLabel(
        tabview.tab("Se connecter en tant que \n revendeur"), text="Numéro de téléphone")
    num_téléphone_revendeur_label.pack(pady=2)
    num_téléphone_revendeur = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n revendeur"), width=200, height=40)
    num_téléphone_revendeur.pack(pady=2)
    nom_boutique_revendeur_label = customtkinter.CTkLabel(
        tabview.tab("Se connecter en tant que \n revendeur"), text="Nom de la boutique")
    nom_boutique_revendeur_label.pack(pady=2)
    nom_boutique_revendeur = customtkinter.CTkEntry(tabview.tab(
        "Se connecter en tant que \n revendeur"), width=200, height=40)
    nom_boutique_revendeur.pack(pady=2)
    textbox_label = customtkinter.CTkLabel(tabview.tab(
        "Se connecter en tant que \n revendeur"), text="Veuillez d'écrire votre boutique")
    textbox_label.pack(pady=2)
    textbox = customtkinter.CTkTextbox(tabview.tab(
        "Se connecter en tant que \n revendeur"), height=100)
    textbox.pack(pady=2)

    def valider_connexion_revendeur():
        nom = nom_revendeur.get().strip()
        prenom = prénom_revendeur.get().strip()
        mot_de_passe = mots_de_passe_revendeur.get().strip()
        numero_telephone = num_téléphone_revendeur.get().strip()
        nom_boutique = nom_boutique_revendeur.get().strip()
        description = textbox.get("1.0", "end-1c").strip()

        if not nom or not prenom or not mot_de_passe or not numero_telephone or not nom_boutique or not description:
            messagebox.showwarning(
                "Erreur", "veuillez remplir tous les champs")
            return
        session = session_factory()
        try:
            session.execute(
                text("""
                        INSERT INTO vendeur (nom, prénom, mots_de_passe, num_telephone, boutique)
                        VALUES (:nom, :prenom, :mot_de_passe, :numero_telephone, :nom_boutique)
                    """),
                {
                    "nom": nom,
                    "prenom": prenom,
                    "mot_de_passe": mot_de_passe,
                    "numero_telephone": numero_telephone,
                    "nom_boutique": nom_boutique,
                },
            )
            session.execute(
                text("""
                        INSERT INTO boutique (nom, admin, description)
                        VALUES (:nom_boutique, :admin, :description)
                    """),
                {
                    "nom_boutique": nom_boutique,
                    "admin": nom,
                    "description": description,
                },
            )
            session.commit()
            messagebox.showinfo(
                "compte créé", "Compte créé")

            return True
        except Exception as e:
            session.rollback()
            messagebox.showerror(
                "erreur", f"impossible d'ajouter le compte : {e}")
            return False
        finally:
            session.close()

    def espace_revendeur():
        fenetre_connexion.update_idletasks()
        largeur = fenetre_connexion.winfo_width()
        hauteur = fenetre_connexion.winfo_height()
        x = fenetre_connexion.winfo_x()
        y = fenetre_connexion.winfo_y()
        fenetre_connexion.withdraw()
        espace_revendeur = tk.Toplevel(fenetre)
        espace_revendeur.title("Espace revendeur")
        espace_revendeur.geometry(f"{largeur}x{hauteur}+{x}+{y}")
        espace_revendeur.configure(bg="#576238")

        def gestion_boutique():
            espace_revendeur.update_idletasks()
            largeur = espace_revendeur.winfo_width()
            hauteur = espace_revendeur.winfo_height()
            x = espace_revendeur.winfo_x()
            y = espace_revendeur.winfo_y()
            espace_revendeur.withdraw()
            gestion_boutique = tk.Toplevel(fenetre)
            gestion_boutique.title("Espace revendeur")
            gestion_boutique.geometry(f"{largeur}x{hauteur}+{x}+{y}")
            gestion_boutique.configure(bg="#576238")

            def ajouter_annonce():
                gestion_boutique.update_idletasks()
                largeur = gestion_boutique.winfo_width()
                hauteur = gestion_boutique.winfo_height()
                x = gestion_boutique.winfo_x()
                y = gestion_boutique.winfo_y()
                gestion_boutique.withdraw()
                fenetre_produit = tk.Toplevel(fenetre)
                fenetre_produit.title("Ajouter un produit")
                fenetre_produit.geometry(f"{largeur}x{hauteur}+{x}+{y}")
                fenetre_produit.configure(bg="#576238")

                def revenir():
                    fenetre_produit.update_idletasks()
                    largeur = fenetre_produit.winfo_width()
                    hauteur = fenetre_produit.winfo_height()
                    x = fenetre_produit.winfo_x()
                    y = fenetre_produit.winfo_y()
                    gestion_boutique.geometry(f"{largeur}x{hauteur}+{x}+{y}")
                    gestion_boutique.deiconify()
                    fenetre_produit.destroy()

                formulaire_produit = ctk.CTkFrame(fenetre_produit)
                formulaire_produit.pack(fill="y", expand=False)
                nom_produit_label = customtkinter.CTkLabel(
                    formulaire_produit, text="Nom du produit")
                nom_produit_label.pack(pady=2)
                nom_produit = customtkinter.CTkEntry(
                    formulaire_produit, width=200, height=40, corner_radius=20)
                nom_produit.pack(pady=2)
                qte_produit_label = customtkinter.CTkLabel(
                    formulaire_produit, text="Quantité en stock")
                qte_produit_label.pack(pady=2)
                qte_produit = customtkinter.CTkEntry(
                    formulaire_produit, width=200, height=40, corner_radius=20)
                qte_produit.pack(pady=2)
                prix_produit_label = customtkinter.CTkLabel(
                    formulaire_produit, text="Prix (FCFA)")
                prix_produit_label.pack(pady=2)
                prix_produit = customtkinter.CTkEntry(
                    formulaire_produit, width=200, height=40, corner_radius=20)
                prix_produit.pack(pady=2)
                date_produit_label = customtkinter.CTkLabel(
                    formulaire_produit, text="Date d'expiration (JJ/MM/AAAA)")
                date_produit_label.pack(pady=2)
                date_produit = customtkinter.CTkEntry(
                    formulaire_produit, width=200, height=40, corner_radius=20)
                date_produit.pack(pady=2)
                description_produit_label = customtkinter.CTkLabel(
                    formulaire_produit, text="Description")
                description_produit_label.pack(pady=2)
                description_produit = customtkinter.CTkTextbox(
                    formulaire_produit, height=80, width=200)
                description_produit.pack(pady=2)

                ajouter_image_label = tk.StringVar(value="")
                apercu_image = customtkinter.CTkLabel(
                    formulaire_produit, text="Aucune image sélectionnée")
                apercu_image.pack(pady=5)

                def choisir_image():
                    chemin = filedialog.askopenfilename(
                        title="Choisir une image",
                        filetypes=[
                            ("Images", "*.png *.jpg *.jpeg *.gif"),
                            ("Tous les fichiers", "*.*"),
                        ],
                    )
                    if not chemin:
                        return
                    try:
                        image = customtkinter.CTkImage(
                            light_image=Image.open(chemin), size=(180, 120),)
                    except Exception as erreur:
                        messagebox.showerror(
                            "Image invalide", f"Impossible d'ouvrir cette image : {erreur}")
                        return
                    ajouter_image_label.set(chemin)
                    apercu_image.configure(image=image, text="")
                    apercu_image.image = image
                ajouter_image = customtkinter.CTkButton(
                    formulaire_produit, text="Choisir une image", command=choisir_image,)
                ajouter_image.pack(pady=5)

                def combobox_callback(choice):
                    print("combobox dropdown clicked:", choice)
                combobox_var = customtkinter.StringVar(value="Electronique")
                combobox = customtkinter.CTkComboBox(formulaire_produit, values=["Véhicules", "Electronique", "Mode & Beauté", "Immobilier", "Electroménager",
                                                     "Pour la maison", "Sports & loisirs", "Services & Emplois"], command=combobox_callback, variable=combobox_var, width=200, height=40, corner_radius=20)
                combobox.pack(pady=2)

                def ajouter_produit():
                    photo = ajouter_image.get()
                    nom = nom_produit.get().strip()
                    quantite = qte_produit.get().strip()
                    prix = prix_produit.get().strip()
                    date = date_produit.get().strip()
                    description = description_produit.get(
                        "1.0", "end-1c").strip()
                    boutique = nom_boutique_revendeur.get().strip()

                    if not nom or not quantite or not prix or not photo or not date or not description:
                        messagebox.showwarning(
                            "Erreur", "Veuillez renseignez toutes les information du produit")
                        return
                    session = session_factory()
                    try:
                        session.execute(
                            text("""
                                INSERT INTO produit (photo ,nom, stock, prix, date_peremption, description, boutique)
                                VALUES (:photo ,:nom, :stock, :prix, :date_peremption, :description, :boutique)
                            """),
                            {
                                "photo": photo,
                                "nom": nom,
                                "stock": quantite,
                                "prix": prix,
                                "date_peremption": date,
                                "description": description,
                                "boutique": boutique,
                            },
                        )
                        session.commit()
                        messagebox.showinfo(
                            "Produit ajouté", f"{nom} a été ajouté à la boutique")
                        revenir()
                    except Exception as e:
                        session.rollback()
                        messagebox.showerror(
                            "Erreur", f"Impossible d'ajouter le produit  {e}")
                    finally:
                        session.close()

                button = customtkinter.CTkButton(
                    formulaire_produit, text="Ajouter le produit", command=two_funcs(ajouter_produit, revenir))
                button.pack(side="right", padx=20, pady=20)
                button.configure(width=200, height=60,
                                 fg_color="#2872a1", corner_radius=10)
                button = customtkinter.CTkButton(
                    formulaire_produit, text="Annuler", command=revenir)
                button.pack(side="left", padx=20, pady=20)
                button.configure(width=200, height=60,
                                 fg_color="#fb3640", corner_radius=10)

            def retour_accueil():
                gestion_boutique.destroy()
                espace_revendeur.deiconify()

            header = tk.Frame(gestion_boutique, bg="#576238", height=100)
            header.pack(fill="x")
            header.grid_columnconfigure(1, weight=1)
            label = customtkinter.CTkLabel(
                header, text="BIENVENUE \n SUR MON SITE", anchor="w", font=("Times new roman", 50, "bold"), text_color="#f0eadc", width=100, height=20)
            label.grid(row=0, column=0, padx=10, pady=2, sticky="w")
            icone_profile = customtkinter.CTkImage(
                light_image=Image.open(
                    Path(__file__).with_name("acceuil.png")),
                size=(25, 25),
            )
            button2 = customtkinter.CTkButton(
                header, text="Accueil", image=icone_profile, compound="left", command=retour_accueil, border_color="#576238", fg_color="#f0eadc", text_color="#576238")
            button2.grid(row=0, column=1, padx=10, pady=2, sticky="e")
            button2.configure(width=150, height=60, corner_radius=30)
            button3 = customtkinter.CTkButton(
                header, text="Ajouter une annonce", image=icone_profile, compound="left", command=ajouter_annonce, border_color="#576238", fg_color="#f0eadc", text_color="#576238")
            button3.grid(row=0, column=2, padx=10, pady=2, sticky="e")
            button3.configure(width=150, height=60, corner_radius=30)

        header = tk.Frame(espace_revendeur, bg="#576238", height=100)
        header.pack(fill="x")
        header.grid_columnconfigure(1, weight=1)
        label = customtkinter.CTkLabel(
            header, text="BIENVENUE \n SUR MON SITE", anchor="w", font=("Times new roman", 50, "bold"), text_color="#f0eadc", width=100, height=20)
        label.grid(row=0, column=0, padx=10, pady=2, sticky="w")
        icone_profile = customtkinter.CTkImage(
            light_image=Image.open(
                Path(__file__).with_name("street-market.png")),
            size=(25, 25),
        )
        button2 = customtkinter.CTkButton(
            header, text="Gérer ma boutique", image=icone_profile, compound="left", command=gestion_boutique, border_color="#576238", fg_color="#f0eadc", text_color="#576238")
        button2.grid(row=0, column=2, padx=10, pady=2, sticky="e")
        button2.configure(width=150, height=60, corner_radius=30)

    # BUTTON REVENDEUR
    button = customtkinter.CTkButton(tabview.tab("Se connecter en tant que \n revendeur"),
                                     text="Créer un compte", command=two_funcs(valider_connexion_revendeur, espace_revendeur))
    button.pack(side="right", padx=20, pady=20)
    button.configure(width=200, height=60,
                     fg_color="#2872a1", corner_radius=10)
    button = customtkinter.CTkButton(
        tabview.tab("Se connecter en tant que \n revendeur"), text="Annuler", command=annuler)
    button.pack(side="left", padx=20, pady=20)
    button.configure(width=200, height=60,
                     fg_color="#fb3640", corner_radius=10)

    # COMPTE EXISTANT
    tabview.add("Se connecter à un compte \n déjà existant")
    nom_label = customtkinter.CTkLabel(
        tabview.tab("Se connecter à un compte \n déjà existant"), text="Nom")
    nom_label.pack(pady=2)
    nom_connexion = customtkinter.CTkEntry(tabview.tab(
        "Se connecter à un compte \n déjà existant"), width=200, height=40)
    nom_connexion.pack(pady=2)
    prénom_label = customtkinter.CTkLabel(tabview.tab(
        "Se connecter à un compte \n déjà existant"), text="Prénom")
    prénom_label.pack(pady=2)
    prénom_connexion = customtkinter.CTkEntry(tabview.tab(
        "Se connecter à un compte \n déjà existant"), width=200, height=40)
    prénom_connexion.pack(pady=2)
    mots_de_passe_label = customtkinter.CTkLabel(
        tabview.tab("Se connecter à un compte \n déjà existant"), text="Mots de passe")
    mots_de_passe_label.pack(pady=2)
    mots_de_passe_connexion = customtkinter.CTkEntry(tabview.tab(
        "Se connecter à un compte \n déjà existant"), width=200, height=40)
    mots_de_passe_connexion.pack(pady=2)

    def valider_connexion_existant():
        nom = nom_connexion.get().strip()
        prenom = prénom_connexion.get().strip()
        mots_de_passe = mots_de_passe_connexion.get().strip()

        if not nom or not prenom or not mots_de_passe:
            messagebox.showwarning(
                "Erreur", "veuillez remplir tous les champs")
            return

        session = session_factory()
        try:
            acheteur = session.execute(
                text("""
                    SELECT * FROM acheteur
                    WHERE nom = :nom AND prénom = :prenom AND mots_de_passe = :mots_de_passe
                """),
                {"nom": nom,
                 "prenom": prenom,
                 "mots_de_passe": mots_de_passe},
            ).fetchone()
            if acheteur:
                fenetre_connexion.destroy()
                espace_client()
                return

            vendeur = session.execute(
                text("""
                    SELECT * FROM vendeur
                    WHERE nom = :nom AND prénom = :prenom AND mots_de_passe = :mots_de_passe
                """),
                {"nom": nom,
                 "prenom": prenom,
                 "mots_de_passe": mots_de_passe},
            ).fetchone()
            if vendeur:
                fenetre_connexion.destroy()
                espace_revendeur()
                return

            messagebox.showerror(
                "Erreur", "Information incorrecte")
        except Exception as e:
            messagebox.showerror(
                "Erreur", f"Se compte n'existe pas {e}")
        finally:
            session.close()

    button8 = customtkinter.CTkButton(
        tabview.tab("Se connecter à un compte \n déjà existant"), text="Se connecter", command=valider_connexion_existant)
    button8.pack(side="right", padx=20, pady=20)
    button8.configure(width=200, height=60,
                      fg_color="#2872a1", corner_radius=10)
    button8 = customtkinter.CTkButton(
        tabview.tab("Se connecter à un compte \n déjà existant"), text="Annuler", command=annuler)
    button8.pack(side="left", padx=20, pady=20)
    button8.configure(width=200, height=60,
                      fg_color="#fb3640", corner_radius=10)


fenetre = tk.Tk()
fenetre.title("Site de vente")
fenetre.geometry("800x600")
fenetre.resizable(True, True)


# EN TETE

header = tk.Frame(fenetre, bg="#576238", height=100)
header.pack(fill="x")
header.grid_columnconfigure(1, weight=1)
label = customtkinter.CTkLabel(
    header, text="BIENVENUE \n SUR MON SITE", anchor="w", font=("Times new roman", 50, "bold"), text_color="#f0eadc", width=100, height=20)
label.grid(row=0, column=0, padx=10, pady=2, sticky="w")
barre_recherche = ctk.CTkEntry(
    header, width=900, height=50, corner_radius=40, fg_color="white", border_color="white", placeholder_text="Rechercher", placeholder_text_color="black", font=("Times new roman", 20))
barre_recherche.grid(row=0, column=1, padx=10, pady=2)

icone_profile = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("utilisateur.png")),
    size=(25, 25),
)
button2 = customtkinter.CTkButton(
    header, text="Se connecter", image=icone_profile, compound="left", command=formulaire_connexion, border_color="#576238", fg_color="#f0eadc", text_color="#576238")
button2.grid(row=0, column=2, padx=10, pady=2, sticky="e")
button2.configure(width=150, height=60, corner_radius=30)

body = ctk.CTkFrame(fenetre, fg_color="#576238")
body.pack(fill="both", expand=True)
# onglets
onglets = ctk.CTkTabview(body,
                         fg_color="black", anchor="w", corner_radius=40, segmented_button_fg_color="#f0eadc", segmented_button_unselected_color="#7a8662", text_color="black")
onglets.pack(fill="both", expand=True, padx=20, pady=20)
onglets._segmented_button.configure(
    width=180, height=55, font=("Times New Roman", 20))

# onglets1
onglets.add("Acceuil")
icone_acceuil = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("accueil.png")),
    size=(25, 25),
)
onglets._segmented_button._buttons_dict["Acceuil"].configure(
    image=icone_acceuil, compound="left")

onglets.add("Véhicules")
icone_vehicule = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("voiture-musclee.png")),
    size=(25, 25),
)
onglets._segmented_button._buttons_dict["Véhicules"].configure(
    image=icone_vehicule, compound="left")

onglets.add("Electronique")
icone_electronic = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("moniteur.png")), size=(25, 25))
onglets._segmented_button._buttons_dict["Electronique"].configure(
    image=icone_electronic, compound="left")

onglets.add("Mode & Beauté")
icone_mode = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("mascara.png")), size=(25, 25))
onglets._segmented_button._buttons_dict["Mode & Beauté"].configure(
    image=icone_mode, compound="left")


onglets.add("Immobilier")
icone_immobilier = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("real-estate.png")), size=(25, 25))
onglets._segmented_button._buttons_dict["Immobilier"].configure(
    image=icone_immobilier, compound="left")


onglets.add("Electroménager")
icone_electromenage = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("home-appliance.png")), size=(25, 25))
onglets._segmented_button._buttons_dict["Electroménager"].configure(
    image=icone_electromenage, compound="left")


onglets.add("Pour la maison")
icone_maison = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("chambre-a-coucher.png")), size=(25, 25))
onglets._segmented_button._buttons_dict["Pour la maison"].configure(
    image=icone_maison, compound="left")


onglets.add("Sports & loisirs")
icone_sport = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("des-sports.png")), size=(25, 25))
onglets._segmented_button._buttons_dict["Sports & loisirs"].configure(
    image=icone_sport, compound="left")

onglets.add("Service & Emplois")
icone_electronic = customtkinter.CTkImage(
    light_image=Image.open(Path(__file__).with_name("public-service.png")), size=(25, 25))
onglets._segmented_button._buttons_dict["Service & Emplois"].configure(
    image=icone_electronic, compound="left")

onglets.set("Acceuil")
fenetre.mainloop()
