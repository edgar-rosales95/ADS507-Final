from rapidfuzz import process, fuzz
from tqdm import tqdm

state_fips_mapping = {
    "CA": 6,  # California
    "TX": 48, # Texas
    "FL": 12, # Florida
    "GA": 13, # Georgia
    "AZ": 4   # Arizona
}

def match_county_id(data_df, counties_df, state_col="state_id", county_col="county_name", threshold=85):
    """
    Matches county names in the dataset to official counties using fuzzy matching.

    Optimizations:
    - Uses `rapidfuzz` (faster fuzzy matching)
    - Caches results to avoid redundant computations
    - Precomputes county name choices per state

    Parameters:
    - data_df (pd.DataFrame): DataFrame containing records that need county_id assignment.
    - counties_df (pd.DataFrame): Official Census counties with state_id, county_name, and county_id.
    - state_col (str): Column name for state_id.
    - county_col (str): Column name for county_name.
    - threshold (int): Minimum similarity score to consider a match.

    Returns:
    - pd.DataFrame: Updated DataFrame with county_id assigned.
    """
    
    tqdm.pandas()  # Enable progress bar
    
    # Create lookup dictionary: {state_id: (county_name_list, county_id_map)}
    county_lookup = {
        state_id: (
            counties_df[counties_df[state_col] == state_id]["county_name"].tolist(),
            counties_df[counties_df[state_col] == state_id].set_index("county_name")["county_id"].to_dict()
        )
        for state_id in counties_df[state_col].unique()
    }

    # Cache for already matched county names
    match_cache = {}

    def find_best_match(state_id, county_name):
        if state_id in county_lookup:
            county_names, county_id_map = county_lookup[state_id]

            # Check cache first
            cache_key = (state_id, county_name)
            if cache_key in match_cache:
                return match_cache[cache_key]

            # Fuzzy match
            match, score, _ = process.extractOne(county_name, county_names, scorer=fuzz.token_sort_ratio)
            if score >= threshold:
                county_id = county_id_map[match]
                match_cache[cache_key] = county_id  # Cache result
                return county_id

        return None  # No match found

    # Apply fuzzy matching with caching and progress bar
    data_df["county_id"] = data_df.progress_apply(lambda row: find_best_match(row[state_col], row[county_col]), axis=1)

    return data_df