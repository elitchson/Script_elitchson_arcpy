###Ce script sert à selection des doublons dans une colonne et les remplacer par d'autres valeurs###
import arcpy 
# Chemin vers la table ou la classe d'entités ou de l'environnement de travail
arcpy.env.workspace=r"C:\Users\elitc\OneDrive\Bureau\UN\Docs_Cours\M1\RLA\MAJ\majL\majL.gdb"
t_ligne="t_ligne_15062023_polyline"
l_arligne="l_arret_ligne_15062023_none"

# Nom de la colonne contenant les doublons
colonne_doublons = "idl_arrete"
# Trouver la valeur maximale dans la colonne "idl_arrete"
max_value = None
with arcpy.da.SearchCursor(l_arligne, [colonne_doublons]) as cursor:
    for row in cursor:
        value = row[0]
        if max_value is None or value > max_value:
            max_value = int(value)

# Dictionnaire pour suivre les occurrences des valeurs dans la colonne
occurrences = {}

# Liste pour stocker les doublons trouvés
doublons = []

# Parcourir les lignes de la table pour trouver les doublons
with arcpy.da.SearchCursor(l_arligne, [colonne_doublons]) as cursor:
    for row in cursor:
        value = row[0]
        if value in occurrences:
            doublons.append(value)
        else:
            occurrences[value] = 1

# Créer une requête de sélection pour les doublons
requete_selection = f"{colonne_doublons} IN {tuple(doublons)}"

# Sélectionner les doublons
selection_d=arcpy.management.SelectLayerByAttribute(l_arligne, "NEW_SELECTION", requete_selection)

# Vérifier le nombre de doublons sélectionnés
nombre_doublons_selectionnes = int(arcpy.GetCount_management(l_arligne)[0])
# Générer la liste des nouvelles valeurs idl_arrete
idl_valeurs=list(range(max_value,int(nombre_doublons_selectionnes+max_value))) 
# Mettre à jour la colonne "idl_arrete" avec les nouvelles valeurs
with arcpy.da.UpdateCursor(selection_d, colonne_doublons) as cursor:
    for row in cursor:
        new_value=idl_valeurs.pop(0)
        row[0] = new_value
        cursor.updateRow(row)
print("Doublons remplacés :)")


