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
                row['price'] = int(float(row['price']) * 100)
                row['profit'] = (float(row['profit']) / 100)
        return csv_content
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return None


csv_file_name = "dataset2_Python+P7.csv"
list_actions = open_csv_file(csv_file_name)
print(list_actions)
print(len(list_actions))

list_actions_clean = [action for action in list_actions if action['price'] > 0]



print(list_actions_clean)
print(len(list_actions_clean))

# Convertir list_actions en un dictionnaire pour accéder aux informations par le nom de l'action
actions_dict = {action['name'].strip(): {'cout': action['price'], 'benefice': action['profit'] * action['price']} for
                action in
                list_actions_clean}
print(actions_dict)
print(len(actions_dict))

budget_max = 500
budget_max_centime = budget_max * 100


def meilleur_combinaison(actions, budget_max):
    matrice = [[0 for x in range(budget_max + 1)] for x in range(len(actions) + 1)]

    num_rows = len(matrice)
    num_columns = len(matrice[0])  # Assuming all rows have the same number of columns

    # Print the size of the matrix
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_columns}")

    for i in range(1, len(actions) + 1):
        cout_action = actions[list(actions.keys())[i - 1]]["cout"]
        benefice_action = actions[list(actions.keys())[i - 1]]["benefice"]
        for j in range(budget_max + 1):
            if cout_action <= j:
                matrice[i][j] = max(benefice_action + matrice[i - 1][j - cout_action], matrice[i - 1][j])
            else:
                matrice[i][j] = matrice[i - 1][j]
    # retouver les actions
    combinaison_optimale = []
    i, j = len(actions), budget_max

    while i > 0 and j > 0:
        if matrice[i][j] == matrice[i - 1][j - actions[list(actions.keys())[i - 1]]["cout"]] + \
                actions[list(actions.keys())[i - 1]]["benefice"]:
            combinaison_optimale.append(list(actions.keys())[i - 1])
            j -= actions[list(actions.keys())[i - 1]]["cout"]
        i -= 1
    # while i > 0 and j > 0:
    #     if matrice[i][j] != matrice[i - 1][j]:
    #         combinaison_optimale.append(list(actions.keys())[i - 1])
    #         j -= actions[list(actions.keys())[i - 1]]["cout"]
    #     i -= 1

    return combinaison_optimale


def calculer_cout_benefice(combinaison, actions):
    cout_total = sum(actions[action]["cout"] for action in combinaison) / 100
    benefice_total = sum(actions[action]["benefice"]/100 for action in combinaison)
    return cout_total, benefice_total


print(len(actions_dict))
resultat = meilleur_combinaison(actions_dict, budget_max_centime)
cout_total, benefice_total = calculer_cout_benefice(resultat, actions_dict)

print("Meilleure combinaison d'actions :", resultat)
for action_name in resultat:
    print(action_name,actions_dict[action_name]['cout'],actions_dict[action_name]['benefice'])
print("Coût total :", cout_total, "euros")
print("Bénéfice total :", benefice_total, "euros")

print(len(resultat))
