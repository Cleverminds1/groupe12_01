"""
Énoncé :
Demander le rôle (employé, visiteur, sécurité).
Si employé → demander badge valide (oui/non) → accès.
Si visiteur → demander s’il a rendez-vous → accès si oui.
Si sécurité → accès direct.
Sinon → refuser.
"""
role = input("Rôle (employé/visiteur/sécurité) : ").lower()

if role == "employé":
    badge = input("Badge valide ? (oui/non) : ").lower()
    if badge == "oui":
        print("Accès autorisé.")
    else:
        print("Accès refusé, badge invalide.")
elif role == "visiteur":
    rdv = input("Avez-vous un rendez-vous ? (oui/non) : ").lower()
    if rdv == "oui":
        print("Accès autorisé.")
    else:
        print("Accès refusé, pas de rendez-vous.")
elif role == "sécurité":
    print("Accès autorisé.")
else:
    print("Accès refusé, rôle inconnu.")
