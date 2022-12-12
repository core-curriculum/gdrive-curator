"""
apply condition to dataframe
"""
import re
import pandas as pd

def apply_condition_to_dataframe(data:pd.DataFrame,condition_text:str)->pd.DataFrame:
    """apply condition to dataframe"""
    condition_text = _escape_comma(condition_text)
    conditions =re.split(r" *, *",condition_text) if isinstance(condition_text,str)  else []
    result = data.copy()
    for condition in conditions:
        unit = r" *(.+?) *"
        spliter =r" *(=|<>) *"
        pattern = f"{unit}{spliter}{unit}$"
        if reg_match:=re.match(pattern,condition):
            key,cond_type,value = reg_match.groups()
            value = _un_escape_comma(value).strip('"')
        else:
            key = condition
            cond_type = "exits"
        match cond_type:
            case "=":
                result = result.loc[result[key]==value,:]
            case "<>":
                result = result.loc[result[key]!=value,:]
            case "exits":
                result = result.loc[~result[key].isna(),:]
    return result

def _escape_comma(text:str)->str:
    pattern = re.compile(r'(".*),(.*")')
    esc = "☺"
    while pattern.search(text):
        text = pattern.sub(r"\1"+esc+r"\2",text)
    return text

def _un_escape_comma(text:str)->str:
    esc = "☺"
    return text.replace(esc,",")

if __name__ == "__main__":
    print(_escape_comma('test"test1,test2,tes33,"'))
    print(_un_escape_comma(_escape_comma('test"test1,test2,tes33,"')))