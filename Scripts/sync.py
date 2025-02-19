def sync(states_list, state_population_dict, location_dict):
    for state in states_list:
        pop_df = state_population_dict[state]
        location_df = location_dict[state]

        columns_to_rename = {'PLACE': 'PLACEFP', 'NAME': 'PLACENAME'}

        pop_df = pop_df.rename(columns = columns_to_rename)

        merged_df = pop_df.merge(
            location_df[['COUNTYFP', 'COUNTYNAME', 'PLACEFP', 'PLACENAME']],
            on = ["PLACEFP", 'PLACENAME'],
            how = 'left'
        )
        merged_df.drop(columns = ['SUMLEV', 'COUSUB', 'CONCIT', 'PRIMGEO_FLAG', 'FUNCSTAT', 'ESTIMATESBASE2010', 'COUNTY'], inplace = True)
        merged_df = merged_df.drop_duplicates()
        merged_df = merged_df.dropna()
        merged_df['COUNTYFP'] = merged_df['COUNTYFP'].astype(int)
        state_population_dict[state] = merged_df