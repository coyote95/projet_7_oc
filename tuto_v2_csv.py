
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
#

# Convert the 'actions'list of dictionary to a list of tuples
actions_tuples = [(action['actions'], action['cout'], action['benefice']* action['cout']) for action in list_actions]
print(actions_tuples)


#

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


print('Algo dynamique', sacADos_dynamique(500, actions_tuples))
