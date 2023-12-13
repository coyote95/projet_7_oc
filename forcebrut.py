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


def generate_combinations(base_combination, remaining_actions, max_depth, result, limite):
    if len(base_combination) == max_depth:
        somme = somme_combination(limite, base_combination)
        if somme is not None:
            result.append(somme)
        return
    for action in remaining_actions:
        if len(base_combination) > 0 and action['actions'] <= base_combination[-1]['actions']:
            continue
        # new_remaining_actions = [a for a in remaining_actions if a != action]
        # print(new_remaining_actions)
        generate_combinations(base_combination + [action], remaining_actions, max_depth, result, plafond)


def somme_combination(limite, combination):
    total_cout = sum([action['cout'] for action in combination])
    if total_cout < limite:
        total_benefice = sum([(action['benefice'] * action['cout']) for action in combination])
        dict_somme_combination = {'actions': [action['actions'] for action in combination],
                                  'total_cout': total_cout, 'total_benefice': total_benefice}
        return dict_somme_combination
    else:
        return None


all_combinaisons = []
all_combinaison_limit_profit = []
plafond = 500

csv_file_name = "actions.csv"
list_dict_actions = open_csv_file(csv_file_name)
print(list_dict_actions) #[{'actions': 'action-1', 'cout': 20, 'benefice': 0.05},...]


for i in range(1, len(list_dict_actions) + 1):
    print(f"depth={i}")
    generate_combinations([], list_dict_actions, i, all_combinaisons, plafond)


all_combinaisons.sort(key=lambda x: x['total_benefice'], reverse=True)
best_combination = all_combinaisons[0]


print(f"\nla meilleur combinaison est: {best_combination['actions']}")
print(f"Total cout: {best_combination['total_cout']} euros")
print(f"Total benefice: {best_combination['total_benefice']}")

end = time.time()
elapsed = end - start

print(f"\nTemps d'exécution : {elapsed:.2f}s")
