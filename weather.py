import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Lire le fichier Excel et charger la feuille "avec" dans un DataFrame
chemin_fichier = 'valerie.xlsx'
nom_feuille = 'avec'
df = pd.read_excel(chemin_fichier, sheet_name=nom_feuille)

# Convertir la colonne 'Date' au format datetime
df['Date'] = pd.to_datetime(df['Date'])

# Tracé
plt.figure(figsize=(12, 6))

# Tracé de la température
plt.subplot(2, 1, 1)
plt.plot(df['Date'], df['Température'], marker='o', linestyle='-', color='b')
plt.title('Température au fil du temps')
plt.xlabel('Date et Heure')
plt.ylabel('Température (°C)')
plt.grid(True)

# Tracé de l'humidité
plt.subplot(2, 1, 2)
plt.plot(df['Date'], df['Humidité'], marker='o', linestyle='-', color='r')
plt.title('Humidité au fil du temps')
plt.xlabel('Date et Heure')
plt.ylabel('Humidité (%)')
plt.grid(True)

# Ajuster la mise en page pour éviter les chevauchements
plt.tight_layout()

# Afficher le graphique
plt.show()
