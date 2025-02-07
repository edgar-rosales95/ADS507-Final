import pandas as pd

var_df = pd.read_csv('_variable_descriptions.csv')

var_df.columns
var_df.drop(columns = 'Table', inplace = True)

var_df.to_csv('var_descrips.txt', sep='\t', index = False)