# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

data = pd.read_csv(path)
data.rename(columns={'Total': 'Total_Medals'}, inplace=True)
print(data.head(10))
#Code starts here



# --------------
#Code starts here   





data['Better_Event'] = np.where(data.Total_Summer > data.Total_Winter, 'Summer', np.where(data.Total_Summer == data.Total_Winter, 'Both', 'Winter'))

better_event = better_event = data.Better_Event.value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter', 'Total_Medals']]
top_countries.set_index('Country_Name')
top_countries.drop(top_countries.index[-1], inplace=True)

def top_ten(df, col):
    country_list = []
    top10 = df.nlargest(10, col)
    country_list = list(top10['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10  = top_ten(top_countries, 'Total_Medals')

common = set(top_10_summer).intersection(set(top_10_winter))
common = list(common.intersection(set(top_10)))
print(common)



# --------------
#Code starts here
summer_df = data[data.Country_Name.isin(top_10_summer)]
winter_df = data[data.Country_Name.isin(top_10_winter)]
top_df = data[data.Country_Name.isin(top_10)]

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 8))

country_names = summer_df.Country_Name
ax1.bar(country_names, summer_df.Total_Summer)
ax2.bar(country_names, winter_df.Total_Winter)
ax3.bar(country_names, top_df.Total_Medals)

plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df.Gold_Summer / summer_df.Total_Summer
summer_max_ratio = summer_df.Golden_Ratio.values.max()
country_id = summer_df.Golden_Ratio.idxmax()
summer_country_gold  = summer_df.loc[country_id][0]

winter_df['Golden_Ratio'] = winter_df.Gold_Winter / winter_df.Total_Winter
winter_max_ratio = winter_df.Golden_Ratio.values.max()
country_id = winter_df.Golden_Ratio.idxmax()
winter_country_gold = summer_df.loc[country_id][0]

top_df['Golden_Ratio'] = top_df.Gold_Total / top_df.Total_Medals
top_max_ratio = top_df.Golden_Ratio.values.max()
country_id = top_df.Golden_Ratio.idxmax()
top_country_gold = top_df.loc[country_id][0]


# --------------
#Code starts here
data_1 = data.drop(data.tail(1).index)

data_1['Total_Points'] = data_1.Gold_Total * 3 + data_1.Silver_Total * 2 + data_1.Bronze_Total
most_points = data_1.Total_Points.max()
country_id = data_1.Total_Points.idxmax()
best_country = data_1.loc[country_id][0]

print(best_country)
print(most_points)


# --------------
#Code starts here

best = data[data.Country_Name == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)
plt.xlabel(best_country)
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


