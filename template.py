#this python file is used to create the template of the project setup for any python software
import os
from pathlib import Path 
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s',
    filename='logfile.log'
) 

project_name = "TextSummerizer"
list_of_files = {
    ".github/wordflows/.gitkeep",  # Removed the trailing '/' 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
} 

for filepath in list_of_files: 
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    print(f"Directory: {filedir}, Filename: {filename}")

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  
        logging.info(f"creating directory: {filedir} for the file {filename}")

    if (not filepath.exists()) or (filepath.stat().st_size == 0): 
        with open(filepath, 'w'):
            pass
        logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} already exists")
