import pandas as pd
df=pd.read_csv(r"C:\Users\Ali\Desktop\Test\country_vaccination_stats.csv")
print(df.head())
print(df.isnull().sum())

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)


#Answer_4-5

#Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column
#per country with the minimum daily vaccination number of relevant countries.

# Fill missing values with 0
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)

# Group by country and find the minimum daily vaccination number
min_daily_vaccinations = df.groupby('country')['daily_vaccinations'].min().reset_index()
print(min_daily_vaccinations)

# Merge back to fill missing values
df = df.merge(min_daily_vaccinations, on='country', suffixes=('', '_min'))

# Replace missing values with the minimum daily vaccination number
df['daily_vaccinations'] = df['daily_vaccinations'].where(df['daily_vaccinations'] != 0, df['daily_vaccinations_min'])

# Drop unnecessary columns
df.drop(columns=['daily_vaccinations_min'], inplace=True)

print(df)


#Answer_6

#Code Implementation Task: Implement code to list the top-3 countries with highest median daily
#vaccination numbers by considering missing values imputed version of dataset.

# Group by country and calculate median daily vaccinations
median_daily_vaccinations = df.groupby('country')['daily_vaccinations'].median().reset_index()

# Sort by median daily vaccinations and select top 3 countries
top_3_countries = median_daily_vaccinations.sort_values(by='daily_vaccinations', ascending=False).head(3)

print(top_3_countries)


#Answer_7

#What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY)
#by considering missing values imputed version of dataset?

# Filter the dataset for January 6, 2021
vaccinations_on_date = df[df['date'] == '2021-01-06']

# Calculate the total number of vaccinations on January 6, 2021
total_vaccinations_on_date = vaccinations_on_date['daily_vaccinations'].sum()

print("Total vaccinations done on 2021-01-06:", total_vaccinations_on_date)
#Answer is 0.




