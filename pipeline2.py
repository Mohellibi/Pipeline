import json
from datetime import datetime

def load_sample(path) -> list[str]:
    with open(path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line == '\n':
            lines.remove(line)
    lines = [line.strip() for line in lines]
    return lines

def generate_json(data) -> list[dict]:
    transactions = {}
    for line in data:
        nom_emetteur, date, montant = line.split()
        montant = int(montant.replace('€', ''))
        if nom_emetteur in transactions:
            transactions[nom_emetteur] += montant
        else:
            transactions[nom_emetteur] = montant

    result = [{'name': name, 'total_sent': total} for name, total in transactions.items()]
    print(result)
    return result
    
def save_result(path, result):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"result_sample{timestamp}.json"
    with open(filename, 'w') as json_file:
        json.dump(result, json_file, indent=4)

""" résultat:
[{'name': 'john', 'total_sent': 8000}]
"""

"""
ca ne fonctionne pas
def process_files(source_dir, archived_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_dir, filename)
            data = load_sample(file_path)
            result = generate_json(data)
            save_result(result)
            os.rename(file_path, os.path.join(archived_dir, filename))

if __name__ == "__main__":
    process_files('pipeline','archive.txt')
"""
