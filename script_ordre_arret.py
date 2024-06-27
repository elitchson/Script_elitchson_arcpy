###Ce script sert à remplir une serie de valeur###
import arcpy 
# Chemin vers la table ou la classe d'entités ou de l'environnement de travail
arcpy.env.workspace=r"C:\Users\elitc\OneDrive\Bureau\UN\Docs_Cours\M1\RLA\MAJ\majL\majL.gdb"
t_ligne="t_ligne_15062023_polyline"
l_arligne="l_arret_ligne_15062023_none"
#selection des attributs à mettre à jour
selection_t =arcpy.management.SelectLayerByAttribute("l_arret_ligne_15062023_none", "NEW_SELECTION", "ligne_sens = '22_1_1'", None)

#initialisation de la liste de valeur répétées
nombre_lignes= int(arcpy.GetCount_management(selection_t)[0])
valeurs=list(range(1,int(nombre_lignes/2)+2))
nombre_valeurs = len(valeurs)
nombre_repetitions = nombre_lignes//nombre_valeurs
valeurs_repetees = valeurs * nombre_repetitions
valeurs_repetees.extend(valeurs[:nombre_valeurs+1])
del valeurs_repetees[0]
del valeurs_repetees[-1]
# Nom de la colonne contenant les doublons
colonne = "ordre_arre"
# Mettre à jour la colonne "ordre_arre" avec les nouvelles valeurs
with arcpy.da.UpdateCursor(selection_t, colonne) as cursor:
    for row in cursor:
        valeur = valeurs_repetees.pop(0)
        row[0] = valeur
        cursor.updateRow(row)
print("les valeurs ont été insérées avec succès! :)")


