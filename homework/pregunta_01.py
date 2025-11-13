"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import pandas as pd
    import os

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", index_col=0, sep=";")

    df.dropna(axis=0, inplace=True)

    df["sexo"] = df["sexo"].str.lower()

    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"],
        dayfirst=True,
        format="mixed",
    )

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.removeprefix("$ ")
        .str.replace(",", "")
        .astype("float64")
    )

    columnas_unificables = [
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]

    for col in columnas_unificables:
        df[col] = df[col].str.lower().str.replace(r"[ .-]", "_", regex=True).str.strip()

    df.drop_duplicates(inplace=True)

    if not os.path.exists("files/output/"):
        os.makedirs("files/output/")

    df.to_csv(
        "files/output/solicitudes_de_credito.csv", sep=";", header=True, index=False
    )
