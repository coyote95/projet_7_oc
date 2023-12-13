actions = {
    "Action-1": {"cout": 20, "benefice": 0.05},
    "Action-2": {"cout": 30, "benefice": 0.10},
    "Action-3": {"cout": 50, "benefice": 0.15},
    "Action-4": {"cout": 70, "benefice": 0.20},
    "Action-5": {"cout": 60, "benefice": 0.17},
    "Action-6": {"cout": 80, "benefice": 0.25},
    "Action-7": {"cout": 22, "benefice": 0.07},
    "Action-8": {"cout": 26, "benefice": 0.11},
    "Action-9": {"cout": 48, "benefice": 0.13},
    "Action-10": {"cout": 34, "benefice": 0.27},
    "Action-11": {"cout": 42, "benefice": 0.17},
    "Action-12": {"cout": 110, "benefice": 0.09},
    "Action-13": {"cout": 38, "benefice": 0.23},
    "Action-14": {"cout": 14, "benefice": 0.01},
    "Action-15": {"cout": 18, "benefice": 0.03},
    "Action-16": {"cout": 8, "benefice": 0.08},
    "Action-17": {"cout": 4, "benefice": 0.12},
    "Action-18": {"cout": 10, "benefice": 0.14},
    "Action-19": {"cout": 24, "benefice": 0.21},
    "Action-20": {"cout": 114, "benefice": 0.18},
}


# Solution optimale - programmation dynamique
def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):
            if elements[i - 1][1] <= w:
                matrice[i][w] = max(elements[i - 1][2] + matrice[i - 1][w - elements[i - 1][1]], matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n - 1]
        if matrice[n][w] == matrice[n - 1][w - e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], elements_selection


# Convert the 'actions' dictionary to a list of tuples
action_list = [(key, value["cout"], value["benefice"]*value["cout"]) for key, value in actions.items()]

print('Algo dynamique', sacADos_dynamique(500, action_list))
