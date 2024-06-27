###Ce script sert à remplir une colonne alternativement avec les valeurs "départ" et "arrivée"###
import arcpy 
# Chemin vers la table ou la classe d'entités ou de l'environnement de travail
arcpy.env.workspace=r"C:\Users\elitc\OneDrive\Bureau\UN\Docs_Cours\M1\RLA\MAJ\majL\majL.gdb"
t_ligne="t_ligne_15062023_polyline"
l_arligne="l_arret_ligne_15062023_none"
#selection des attributs à mettre à jour
selection_t =arcpy.management.SelectLayerByAttribute("l_arret_ligne_15062023_none", "NEW_SELECTION", "ligne_sens = '22_1_1'", None)

colonne = "noeud_tron"
# Ouvrir une mise à jour sur la table ou la classe d'entités
with arcpy.da.UpdateCursor(selection_t, colonne) as cursor:
    # Définir les valeurs "départ" et "arrivée"
    depart = "départ"
    arrivee = "arrivée"
    compteur = 0
    for row in cursor:
        if compteur % 2 == 0:
            row[0] = depart
        else:
            row[0] = arrivee
        cursor.updateRow(row)
        compteur += 1
print("les valeurs ont été insérées avec succès! :)")


