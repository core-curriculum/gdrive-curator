import re
import pandas as pd

from lib.utils import SHEETS_OUTCOMES_DIR,SHEETS_OUTCOMES_DIR,get_glob_file
from lib.apply_condition_to_dataframe  import apply_condition_to_dataframe



def get_table_index():
    return pd.read_csv(f"{SHEETS_OUTCOMES_DIR}/別表一覧/別表一覧.csv",encoding="utf_8_sig")

def iter_tables_for_outcome_raw():
    table_index = get_table_index()
    for info in table_index.itertuples():
        file = get_glob_file(f"{SHEETS_OUTCOMES_DIR}/*編集用/別表-{info.データ元}.csv")
        table = pd.read_csv(file)
        table = apply_condition_to_dataframe(table,info.条件)
        table["index"]=table.reset_index().index+1
        table["index"]=f"TBL-{info.id}-"+table["index"].astype(str).str.zfill(3)
        yield table,info

table_index = get_table_index()
def format_table_ref(x:str)->str:
    def name_to_label(name:str):
        try:
            return table_index.set_index("表名").at[name,"id"]
        except KeyError:
            return ""

    def replace_func(reg:re.match)->str:
        name = reg.group(1)
        whole = reg.group(0)
        label = name_to_label(name)
        if label:
            return f"[@tbl:{label}]"
        else:
            return whole
    return re.sub(r"表\[([^\]]+)\]",replace_func,x)
