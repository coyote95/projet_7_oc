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


all_combinaisons = []
all_combinaison_limit_profit = []
plafond = 500

csv_file_name = "actions.csv"
list_actions = open_csv_file(csv_file_name)
print(list_actions)

# Convertir list_actions en un dictionnaire pour accéder aux informations par le nom de l'action
actions_dict = {action['actions']: {'cout': action['cout'], 'profit': action['cout'] * action['benefice']} for action
                in
                list_actions}

for action in actions_dict:
    print(f"action:{actions_dict[action]['cout']}, {actions_dict[action]['profit']}")


def glouton(capacite, elements):
    elements_tri = sorted(elements.items(), key=lambda x: x[1]['profit'], reverse=False)
    elements_selection = []
    prix_total = 0
    profit_total = 0

    while elements_tri:
        action, info = elements_tri.pop()
        if info['cout'] + prix_total <= capacite:
            elements_selection.append(action)
            prix_total += info['cout']
            profit_total += info['profit']
    return prix_total,profit_total, elements_selection


print('Algo glouton', glouton(500, actions_dict))
