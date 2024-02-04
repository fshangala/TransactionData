import pandas
from datetime import datetime

# import data
dataframe = pandas.read_csv('sample1.csv',header=None)
dataframe[1] = dataframe[1].map(lambda x: datetime.strptime(x,'%d/%m/%Y'))

# query parameters
input_1 = input('Start Date (dd/mm/YYYY): ')
start_date = datetime.strptime(input_1,'%d/%m/%Y')
input_2 = input('End Date (dd/mm/YYYY): ')
end_date = datetime.strptime(input_2,'%d/%m/%Y')
search_string = input("Search Phrase: ")

# search
dataframe = dataframe[(dataframe[1] >= start_date) & (dataframe[1] <= end_date)]
dataframe = dataframe[dataframe[3].str.match(f'^.*{search_string}.*')]

#result
print(dataframe)
