import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ts_confirmed = pd.read_csv('time_series_covid_19_confirmed.csv')
ts_recovered = pd.read_csv('time_series_covid_19_recovered.csv')
ts_deaths = pd.read_csv('time_series_covid_19_deaths.csv')

ts_confirmed = ts_confirmed.replace(np.nan, '', regex=True)
ts_recovered = ts_recovered.replace(np.nan, '', regex=True)
ts_deaths = ts_deaths.replace(np.nan, '', regex=True)
#print(ts_confirmed.head())
#print(ts_recovered.head())
#print(ts_deaths.head())


#create location string
# Create empty column
Location_string = pd.Series('Null',index=ts_confirmed.index)

# Populate column with batch numbers
for i in range(len(ts_confirmed)):
    Location_string[i] = str(ts_confirmed['Country/Region'][i])+' '+str(ts_confirmed['Province/State'][i])

# Insert batch column into reordered_clean_table
ts_confirmed.insert(2,'Location_string',Location_string)
#-----------------------------------------------------------------------------------------------------------------------
# Create empty column
Location_string = pd.Series('Null',index=ts_recovered.index)

# Populate column with batch numbers
for i in range(len(ts_recovered)):
    Location_string[i] = str(ts_recovered['Country/Region'][i])+' '+str(ts_recovered['Province/State'][i])

# Insert batch column into reordered_clean_table
ts_recovered.insert(2,'Location_string',Location_string)
#-----------------------------------------------------------------------------------------------------------------------
# Create empty column
Location_string = pd.Series('Null',index=ts_deaths.index)

# Populate column with batch numbers
for i in range(len(ts_deaths)):
    Location_string[i] = str(ts_deaths['Country/Region'][i])+' '+str(ts_deaths['Province/State'][i])

# Insert batch column into reordered_clean_table
ts_deaths.insert(2,'Location_string',Location_string)
#-----------------------------------------------------------------------------------------------------------------------
# DROPPING USELESS COLUMNS

ts_confirmed=ts_confirmed.drop(['Province/State','Country/Region','Lat','Long'],axis=1)
ts_recovered=ts_recovered.drop(['Province/State','Country/Region','Lat','Long'],axis=1)
ts_deaths=ts_deaths.drop(['Province/State','Country/Region','Lat','Long'],axis=1)

#-----------------------------------------------------------------------------------------------------------------------
# ORDERING VALUES

ts_confirmed = ts_confirmed.sort_values(by=['Location_string'])
ts_recovered = ts_recovered.sort_values(by=['Location_string'])
ts_deaths = ts_deaths.sort_values(by=['Location_string'])

#-----------------------------------------------------------------------------------------------------------------------

plot_confirmed = ts_confirmed.drop(['Location_string'],axis=1)
plot_recovered = ts_recovered.drop(['Location_string'],axis=1)
plot_deaths = ts_deaths.drop(['Location_string'],axis=1)

plt.style.use('ggplot')

dates_list = plot_confirmed.columns
dates_list_clean = []
for element in dates_list:
    element = element[:-3]
    dates_list_clean.append(element)

#53 -1/2 = 26
location = 0

while location < 400:
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 5)
    plt.plot(plot_confirmed.loc[location].values,c='b',label='Confirmed Cases')
    plt.plot(plot_recovered.loc[location].values,c='g',label='Recovered')
    plt.plot(plot_deaths.loc[location].values,c='r',label='Deaths')
    plt.legend()
    #plt.axis('off')
    plt.title(ts_confirmed['Location_string'][location])
    plt.xticks(range(0, len(plot_confirmed.columns)),dates_list_clean)
    every_nth = 4
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    plt.show()
    location = location +1
