def fill_missing_values(df, replace_dict, col, fill_col):
    """
    Fill missing values based on the state column.
    """
    for key, value in replace_dict.items():
        df.loc[df[col] == key, fill_col] = df.loc[df[col] == key, fill_col].fillna(value)
    return df