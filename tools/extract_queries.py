import os
import argparse
from pathlib import Path
from dax_extract import read_data_model_schema
import re

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='pbit files dir or specific file. If dir is given script will print all '
                                   'queries on all pbit files.')
args = parser.parse_args()


def parse_pbit_file(file_path, file_name):
    print(f"# Parsing '{pbit_file_name}'")
    data = read_data_model_schema(Path(os.path.join(file_path, file_name)))

    printed_query_count = 0

    tables = data["model"]["tables"]

    for table in tables:
        for partition in table["partitions"]:
            queries = re.findall('Query=".*"', partition["source"]["expression"])

            for query in queries:
                printed_query_count += 1
                print(f"## {printed_query_count}.{' '.join(query.replace('#(lf)', ' ').split())}")

    if not printed_query_count:
        print("## No queries found")


pbit_dir = args.file

if re.match(r'.*\.pbit', pbit_dir):
    pbit_dir, pbit_file_name = os.path.split(pbit_dir)
    pbit_files_to_parse = [pbit_file_name]
else:
    pbit_files_to_parse = [f for f in os.listdir(pbit_dir) if re.match(r'.*\.pbit', f)]

print(f"{len(pbit_files_to_parse)} pbit files will be parsed")

for pbit_file_name in pbit_files_to_parse:
    parse_pbit_file(pbit_dir, pbit_file_name)
