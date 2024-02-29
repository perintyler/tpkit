 #!/bin/sh 

python3 -m venv venv;
. venv/bin/activate;
pip install .;
python3 ./scripts/source_bash_functions.py
deactivate;
rm -r venv;
