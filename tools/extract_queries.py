import os
import argparse
from pathlib import Path
from dax_extract import read_data_model_schema
import re

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='pbit files dir or specific file. If dir is given script will print all '
                                   'queries on all pbit files.')
parser.add_argument('--output', help='csv file to write queries.')
args = parser.parse_args()

output_file_path = args.output

def write_queries(file_name, queries):
    with open(output_file_path, "a") as output_file:
        for query in queries:
            output_file.write(file_name + ";" + query + "\n")


def parse_pbit_file(file_path, file_name):
    print(f"# Parsing '{pbit_file_name}'")
    data = read_data_model_schema(Path(os.path.join(file_path, file_name)))

    tables = data["model"]["tables"]
    
    all_queries = []

    for table in tables:
        for partition in table["partitions"]:
            queries = re.findall('Query=".*?"', partition["source"]["expression"])
                        
            for query in queries:
                clean_query = ' '.join(query.replace('Query="', '')[:-1].replace('#(lf)', ' ').replace('#(tab)', '\t').split())
                all_queries.append(clean_query)

    if not all_queries:
        print("## No queries found")
    else:
        print(f"## {len(all_queries)} queries will be written to output")
        write_queries(file_name, all_queries)


pbit_dir = args.input

if re.match(r'.*\.pbit', pbit_dir):
    pbit_dir, pbit_file_name = os.path.split(pbit_dir)
    pbit_files_to_parse = [pbit_file_name]
else:
    pbit_files_to_parse = [f for f in os.listdir(pbit_dir) if re.match(r'.*\.pbit', f)]

print(f"{len(pbit_files_to_parse)} pbit files will be parsed")

for pbit_file_name in pbit_files_to_parse:
    parse_pbit_file(pbit_dir, pbit_file_name)
