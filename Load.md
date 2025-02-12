**Page for SQL code to load into database**

# Create Database

```sql
CREATE DATABASE IF NOT EXISTS wildfire_housing
```

# Create places table

```sql
CREATE TABLE IF NOT EXISTS places (
    place_id int FOREIGN KEY, --This will reference the combined STATE-COUNTY-PLACE code from population data 
    state_id int FOREIGN KEY, -- This will be the FIPS State Code.  Make this primary key instead? 
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
    PRICE_ID INT AUTO_INCREMENT PRIMARY KEY, --Auto_incrementing for each new record since a new one will be added each month with updated price
    State_ID CHAR(2) NOT NULL, --Will need to make this a foreign_key
    region_name VARCHAR(40), 
    county_name VARCHAR(20),
    eval_date date, --this will be the date the housing price was assessed
    price DECIMAL(10, 2)
);
```

# Create Rentals Table

```sql
CREATE TABLE IF NOT EXISTS rentals (
    RENT_ID INT AUTO_INCREMENT PRIMARY KEY,
    STATE_ID CHAR(2) NOT NULL,
    region_name VARCHAR(40),
    county_name VARCHAR(40),
    eval_date DATE,
    price DECIMAL (10,2)
);
```



# Create Population Table

```sql
CREATE TABLE IF NOT EXISTS population (
    places_id int PRIMARY KEY,
)