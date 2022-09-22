# I used the World Bank API to collect my data
from audioop import avg
import wbgapi as wb
import pandas as pd
import numpy as np

def main():
  # Education Statistics Database
  wb.db = 12
  # World Bank API Object creates dataframe for data regarding percentage of upper secondary schools with access
  # to internet for teaching purposes
  # Dataframe consists of countries from Africa, South Asia, Latin America, the Carribean, Central Europe, and the Baltics
  # Data ranges from years 2015 - 2020 incrementing by one
  df = wb.data.DataFrame('UIS.SCHBSP.3.WINTERN', economy=wb.region.members('AFR').union(wb.region.members('CSA').union(wb.region.members('CLA').union(wb.region.members('CEB')))), 
    time=range(2015, 2020, 1))
  # Get separate dataframe for each continent
  african = df[df.index.isin(wb.region.members('AFR'))]
  south_asia = df[df.index.isin(wb.region.members('CSA'))]
  latin_america = df[df.index.isin(wb.region.members('CLA'))]
  europe = df[df.index.isin(wb.region.members('CEB'))]
  # Find mean percentage for each continent/region each year and make new dataframe
  avg_df = pd.DataFrame(index=["AFR", "CSA", "CLA", "CEB"], columns=["YR2015", "YR2016", "YR2017", "YR2018", "YR2019"])
  avg_df.iloc[0] = african.mean(axis=0)
  avg_df.iloc[1] = south_asia.mean(axis=0)
  avg_df.iloc[2] = latin_america.mean(axis=0)
  avg_df.iloc[3] = europe.mean(axis=0)
  avg_df = avg_df.transpose()
  avg_df.index.name = 'year'

  
  # Create csv file for initial data frame
  df.to_csv('Education_Statistics.csv')
  # Create csv file for final data frame
  avg_df.to_csv('Continent_Percentages.csv')

 
if __name__ == '__main__':
    main()  