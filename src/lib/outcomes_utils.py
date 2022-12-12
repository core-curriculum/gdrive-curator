import re
import pandas as pd

from lib.vars import dirs
from lib.utils import get_glob_file
from lib.apply_condition_to_dataframe  import apply_condition_to_dataframe

table_columns_conversion = {
    "ja":{"name-ja":"name","legend-ja":"legend","columns-ja":"columns","main-ja":"main","conditions-ja":"conditions"},
    "en":{"name-en":"name","legend-en":"legend","columns-en":"columns","main-en":"main","conditions-en":"conditions"},
}

table_columns = ["id","name","UID","source","legend","number","index","columns","main","conditions","layout","ref"]



def get_table_index(lang="ja"):
    return pd.read_csv(f"{dirs().source.sheets.outcomes}/別表一覧/別表一覧.csv",encoding="utf_8_sig")\
        .rename(columns=table_columns_conversion[lang])\
        .loc[:,table_columns]

def iter_tables_for_outcome_raw(lang="ja"):
    table_index = get_table_index(lang)
    for info in table_index.itertuples():
        file = get_glob_file(f"{dirs().source.sheets.outcomes}/*編集用/別表-{info.source}.csv")
        table = pd.read_csv(file)
        table = apply_condition_to_dataframe(table,info.conditions)
        table["index"]=table.reset_index().index+1
        table["index"]=f"{info.index}-"+table["index"].astype(str).str.zfill(3)
        yield table,info

table_index = get_table_index()
def format_table_ref(x:str)->str:
    def name_to_label(name:str):
        try:
            return table_index.set_index("name").at[name,"id"]
        except KeyError:
            return ""

    def replace_func(reg:re.match)->str:
        name = reg.group(2)
        whole = reg.group(0)
        label = name_to_label(name)
        if label:
            return f"[@tbl:{label}]"
        else:
            return whole
    return re.sub(r"表|(Table) ?\[([^\]]+)\]",replace_func,x)
