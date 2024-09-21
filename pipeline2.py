import os
import json
import datetime
from memory_profiler import profile

def load_sample(path):
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                yield line  

def generate_json(data):
    transactions = {}
    for line in data:
        nom_emetteur, date, montant = line.split()
        montant = float(montant.replace('€', ''))
        if nom_emetteur in transactions:
            transactions[nom_emetteur] += montant
        else:
            transactions[nom_emetteur] = montant

    yield from [{'name': name, 'total_sent': total} for name, total in transactions.items()]  

""" résultat:
[{'name': 'john', 'total_sent': 8000}]
"""


def save_result(result):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"result/result_sample_{timestamp}.json"
    with open(filename, 'w') as json_file:
        json.dump(list(result), json_file, indent=4)  


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
