actions = {
    "Action-1": {"cout": 20, "benefice": 0.05},
    "Action-2": {"cout": 30, "benefice": 0.10},
    "Action-3": {"cout": 50, "benefice": 0.15},
    "Action-4": {"cout": 70, "benefice": 0.20},
    "Action-5": {"cout": 60, "benefice": 0.17},
    "Action-6": {"cout": 80, "benefice": 0.25},
    "Action-7": {"cout": 22, "benefice": 0.07},
    "Action-8": {"cout": 26, "benefice": 0.11},
    "Action-9": {"cout": 48, "benefice": 0.13},
    "Action-10": {"cout": 34, "benefice": 0.27},
    "Action-11": {"cout": 42, "benefice": 0.17},
    "Action-12": {"cout": 110, "benefice": 0.09},
    "Action-13": {"cout": 38, "benefice": 0.23},
    "Action-14": {"cout": 14, "benefice": 0.01},
    "Action-15": {"cout": 18, "benefice": 0.03},
    "Action-16": {"cout": 8, "benefice": 0.08},
    "Action-17": {"cout": 4, "benefice": 0.12},
    "Action-18": {"cout": 10, "benefice": 0.14},
    "Action-19": {"cout": 24, "benefice": 0.21},
    "Action-20": {"cout": 114, "benefice": 0.18},
}

budget_max = 500


def meilleur_combinaison(actions, budget_max):
    dp = [[0] * (budget_max + 1) for _ in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for j in range(budget_max + 1):
            cout_action = actions[list(actions.keys())[i - 1]]["cout"]
            benefice_action = actions[list(actions.keys())[i - 1]]["benefice"]
            if cout_action <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cout_action] + cout_action * benefice_action)
            else:
                dp[i][j] = dp[i - 1][j]

    combinaison_optimale = []
    i, j = len(actions), budget_max
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            combinaison_optimale.append(list(actions.keys())[i - 1])
            j -= actions[list(actions.keys())[i - 1]]["cout"]
        i -= 1

    return combinaison_optimale


def calculer_cout_benefice(combinaison, actions):
    cout_total = sum(actions[action]["cout"] for action in combinaison)
    benefice_total = sum(actions[action]["cout"] * actions[action]["benefice"] for action in combinaison)
    return cout_total, benefice_total


resultat = meilleur_combinaison(actions, budget_max)
cout_total, benefice_total = calculer_cout_benefice(resultat, actions)

print("Meilleure combinaison d'actions :", resultat)
print("Coût total :", cout_total, "euros")
print("Bénéfice total :", benefice_total, "euros")
