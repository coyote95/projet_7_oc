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


csv_file_name = "actions2.csv"
list_actions = open_csv_file(csv_file_name)
print(list_actions)

target_cost = 500

# Convertir list_actions en un dictionnaire pour accéder aux informations par le nom de l'action
actions_dict = {action['actions']: {'cout': action['cout'], 'benefice': action['benefice']} for action in list_actions}


def generate_combinations(actions, current_combination, remaining_actions, target_cost, result):

    print("***********************************************")
    # print(f"toutes les action:{actions}")
    print(f"current-combinaison:{current_combination}")
    print(f"reste combinaisons:{remaining_actions}")
    print("**********************************************")
    current_cost = sum(actions[action]['cout'] for action in current_combination)

    if current_cost <= target_cost:
        total_benefice = sum([actions[action]['benefice'] * actions[action]['cout'] for action in current_combination])
        dict_somme_combination = {'actions': current_combination, 'total_cout': current_cost,
                                  'total_benefice': total_benefice}
        result.append(dict_somme_combination)
       # print(f"save:{dict_somme_combination}")

    # Condition d'arrêt explicite
    if not remaining_actions:
        return

    for i, action in enumerate(remaining_actions):
        print(f'\nindicei: {i} action: {action} remaining: {remaining_actions}')
        # print("\n**********DEBUT**********")
        print(f"TEST currentcombinaison{current_combination}")
        # print(f'BEFORE-------indice{i} et action:{action}-------')
        # print(f"BEFORE------reste combinaisons:{remaining_actions}")
        generate_combinations(actions, current_combination + [action], remaining_actions[i+1:], target_cost, result)
        # print(f'AFTER-------indice{i} et action:{action}-------')
        # print(f"AFTER------reste combinaisons:{remaining_actions}")
        # print("\n**********FIN**********")


# Générer les combinaisons
all_combinations = []
generate_combinations(actions_dict, [], [action['actions'] for action in list_actions], target_cost, all_combinations)

print(len(all_combinations))
# Afficher les combinaisons valides
# for combination in valid_combinations:
#     print(combination)


all_combinations.sort(key=lambda x: x['total_benefice'], reverse=True)
best_combination = all_combinations[0]

print(f"\nla meilleur combinaison est: {best_combination['actions']}")
print(f"Total cout: {best_combination['total_cout']} euros")
print(f"Total benefice: {best_combination['total_benefice']}")

end = time.time()
print(f"Execution time: {end - start} seconds")
