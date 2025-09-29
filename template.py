# A general template and can be used in any project
# this code generated full template with empty files to write code for project without manually doing the things

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

# Below is the project structure files needed to create this project
list_of_files = [
    ".github/workflows/.gitkeep",  #whenever we do cicd deployment we need this workflow folder which will contain main.yaml, having commands to successfully deploy it
    f"src/{project_name}/__init__.py",  #this constructor file helps make this folder as local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for file {filename}")

    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'File {filepath} already exists')