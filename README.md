# PowerBITools

### Tested on Ubuntu 22.04.3 LTS with Python 3.10.12

### Install requirements:

pip install -r requirements.txt

### To extract queries of single pbit file:

python tools/extract_queries.py --file "[path/to/file.pbit]"

### To extract queries of all pbit files in directory:

python tools/extract_queries.py --file "[path/to/directory]"

### To download pbix files for all reports in a workspace (script will need some intput and microsoft login to proceed):

python tools/download_pbix.py
