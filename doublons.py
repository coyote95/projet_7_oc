import csv

def find_duplicate_first_column(csv_file_name):
    try:
        with open(csv_file_name, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            first_column_values = set()
            line_number = 0
            duplicates = []

            for row in csv_reader:
                line_number += 1

                if row:  # Skip empty rows
                    first_column_value = row[0].strip()

                    if first_column_value in first_column_values:
                        duplicates.append(line_number)
                    else:
                        first_column_values.add(first_column_value)

            return duplicates  # Retourne la liste des numéros de lignes avec des doublons

    except FileNotFoundError:
        print(f"The file {csv_file_name} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while checking for duplicates: {e}")
        return None

# Exemple d'utilisation
csv_file_name = "dataset2_Python+P7.csv"
duplicate_lines = find_duplicate_first_column(csv_file_name)

if duplicate_lines is not None:
    if duplicate_lines:
        print(f"Duplicate values found in the first column at lines: {duplicate_lines}.")
    else:
        print(f"No duplicate values found in the first column of {csv_file_name}.")
