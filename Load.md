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
    state_name CHAR(2),
    county_code int FOREIGN KEY, -- This will be the FIPS County Code.
    county_name VARCHAR(20),
    place_name VARCHAR(20)
);

-- Not sure yet how to fully organize this.  We don't have places for all columns so maybe make state and county a composite and places a foreign key
```

# Create Wildfire table

```sql
CREATE TABLE IF NOT EXISTS wildfire (
    object_id int PRIMARY KEY, -- included with the wildfire data
    fire_name VARCHAR(20), --Lot of unknowns in this feature and a lot of repeats (like 'Grass fire') better to just delete?
    discovery_date date,
    cause VARCHAR(20), --we have two, one that's general and one specific, probably will just keep one
    state CHAR(2),
    state_id int FOREIGN KEY,
    county_name VARCHAR(20)
);

--we can use county and state id codes but necessary?
```


# Create Housing Table

```sql
CREATE TABLE IF NOT EXISTS housing (
    region_id int PRIMARY KEY, --use this as Primary key?  I think we'll need it since each record will have a bunch of dates and prices
    state CHAR(2),
    county_name VARCHAR(20),
    eval_date date, --this will be the date the housing price was assessed
    price DECIMAL(10, 2),
    size_rank
);

--I think it's best to combine all housing data, not sure what value separating bottom and top is anymore, maybe still include size rank and for data processing we'll need to pivot long the price values and date features
```