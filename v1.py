liste_actions = ["Action-1", "Action-2", "Action-3", "Action-4", "Action-5", "Action-6"]
all_combinaisions = []
combinaison = []

for i1 in liste_actions:
    combinaison.append(i1)
    for i2 in liste_actions:
        if i1 == i2:
            continue
        else:
            combinaison.append(i1 + " " + i2)
            for i3 in liste_actions:
                if i1 == i3 or i2 == i3:
                    continue
                else:
                    combinaison.append(i1 + " " + i2 + " " + i3)

print(combinaison)
