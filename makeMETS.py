#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Erzeugung statischer METS-Dateien für Handschriftendigitalisate der HAB

import mets as mets

# Beispiel: Erzeugen einer METS-Datei für das Digitalisat http://diglib.hab.de/mss/ed000371/start.htm:
# Als erster Parameter wird die normierte Signatur (ohne "mss/") übergeben. Der zweite, optionale Parameter enthält einen Titel für das Digitalisat
builder = mets.METSBuilder("ed000371", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225")
builder.build()

# Dasselbe für eine Liste
"""
listDigi = [
    ["ed000371", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000372", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000373", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000374", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000375", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000376", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000244", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA Reg N 621"], 
    ["ed000388", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000389", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000378", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000379", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 224"], 
    ["ed000391", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 225"], 
    ["ed000380", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 224"], 
    ["ed000381", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 224"], 
    ["ed000392", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 224"], 
    ["ed000377", "Stadtbibliothek Bildcampus Nürnberg, Autogr. 239"], 
    ["ed000382", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 475"], 
    ["ed000393", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. O, Nr. 475"], 
    ["ed000399", "Landesarchiv Sachsen-Anhalt, A 2, Nr. 499"], 
    ["ed000395", "Ratsschulbibliothek Zwickau, Ms. KKKK.1"], 
    ["ed000245", "Staatsbibliothek zu Berlin - Preußischer Kulturbesitz, Ms. theol. lat. oct. 40"], 
    ["ed000396", "Ratsschulbibliothek Zwickau, Ms.34"], 
    ["ed000383", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. N, Nr. 624"], 
    ["ed000394", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. N, Nr. 624"], 
    ["ed000385", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. N, Nr. 624"], 
    ["ed000384", "Landesarchiv Sachsen-Anhalt, A2, Nr. 499"], 
    ["ed000398", "Landesarchiv Sachsen-Anhalt, A2, Nr. 499"], 
    ["ed000386", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. N, Nr. 624"], 
    ["ed000387", "Landesarchiv Thüringen - Hauptstaatsarchiv Weimar, EGA, Reg. N, Nr. 624"], 
    ["ed000397", "Ratsschulbibliothek Zwickau, Ms.35"], 
    ["ed000407", "Ratsschulbibliothek Zwickau, N 136"]]

for digi in listDigi:
    builder = mets.METSBuilder(digi[0], digi[1])
    builder.build()
"""