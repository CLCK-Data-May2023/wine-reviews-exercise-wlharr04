import pandas as pd

dfreviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

#Get the relevant data from the original dataframe
country_counts = dfreviews.country.value_counts()
country_points = dfreviews.groupby(['country']).points.mean().round(1)

#Combine the series and rename the columns
dfcountries = pd.concat([country_counts, country_points], axis=1).rename(columns={'country': 'count'})

#Save as CSV
dfcountries.to_csv('data/reviews-per-country.csv', index_label='country')