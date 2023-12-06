import csv


def open_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            print("csv reader", csv_reader)
            csv_content = list(csv_reader)
            print("csv content", csv_content)
        return csv_content
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return None


# Example usage
csv_file_name = "actions.csv"
csv_data = open_csv_file(csv_file_name)
# list_ligne_1 = []
# i = 0
# if csv_data is not None:
#     for ligne in range(0, len(csv_data) - 1):
#         print(csv_data[0]['cout'])
#         print(csv_data[1 + ligne]['cout'])
#         ligne_1 = int(csv_data[0]['cout']) + int(csv_data[1 + ligne]['cout'])
#         list_ligne_1.append(ligne_1)
#         i += 1
#         print(i, ligne_1)
#     csv_data.pop(0)
# print(len(csv_data))
# print(f"liste ligne 1:{list_ligne_1}")

if csv_data is not None:
    total_ligne_1 = int(csv_data[0]['cout'])
    for ligne in range(0, len(csv_data) - 1):
        if total_ligne_1 + int(csv_data[1 + ligne]['cout']) < 500:
            total_ligne_1 += int(csv_data[1 + ligne]['cout'])
            print(f"ok{total_ligne_1 }")
        else:
            print(f"stop{total_ligne_1 + int(csv_data[1 + ligne]['cout'])}")
            break
