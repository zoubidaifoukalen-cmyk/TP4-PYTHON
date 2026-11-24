# notes_admission.py - saisie de notes, puis affichage Admis / Refusé
seuil = 10
notes = []

# 1 + 2. Lecture des notes jusqu'à "stop", stockage des valeurs valides
while True:
    entree = input("Entrez une note ou 'stop' : ").strip()
    if entree.lower() == "stop":
        break
    try:
        note = float(entree.replace(",", "."))  # accepte aussi 12,5
        notes.append(note)
    except ValueError:
        print("Valeur incorrecte, merci d'entrer un nombre.")

# 3 + 4. Parcours de la liste avec enumerate et if/else
if not notes:
    print("Aucune note saisie.")
else:
    for index, note in enumerate(notes, start=1):
        if note >= seuil:
            statut = "Admis"
        else:
            statut = "Refusé"
        # Version ternaire équivalente :
        # statut = "Admis" if note >= seuil else "Refusé"
        print(f"Étudiant {index} : note {note} → {statut}")
