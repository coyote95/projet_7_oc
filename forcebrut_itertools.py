from itertools import combinations

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


def somme_combination(limite, combination):
    total_cout = sum([action['cout'] for action in combination])
    if total_cout < limite:
        total_benefice = sum([(action['benefice'] * action['cout']) for action in combination])
        dict_somme_combination = {'actions': [action['actions'] for action in combination],
                                  'total_cout': total_cout, 'total_benefice': total_benefice}
        return dict_somme_combination
    else:
        return None

csv_file_name = "actions.csv"
list_actions = open_csv_file(csv_file_name)
print(list_actions)
target_cost = 500

# Générer toutes les combinaisons possibles d'actions
all_combinations = []
result=[]
for r in range(1, len(list_actions) + 1):
    for combination in combinations(list_actions, r):
        somme = somme_combination(500, combination)
        if somme is not None:
            result.append(somme)

    # all_combinations.extend(combinations(list_actions, r))

# for combination in all_combinations:
#     print(combination)

print(len(all_combinations))


# Filtrer les combinaisons dont la somme du coût est inférieure ou égale à 500
valid_combinations = [comb for comb in all_combinations if sum(action['cout'] for action in comb) <= target_cost]



result.sort(key=lambda x: x['total_benefice'], reverse=True)
best_combination = result[0]


print(f"\nla meilleur combinaison est: {best_combination['actions']}")
print(f"Total cout: {best_combination['total_cout']} euros")
print(f"Total benefice: {best_combination['total_benefice']}")

end = time.time()
elapsed = end - start

print(f"\nTemps d'exécution : {elapsed:.2f}s")
