import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SHEETS_DIR= os.path.join(BASE_DIR,"sheets")
DOCS_DIR= os.path.join(BASE_DIR,"docs")
DOCS_OUTCOMES_DIR= os.path.join(DOCS_DIR,"outcomes")
SHEETS_OUTCOMES_DIR= os.path.join(SHEETS_DIR,"outcomes")
SHEETS_GENERAL_DIR= os.path.join(SHEETS_DIR,"general")
OUTPUT_DIR= os.path.join(BASE_DIR,"output","2022","ja")
OUTPUT_OUTCOMES_DIR= os.path.join(OUTPUT_DIR,"outcomes")
OUTPUT_OUTCOMES_TABLE_DIR= os.path.join(OUTPUT_OUTCOMES_DIR,"tables")
OUTCOME_TABLE_SOURCE_DIR= os.path.join(SHEETS_DIR,"outcome_tables_source")
OUTPUT_RELATIONS_DIR = os.path.join(OUTPUT_DIR,"relations","from2016to2022")
TABLE_FORMATTED_DIR= os.path.join(OUTPUT_DIR,"tables")

def get_glob_file(glob_path:str)->str:
    files = glob.glob(glob_path)
    if len(files)==0:
        raise Exception(f"Cannot find {glob_path}")
    return list(glob.glob(glob_path))[0]


