import csv


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


def generate_combinations(base_combinaison, remaining_actions, max_depth, result):
    if len(base_combinaison) == max_depth:
        result.append(base_combinaison)
        return
    for action in remaining_actions:
        if len(base_combinaison) > 0 and action['actions'] <= base_combinaison[-1]['actions']:
            continue
        new_remaining_actions = [a for a in remaining_actions if a != action]
        generate_combinations(base_combinaison + [action], new_remaining_actions, max_depth, result)


def somme_combinations(all_combinations, plafond):
    for combination in all_combinations:
        total_cout = sum([action['cout'] for action in combination])
        if total_cout < plafond:
            total_benefice = sum([(action['benefice'] * action['cout']) for action in combination])
            dict_somme_combination = {'actions': [action['actions'] for action in combination],
                                      'total_cout': total_cout, 'total_benefice': total_benefice}
            all_combinaison_limit_profit.append(dict_somme_combination)
    return all_combinaison_limit_profit


all_combinaisons = []
all_combinaison_limit_profit = []

csv_file_name = "actions.csv"
list_actions = open_csv_file(csv_file_name)
print(list_actions)

for i in range(1, len(list_actions) + 1):
    print(f"depth={i}")
    generate_combinations([], list_actions, i, all_combinaisons)

resultat = somme_combinations(all_combinaisons, 500)
resultat.sort(key=lambda x: x['total_benefice'], reverse=True)


best_combination = resultat[0]
print()
print(f"la meilleur combinaison est: {best_combination['actions']}")
print(f"Total cout: {best_combination['total_cout']}")
print(f"Total benefice: {best_combination['total_benefice']}")