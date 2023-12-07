import csv


def open_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            csv_content = list(csv_reader)
            csv_content = [{key.strip('\ufeff'): value.strip() for key, value in row.items()} for row in csv_content]
            for row in csv_content:
                row['cout'] = int(row['cout'])
                row['benefice'] = float(row['benefice'].rstrip('%'))/100
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

all_combinaisons = []
all_combinaisons_plafond = []


def generate_combinations(base_combinaison, remaining_actions, max_depth, result):
    if len(base_combinaison) == max_depth:
        result.append(base_combinaison)
        return

    for action in remaining_actions:
        if len(base_combinaison) > 0 and action['actions'] <= base_combinaison[-1]['actions']:
            continue
        new_remaining_actions = [a for a in remaining_actions if a != action]
        generate_combinations(base_combinaison + [action], new_remaining_actions, max_depth, result)


for i in range(1, len(list_actions) + 1):
    print(f"depth={i}")
    generate_combinations([], list_actions, i, all_combinaisons)


def somme_combinations(all_combinaisons, plafond):
    for combination in all_combinaisons:
        action_names = [action['actions'] for action in combination]
        total_cout = sum([action['cout'] for action in combination])
        if total_cout < plafond:

            total_benefice = sum([((action['benefice']/100) * action['cout'] ) for action in combination])
            result_combination = {'actions': [action['actions'] for action in combination], 'total_cout': total_cout,
                                  'total_benefice': total_benefice}

            all_combinaisons_plafond.append(result_combination)
            # print(f"Combinaison : {action_names}, Somme : {total_cout}, Benefice: {total_benefice}")

    return all_combinaisons_plafond


resultat = somme_combinations(all_combinaisons, 500)
resultat_trie = sorted(resultat, key=lambda x: x['total_benefice'], reverse=False)

# Affichage du résultat trié
print("Résultat trié par plus grand total bénéfice :")
for result in resultat_trie:
    print(f"Combinaison : {result['actions']}, Somme : {result['total_cout']}, Benefice : {result['total_benefice']}")




