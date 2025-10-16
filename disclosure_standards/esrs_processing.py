import pandas as pd
from pathlib import Path
import sys

from config.paths import DISC_STANDARDS_RAW


REQ_KEYS = [
    'ESRS',
    'DR',
    'Paragraph',
    'Related AR',
    'Name',
    'Data Type',
    'Conditional or alternative DP'
]

def strip_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to convert all columns of the dataframe to string,
    and then return df with all values stripped of whitespaces
    """
    df = raw.loc[:, REQ_KEYS]
    df = df.astype(str)
    df = df.apply(lambda x: x.str.strip())
    return df





if __name__=="__main__":

    raw = pd.read_excel(DISC_STANDARDS_RAW / "EFRAG IG 3 List of ESRS Data Points.xlsx", skiprows=1, sheet_name='ESRS E1')

    print(raw.head())

    stripped_df = strip_df(raw)

    # extracting nested values and converting them to dict
    nested = (
        stripped_df.groupby(["ESRS", "DR", "Paragraph"], dropna=False)
        .apply(lambda g: g[["Related AR", "Name", "Data Type", "Conditional or alternative DP"]]
                .rename(columns={
                    "Related AR": "AR",
                    "Data Type": "datatype",
                    "Conditional or alternative DP": "dp_type"
                    })
                .to_dict(orient="records"))
        .reset_index(name="entries")
    )

    # converting to JSON
    level1 = (
        nested.groupby("ESRS")
        .apply(lambda g: g.groupby("DR")
            .apply(lambda h: dict(zip(h["Paragraph"], h["entries"])))
            .to_dict())
        .to_dict()
    )

    



