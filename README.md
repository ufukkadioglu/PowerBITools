# PowerBITools

### Query extracter tested on Ubuntu 22.04.3 LTS with Python 3.10.12

### Report downloader tested on Windows 11 Pro with Python 3.10.11

### Install requirements for query extracter:

pip install -r requirements.txt

### To extract queries of single pbit file:

python tools/extract_queries.py --file "[path/to/file.pbit]"

### To extract queries of all pbit files in directory:

python tools/extract_queries.py --file "[path/to/directory]"

### To download pbix files for all reports in a workspace (script will need some intput and microsoft login to proceed):

python tools/download_pbix.py

### Downloader uses powershell and will give a proper warning if it is not installed on ubuntu, but windows does not show the proper warning and shows an error. Here is the page to install powershell if you do not get the proper warning:

https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell
