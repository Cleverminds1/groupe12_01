#Énoncé : Écrire un programme qui lit une distance (en km) et un temps (en heures), puis calcule la vitesse moyenne (km/h) et la vitesse en m/s.
distance_km = float(input("Distance (km) : "))
temps_h = float(input("Temps (heures) : "))

vitesse_kmh = distance_km / temps_h
vitesse_ms = (distance_km * 1000) / (temps_h * 3600)

print(f"Vitesse moyenne : {vitesse_kmh:.2f} km/h")
print(f"Vitesse moyenne : {vitesse_ms:.2f} m/s")