list_actions = [{'actions': 'action-1', 'cout': 20, 'benefice': 5},
                {'actions': 'action-2', 'cout': 30, 'benefice': 10},
                {'actions': 'action-3', 'cout': 50, 'benefice': 15},
                {'actions': 'action-4', 'cout': 70, 'benefice': 20},
                {'actions': 'action-5', 'cout': 60, 'benefice': 17},
                {'actions': 'action-6', 'cout': 80, 'benefice': 25},
                {'actions': 'action-7', 'cout': 22, 'benefice': 7},
                {'actions': 'action-8', 'cout': 26, 'benefice': 11},
                {'actions': 'action-9', 'cout': 48, 'benefice': 13},
                {'actions': 'action-10', 'cout': 34, 'benefice': 27},
                {'actions': 'action-11', 'cout': 42, 'benefice': 17},
                {'actions': 'action-12', 'cout': 110, 'benefice': 9},
                {'actions': 'action-13', 'cout': 38, 'benefice': 23},
                {'actions': 'action-14', 'cout': 14, 'benefice': 1},
                {'actions': 'action-15', 'cout': 18, 'benefice': 3},
                {'actions': 'action-16', 'cout': 8, 'benefice': 8},
                {'actions': 'action-17', 'cout': 4, 'benefice': 12},
                {'actions': 'action-18', 'cout': 10, 'benefice': 14},
                {'actions': 'action-19', 'cout': 24, 'benefice': 21},
                {'actions': 'action-20', 'cout': 114, 'benefice': 18}]
all_combinaisons = []
all_combinaisons_plafond = []


def generate_combinations(prefix, remaining_actions, max_depth, result):
    if len(prefix) == max_depth:
        result.append(prefix)
        return

    for action in remaining_actions:
        if len(prefix) > 0 and action['actions'] <= prefix[-1]['actions']:
            continue
        new_remaining_actions = [a for a in remaining_actions if a != action]
        generate_combinations(prefix + [action], new_remaining_actions, max_depth, result)


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

