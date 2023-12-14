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
                row['price'] = int(float(row['price']) * 100)
                row['profit'] = (float(row['profit']) / 100)
        return csv_content
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return None


csv_file_name = "dataset2_Python+P7.csv"
list_actions = open_csv_file(csv_file_name)
print(list_actions)

list_actions_clean = [action for action in list_actions if action['price'] > 0]



print(list_actions_clean)
print(len(list_actions_clean))
#

# Convert the 'actions'list of dictionary to a list of tuples
actions_tuples = [(action['name'], action['price'], action['profit'] * action['price']) for action in list_actions_clean]
i = 0
print(actions_tuples)
print(len(actions_tuples))


# Solution optimale - programmation dynamique
def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    # Determine the number of rows and columns
    num_rows = len(matrice)
    num_columns = len(matrice[0])  # Assuming all rows have the same number of columns

    # Print the size of the matrix
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_columns}")

    for i in range(1, len(elements) + 1):
        for j in range(1, capacite + 1):
            if elements[i - 1][1] <= j:
                matrice[i][j] = max(elements[i - 1][2] + matrice[i - 1][j - elements[i - 1][1]], matrice[i - 1][j])
            else:
                matrice[i][j] = matrice[i - 1][j]

    # Retrouver les éléments en fonction de la somme
    j = capacite
    i = len(elements)
    elements_selection = []

    while j > 0 and i > 0:
        e = elements[i - 1]
        if matrice[i][j] == matrice[i - 1][j - e[1]] + e[2]:
            elements_selection.append(e)
            j -= e[1]

        i -= 1

    return matrice[-1][-1], elements_selection


benefice, actions = sacADos_dynamique(50000, actions_tuples)
print('Algo dynamique', benefice, actions)
print(len(actions))

total_price = sum(action[1] for action in actions)/100
print("Total Price:", total_price)


