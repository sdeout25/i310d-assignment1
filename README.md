# i310d-assignment1
I310D Introduction to Human Centered Data Science Assignment#1


For this assignment, I used the World Bank API to collect and process data from one of their many databases. I collected data from the Education Statistics database, speficically the percentage of upper secondary schools with internet access for learning. I looked at the countries in multiple regions: Africa, South Asia, Europe, and Latin America. My goal was to see just how large the difference in access to internet for schools in areas like Africa and South Asia to developed Europe. The data has multiple issues. Many individual countries had unknown values for some years, and those values were not counted in the continent average. Data in the files consists of years as strings (i.e. 'YR2015' = 2015), 3 letter strings for country abbreviations (i.e. 'ARG' = Argentina). Mean percetages have type float as values in the table. Other than the large amount of unknown values, there were no other significant issues with the data or indications of bias.

WORLD BANK API DOCUMENTATION: https://documents.worldbank.org/en/publication/documents-reports/api
DATA LICENSE:  Creative Commons Attribution 4.0 International license
