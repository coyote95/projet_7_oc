import csv
import time

start = time.time()


def open_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            csv_content = list(csv_reader)
            csv_content = [{key.strip('\ufeff'): value.strip() for key, value in row.items()} for row in csv_content]
            for row in csv_content:
                row['cout'] = int(row['cout'])
                row['benefice'] = float(row['benefice'].rstrip('%')) / 100
        return csv_content
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return None


csv_file_name = "actions.csv"
list_actions = open_csv_file(csv_file_name)
print(list_actions)

target_cost = 500

# Convertir list_actions en un dictionnaire pour accéder aux informations par le nom de l'action
actions_dict = {action['actions']: {'cout': action['cout'], 'benefice': action['benefice']} for action in list_actions}
print (actions_dict)

budget_max = 500


def meilleur_combinaison(actions, budget_max):
    matrice = [[0] * (budget_max + 1) for _ in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for j in range(budget_max + 1):
            cout_action = actions[list(actions.keys())[i - 1]]["cout"]
            benefice_action = actions[list(actions.keys())[i - 1]]["benefice"]
            if cout_action <= j:
                matrice[i][j] = max(matrice[i - 1][j], matrice[i - 1][j - cout_action] + cout_action * benefice_action)
            else:
                matrice[i][j] = matrice[i - 1][j]
    #retouver les actions
    combinaison_optimale = []
    i, j = len(actions), budget_max
    while i > 0 and j > 0:
        if matrice[i][j] != matrice[i - 1][j]:
            combinaison_optimale.append(list(actions.keys())[i - 1])
            j -= actions[list(actions.keys())[i - 1]]["cout"]
        i -= 1

    return combinaison_optimale


def calculer_cout_benefice(combinaison, actions):
    cout_total = sum(actions[action]["cout"] for action in combinaison)
    benefice_total = sum(actions[action]["cout"] * actions[action]["benefice"] for action in combinaison)
    return cout_total, benefice_total


resultat = meilleur_combinaison(actions_dict, budget_max)
cout_total, benefice_total = calculer_cout_benefice(resultat, actions_dict)

print("Meilleure combinaison d'actions :", resultat)
print("Coût total :", cout_total, "euros")
print("Bénéfice total :", benefice_total, "euros")


