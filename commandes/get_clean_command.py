# python 3.10
# UTF-8
def give_good_command(command):
    """
    Fonction qui enlève tout les accents et les majuscules
    :param command: String représentant une commande entrée
    :return: String contenant command sans accents et majuscules
    """
    dico_changment = {
        'à': 'a',
        'â': 'a',
        'ä': 'a',
        'é': 'e',
        'è': 'e',
        'ë': 'e',
        'ê': 'e',
        'ç': 'c',
        'ï': 'i',
        'î': 'i',
        'ô': 'o',
        'ö': 'o',
        'ü': 'u',
        'û': 'u',
        'ÿ': 'y'
    }

    min_command = str(command).lower()
    for i in min_command:
        for j in dico_changment.keys():
            if i == j:
                min_command = min_command.replace(i, dico_changment[j])
    """
    index = 0
    for i in min_command:
        if i == 'é' or i == 'è' or i == 'ë' or i == 'ê':
            min_command = min_command.replace(i, 'e')
        elif i == 'à' or i == 'â' or i == 'ä':
            min_command = min_command.replace(i, 'a')
        elif i == 'ç':
            min_command = min_command.replace(i, 'c')
        elif i == 'ï' or i == 'î':
            min_command = min_command.replace(i, 'i')
        elif i == 'ö' or i == 'ô':
            min_command = min_command.replace(i, 'o')
        elif i == 'ü' or i == 'û':
            min_command = min_command.replace(i, 'u')
        elif i == 'ÿ':
            min_command = min_command.replace(i, 'y')
        index += 1
    """
    return min_command


""" Examples
print(give_good_command("/MétèO"))
print(give_good_command("/éèëêàâäçîïôöûüÿ"))
print(give_good_command("/MétèO"))
"""
