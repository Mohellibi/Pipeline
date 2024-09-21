import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='Ecole',
    user='root',
    password='!4$b7WsJwM5&eznjCS#C'
)


def affiche_select(rows):
    for row in rows:
        print(row)



def select_table(name_table):

    cursor = conn.cursor()
    cursor.execute(f" SELECT * FROM {name_table}")

    rows = cursor.fetchall()
   
    cursor.close()

    return rows

#affiche_select(select_table('enseignants'))
"""
résultat:
(1, 'jonas', 'salk', None, 'biologie', None, 'jsalk@school.org', '777-555-4321', '5')
(2, 'sophie', 'dubois', None, 'mathématiques', None, 'sophie.dubois@school.org', '777-555-1111', '1')
(3, 'paul', 'martin', None, 'physique', None, 'paul.martin@school.org', '777-555-2222', '2')
(4, 'lucie', 'bernard', None, 'chimie', None, 'lucie.bernard@school.org', '777-555-3333', '3')
(5, 'antoine', 'roux', None, 'histoire', None, 'antoine.roux@school.org', '777-555-4444', '4')
"""





def eleves_enseignants():
    eleves = select_table('élèves')
    enseignants = select_table('enseignants')
    enseignants_par_classe = {}
    
    for teacher in enseignants:
        numero_classe = teacher[8]
        if numero_classe not in enseignants_par_classe:
            enseignants_par_classe[numero_classe] = []
        enseignants_par_classe[numero_classe].append(teacher)

    eleves_enseignants = []
    for eleve in eleves:
        numero_classe = eleve[7]
        if numero_classe in enseignants_par_classe:
            enseignants_associes = enseignants_par_classe[numero_classe]
            for enseignant in enseignants_associes:
                eleves_enseignants.append((eleve[:3], enseignant[:3]))

    return eleves_enseignants

#affiche_select(eleves_enseignants())
"""
résultat
((1, 'mark', 'watney'), (1, 'jonas', 'salk'))
((2, 'alice', 'durand'), (2, 'sophie', 'dubois'))
((3, 'benjamin', 'moreau'), (2, 'sophie', 'dubois'))
((4, 'camille', 'giraud'), (2, 'sophie', 'dubois'))
((5, 'david', 'leclerc'), (2, 'sophie', 'dubois'))
((6, 'emma', 'lafont'), (2, 'sophie', 'dubois'))
((7, 'florian', 'muller'), (2, 'sophie', 'dubois'))
((8, 'garance', 'perez'), (2, 'sophie', 'dubois'))
((9, 'hugo', 'fontaine'), (3, 'paul', 'martin'))
((10, 'ines', 'chevalier'), (3, 'paul', 'martin'))
((11, 'jules', 'noel'), (3, 'paul', 'martin'))
((12, 'laura', 'morris'), (3, 'paul', 'martin'))
((13, 'mathis', 'robin'), (3, 'paul', 'martin'))
((14, 'karl', 'boucher'), (4, 'lucie', 'bernard'))
((15, 'lola', 'ricard'), (4, 'lucie', 'bernard'))
((16, 'maxime', 'vasseur'), (4, 'lucie', 'bernard'))
((17, 'nina', 'francois'), (5, 'antoine', 'roux'))
((18, 'olivier', 'garnier'), (5, 'antoine', 'roux'))
((19, 'pauline', 'delacroix'), (5, 'antoine', 'roux'))
((20, 'quentin', 'marcel'), (5, 'antoine', 'roux'))
((21, 'rose', 'simon'), (5, 'antoine', 'roux'))
((22, 'simon', 'leroy'), (5, 'antoine', 'roux'))
((23, 'tania', 'guillot'), (5, 'antoine', 'roux'))
((24, 'victor', 'blais'), (5, 'antoine', 'roux'))
((25, 'wendy', 'valentin'), (5, 'antoine', 'roux'))
((26, 'xavier', 'richard'), (5, 'antoine', 'roux'))
((27, 'yasmine', 'clement'), (1, 'jonas', 'salk'))
((28, 'zacharie', 'fortier'), (1, 'jonas', 'salk'))
((29, 'amandine', 'barre'), (1, 'jonas', 'salk'))
((30, 'benoit', 'blanchard'), (1, 'jonas', 'salk'))
((32, 'dorian', 'couture'), (1, 'jonas', 'salk'))
((33, 'emilie', 'gagne'), (1, 'jonas', 'salk'))
((34, 'fabien', 'caron'), (1, 'jonas', 'salk'))
"""

def comptage_eleves_par_enseignant(dict_eleves_enseignants):
    enseignants = select_table('enseignants')
    #la je rentre tout les prof dans le dictionnaire car c'est dure de verifier avec un in vue que cest pas des clés
    compte = {enseignant[:3]:0 for enseignant in enseignants} 
    for eleve,enseignant in dict_eleves_enseignants:
        compte[enseignant] +=1
    return compte


#print(comptage_eleves_par_enseignant(eleves_enseignants()))
""" resultat : {(1, 'jonas', 'salk'): 8, (2, 'sophie', 'dubois'): 7, (3, 'paul', 'martin'): 5, (4, 'lucie', 'bernard'): 3,
                 (5, 'antoine', 'roux'): 10}"""
conn.close()


