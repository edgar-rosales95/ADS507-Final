
CREATE TABLE IF NOT EXISTS locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    county_id INT NOT NULL,
    state_name CHAR(2) NOT NULL,
    county_name VARCHAR(50) NOT NULL,
    UNIQUE (state_id, county_id)
);

CREATE TABLE IF NOT EXISTS wildfire (
    fire_id INT PRIMARY KEY,
    location_id INT NOT NULL,
    fire_name VARCHAR(50),
    fire_size DECIMAL(10, 2),
    discovery_date DATE,
    cause VARCHAR(50),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);


CREATE TABLE IF NOT EXISTS housing (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    region_name VARCHAR(50),
    assessment_date DATE,
    price DECIMAL(10, 2),
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    UNIQUE (location_id, region_name, assessment_date, price)
);


CREATE TABLE IF NOT EXISTS rentals (
    rent_price_id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    region_name VARCHAR(50),
    assessment_date DATE,
    price DECIMAL(10, 2),
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    UNIQUE (location_id, region_name, assessment_date, price)
);


CREATE TABLE IF NOT EXISTS census (
    location_id INT NOT NULL,
    true_pop_2010 INT CHECK (true_pop_2010 >= 0),
    pop_estimate_2011 INT,
    pop_estimate_2012 INT,
    pop_estimate_2013 INT,
    pop_estimate_2014 INT,
    pop_estimate_2015 INT,
    pop_estimate_2016 INT,
    pop_estimate_2017 INT,
    pop_estimate_2018 INT,
    pop_estimate_2019 INT,
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    UNIQUE (location_id)
);
