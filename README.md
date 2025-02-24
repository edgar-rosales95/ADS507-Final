# ADS507-Final

---

### Table of Contents

- [Description](#description)
- [Monitoring](#monitoring)
- [License](#license)

---

## Description

Wildfires have become an increasing concern for home buyers, renters, and real estate investors, impacting housing prices, rental trends, and population shifts. This project aims to develop a data pipeline that integrates wildfire records, housing market data, and population statistics to provide insights into how wildfire activity influences real estate markets in affected areas.

To achieve this, we source data from:
- Kaggle: Historical wildfire data, including fire location, size, and cause.
- Zillow: Home sales and rental prices by city.
- Census Data: Year-over-year population changes in high-risk wildfire states.

# Deployment

The extraction phase involves retrieving raw data from multiple sources and loading it into Pandas DataFrames for preprocessing. The primary dataset for wildfire records is sourced from Kaggle's U.S. Wildfire Records dataset, which includes details such as fire name, discovery date, cause, size, and location. The pipeline uses the Kaggle API via the kagglehub library to automate data retrieval, storing the extracted data in a Pandas DataFrame with key columns like FIRE_NAME, DISCOVERY_DATE, NWCG_GENERAL_CAUSE, FIRE_SIZE, STATE, and FIPS_NAME. This API-based approach ensures data accuracy and facilitates updates when new wildfire data is released.

Once extracted, the raw data undergoes cleaning and transformation to ensure consistency and relevance. The dataset is filtered to include only wildfire records from heavily impacted states—California, Texas, Georgia, Florida, and Arizona—while excluding records outside these regions and those predating the year 2000. The DISCOVERY_DATE column is standardized into a datetime format, and additional steps like renaming columns, removing duplicates, and standardizing categorical variables (e.g., fire causes) are applied to enhance data quality. The cleaned dataset is then loaded into an Azure-hosted MySQL database using MySQL Connector and SQLAlchemy, with secure authentication ensuring data integrity. The transformed data is stored in a dedicated table named *wildfires*, structured with attributes like fire_id, fire_name, discovery_date, fire_size, state, and zip_code, enabling seamless integration with housing and population data for future analysis.

# Monitoring

By storing the dataset in Azure MySQL, the system enables scalability, accessibility, and efficient querying, allowing users to analyze the relationship between wildfire activity and housing trends. This structured approach also supports potential dashboard integration and data visualization tools, ensuring that insights can be derived efficiently from the stored data.



#### Technologies

- SQL
- Python

[Back To The Top](#read-me-template)

---



[Back To The Top](#read-me-template)

---

## References
[Back To The Top](#read-me-template)

---

## License

MIT License


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

[Back To The Top](#read-me-template)
