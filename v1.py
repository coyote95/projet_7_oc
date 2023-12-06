# liste_actions = ["Action-1", "Action-2", "Action-3", "Action-4", "Action-5", "Action-6"]
# combinaison = []
#
# for i1 in liste_actions:
#     combinaison.append(i1)
#     for i2 in liste_actions:
#         if i1 == i2:
#             continue
#         else:
#             combinaison.append(i1 + " " + i2)
#             for i3 in liste_actions:
#                 if i1 == i3 or i2 == i3:
#                     continue
#                 else:
#                     combinaison.append(i1 + " " + i2 + " " + i3)
#
# print(combinaison)

def generate_combinations(prefix, remaining_actions, max_depth, result):
    print(f"prefix={prefix}, max_depth={max_depth}")
    print(remaining_actions)

    if len(prefix) == max_depth:
        result.append(prefix)
        return


    for action in remaining_actions:
        if len(prefix) > 0 and action <= prefix[-1]:
            continue
        new_remaining_actions = [a for a in remaining_actions if a != action ]
        generate_combinations(prefix + [action], new_remaining_actions, max_depth, result)

liste_actions = ["Action-1", "Action-2", "Action-3", "Action-4", "Action-5", "Action-6"]
all_combinaisons = []

for i in range(1, len(liste_actions) + 1):
    generate_combinations([], liste_actions, i, all_combinaisons)
    print("fini")



for combinaision in all_combinaisons:
    print(combinaision)

#
# def generate_combinations(prefix, remaining_actions, max_depth, result):
#     if len(prefix) == max_depth:
#         result.append(prefix)
#         return
#
#     for action in remaining_actions:
#         new_remaining_actions = [a for a in remaining_actions if a != action and a > action]
#         generate_combinations(prefix + [action], new_remaining_actions, max_depth, result)
#
# # Exemple d'utilisation
# dict_actions = ["Action-1", "Action-2", "Action-3", "Action-4", "Action-5", "Action-6"]
# max_depth = len(dict_actions)
#
# all_combinations = []
# generate_combinations([], dict_actions, max_depth, all_combinations)
#
# # Afficher toutes les combinaisons
# for combination in all_combinations:
#     print(combination)
