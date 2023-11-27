#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import os
import json
from recettes import *

# TODO: Définissez vos fonction ici
def file_comp(file1, file2):
    with open(file1, "r") as f:
        file_1 = f.readlines()
    with open(file2, "r") as f0:
        file_2 = f0.readlines()

    for i in range(len(file_1)):
        if len(file_1) != len(file_2):
            return f"Les fichiers {file1} et {file2} ne sont pas identiques"
        elif file_1[i] != file_2[i]:
                return f"Les fichiers {file1} et {file2} ne sont pas identiques"  
    return f"Les fichiers {file1} et {file2} sont identiques"


def copy_file_3x_space(file1, file3):
    with open(file1, "r") as f, open(file3, "w") as f1:
        for line in f.readlines():
            for letter in line:
                if letter == " ":
                    f1.write(letter*3)
                else:
                    f1.write(letter)
    return f"The file {file1} was copied with 3 spaces between words"


def note_jsn(fil4, file5, file6):
    with open(fil4, "r") as f0:
        seuils = json.load(f0)

    with open(file5, "r") as f:
        dictNote = {}
        for note in f.readlines():
            if int(note[0:3]) in range(seuils["A*"][0],seuils["A*"][1]):
                dictNote[int(note[0:3])] = "A*"
            elif int(note[0:3]) in range(seuils["A"][0],seuils["A"][1]):
                dictNote[int(note[0:3])] = "A"
            elif int(note[0:3]) in range(seuils["B+"][0],seuils["B+"][1]):
                dictNote[int(note[0:3])] = "B+"
            elif int(note[0:3]) in range(seuils["B"][0],seuils["B"][1]):
                dictNote[int(note[0:3])] = "B"
            elif int(note[0:3]) in range(seuils["C+"][0],seuils["C+"][1]):
                dictNote[int(note[0:3])] = "C+"
            elif int(note[0:3]) in range(seuils["C"][0],seuils["C"][1]):
                dictNote[int(note[0:3])] = "C"
            elif int(note[0:3]) in range(seuils["F"][0],seuils["F"][1]):
                dictNote[int(note[0:3])] = "F"
    
    with open(file6, "w") as f1:
        json.dump(dictNote, f1, indent=4)

    return f"Les note du fichier {file5} ont ete convertiess en dictionnaire dans le fichier {file6}"

def data_recettes():
    pass
    

            








    
        


if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")
    file1 = "./data/exemple.txt"
    file2 = "./data/exemple2.txt"
    file3 = "./data/plus.txt"
    file4 = "./data/seuils.json"
    file5 = "./data/notes.txt"
    file6 = "./data/notes_dict.json"
    #print(file_comp(file1, file2))
    #print(copy_file_3x_space(file1, file3))
    print(note_jsn(file4, file5, file6))

    # TODO: Appelez vos fonctions ici, mettez vos fichiers de sortie dans le dossier "output".

