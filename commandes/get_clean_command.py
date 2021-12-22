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

    return min_command
