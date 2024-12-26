Please activate the virtual env and modules before running \
To run the entire package, head into root and run: bin/python3 src/main.py \
To replicate the virtual environment elsewhere, run: pip install -r /src/requirements.txt \
To compile python into windows exe, head into /Downloads and run: pyinstaller --noconsole -y --clean ~/Downloads/planningadmin/main.py --add-data "planningadmin/greatsettings.ini;."
