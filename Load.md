**Page for SQL code to load into database**

# Create Database

```sql
CREATE DATABASE IF NOT EXISTS wildfire_housing
```

# Create places table

```sql
CREATE TABLE IF NOT EXISTS places (
    place_id int PRIMARY KEY AUTO INCREMENT, --This will be for each unique place or FIPS Place Code
    state_id int FOREIGN KEY, -- This will be the FIPS State Code
    state_name VARCHAR(2),
    county_code int FOREIGN KEY, -- This will be the FIPS County Code.
    county_name VARCHAR(20),
    place_name VARCHAR(20)
);

-- Not sure yet how to fully organize this.  We don't have places for all columns so maybe make state and county a composite and places a foreign key
```

# Create Wildfire table

```sql
CREATE TABLE IF NOT EXISTS wildfire (
    
)