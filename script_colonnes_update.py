###Ce script pour mettre à jour plusieurs colonnes avec des valeurs différentes ###
import arcpy 
# Chemin vers la table ou la classe d'entités ou de l'environnement de travail
arcpy.env.workspace=r"C:\Users\elitc\OneDrive\Bureau\UN\Docs_Cours\M1\RLA\MAJ\majL\majL.gdb"
t_ligne="t_ligne_15062023_polyline"
l_arligne="l_arret_ligne_15062023_none"
#selection des attributs à mettre à jour
selection_t =arcpy.management.SelectLayerByAttribute("l_arret_ligne_15062023_none", "NEW_SELECTION", "ligne_sens = '22_2_2'", None)

#definition des colonnes et valeur pour la mise à jour
colonne = ["ligne_sens", "date_explo","type_arret"]
nouvelles_valeurs=["22_1_1","2023","Passage"]
with arcpy.da.UpdateCursor(selection_t, colonne) as cursor:
    for row in cursor:
        for i, col in enumerate(colonne):
                row[i] = nouvelles_valeurs[i]
        cursor.updateRow(row)
        
print("les valeurs ont été insérées avec succès! :)")


