import os
from os import path
import glob
import pandas as pd



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
