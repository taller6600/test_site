# Demander l# Demander le prix à l'utilisateur et le convertir en nombre décimal (float)
prix = float(input("Entre le prix de l'article (en FCFA) : "))

# Condition : Si le prix est supérieur ou égal à 10 000
if prix >= 10000:
   remise = prix * 0.10  # Calcul de 10% de réduction
   prix_final = prix - remise
   print(f"Réduction de 10% appliquée (-{int(remise)} FCFA) !")
   print(f"Nouveau prix à payer : {int(prix_final)} FCFA")
   else:
   manque = 10000 - prix
   print(f"Pas de réduction. Prix à payer : {int(prix)} FCFA")
   print(f"(Ajoute {int(manque)} FCFA d'achats pour débloquer 10% de réduction !)")
   ")")
