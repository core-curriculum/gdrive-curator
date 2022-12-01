import os
from os import path
import glob
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SHEETS_DIR= os.path.join(BASE_DIR,"sheets")
DOCS_DIR= os.path.join(BASE_DIR,"docs")
DOCS_OUTCOMES_DIR= os.path.join(DOCS_DIR,"outcomes")
SHEETS_OUTCOMES_DIR= os.path.join(SHEETS_DIR,"outcomes")
SHEETS_GENERAL_DIR= os.path.join(SHEETS_DIR,"general")
OUTPUT_BASE_DIR= os.path.join(BASE_DIR,"output")
OUTPUT_RELATIONS_DIR = os.path.join(OUTPUT_BASE_DIR,"relations","from2016to2022")
OUTPUT_DIR= os.path.join(OUTPUT_BASE_DIR,"2022","ja")
OUTPUT_2016_DIR= os.path.join(OUTPUT_BASE_DIR,"2016")
OUTPUT_OUTCOMES_DIR= os.path.join(OUTPUT_DIR,"outcomes")
OUTPUT_OUTCOMES_TABLE_DIR= os.path.join(OUTPUT_OUTCOMES_DIR,"tables")
OUTCOME_TABLE_SOURCE_DIR= os.path.join(SHEETS_DIR,"outcome_tables_source")
TABLE_FORMATTED_DIR= os.path.join(OUTPUT_DIR,"tables")

DOCS_SOURCE_DIR = path.join(DOCS_DIR,"documents")
OUTPUT_DOCS_DIR = path.join(OUTPUT_DIR,"documents")
OUTPUT_DOCS_CONTENTS_DIR = path.join(OUTPUT_DOCS_DIR,"contents")


def get_glob_file(glob_path:str)->str:
    files = glob.glob(glob_path)
    if len(files)==0:
        raise Exception(f"Cannot find {glob_path}")
    return list(glob.glob(glob_path))[0]


def save_csv(data:pd.DataFrame,file_path:str):
    """
    save dataframe as csv file
    """
    data.to_csv(file_path,index=False,encoding="utf_8_sig")

def load_csv(file_path:str):
    """
    load dataframe as csv file
    """
    return pd.read_csv(file_path,encoding="utf_8_sig")


def save_text(text:str,file_path:str):
    """
    save text as text file
    """
    with open(file_path,"w",encoding="utf_8") as f:
        f.write(text)


def load_text(file_path:str):
    """
    load text file
    """
    text=""
    with open(file_path,"r",encoding="utf_8") as f:
        text = f.read()
    return text
