# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:02:05 2019

@author: Ibrahim

This tool to compare between Stack overflow developers survey in 2017 and 2019. 
It can be upgraded later on to compare with different years, so the user allows us to enter which year to compare. 
The author selected the language, database, and platform to be compared because those three questions are the most important for any developer.
"""

# Importing Libraries
import pandas as pd
from collections import Counter
#  Importing Libraraies for data Visualization
#  https://seaborn.pydata.org/tutorial.html
import matplotlib.pyplot as plt
import seaborn as sns

# Reading Stackoverflow survey data for 2017 and 2019
df_2017 = pd.read_csv('2017/survey_results_public.csv')
df_2019 = pd.read_csv('2019/survey_results_public.csv')

# Reading User Variables 
country_2017 = input('Enter the Country from 2017 Stackover flow survey?')
gender_2017 =  input('Enter the Gender from 2017 Stackover flow survey? [Male, Female]')
country_2019 = country_2017
gender_2019 =  input('Enter the Gender from 2019 Stackover flow survey? [Man, Women]')

# Filter the data based on the entered country and gender. The function will return clean dataframe 
# based on the filters
# dropna function used to clean and remove the data. 
# https://www.geeksforgeeks.org/python-pandas-dataframe-dropna/

def myfilters(mydata, column__country_filter, country,column_gender_filter, gender, columns):
    clean_data = mydata        
    for column in columns: 
        clean_data = clean_data[clean_data[column__country_filter] == country].dropna(subset=[column])        
    for column in columns: 
        clean_data = clean_data[clean_data[column_gender_filter] == gender].dropna(subset=[column])        
    return clean_data

# Filter the dataframe by country and gender and create new dataframes with the searched fields (Language, Database, Platform)
# Apply filters and reflect this to new dataframes
stackoverflow_langugage_2017 = myfilters(df_2017, 'Country', country_2017 , 'Gender', gender_2017, ['HaveWorkedLanguage', 'WantWorkLanguage'])
stackoverflow_langugage_2019 = myfilters(df_2019, 'Country', country_2019, 'Gender', gender_2019, ['LanguageWorkedWith', 'LanguageDesireNextYear'])
stackoverflow_database_2017 = myfilters(df_2017, 'Country', country_2017 , 'Gender', gender_2017, ['HaveWorkedDatabase', 'WantWorkDatabase'])
stackoverflow_database_2019 = myfilters(df_2019, 'Country', country_2019, 'Gender', gender_2019, ['DatabaseWorkedWith', 'DatabaseDesireNextYear'])
stackoverflow_platform_2017 = myfilters(df_2017, 'Country', country_2017 , 'Gender', gender_2017, ['HaveWorkedPlatform', 'WantWorkPlatform'])
stackoverflow_platform_2019 = myfilters(df_2019, 'Country', country_2019, 'Gender', gender_2019, ['PlatformWorkedWith', 'PlatformDesireNextYear'])


# Clean the data by using splitting by delimiater 
# https://cmdlinetips.com/2018/11/how-to-split-a-text-column-in-pandas/
# https://www.geeksforgeeks.org/python-pandas-split-strings-into-two-list-columns-using-str-split/
# the below function will split the data in each identified column as they entered in the CSV by semi column 
# The function return a series of index and data ( two columns)

def splitingfunction(df, column):
    df_copy = df
    column_series = df_copy[column].apply(lambda x: x.split(';'))    
    return column_series

# Apply the function for language, database and platform
worked_lang_2017 = splitingfunction(stackoverflow_langugage_2017, 'HaveWorkedLanguage')
wanted_lang_2017 = splitingfunction(stackoverflow_langugage_2017, 'WantWorkLanguage')
worked_lang_2019 = splitingfunction(stackoverflow_langugage_2019, 'LanguageWorkedWith')
wanted_lang_2019 = splitingfunction(stackoverflow_langugage_2019, 'LanguageDesireNextYear')

worked_database_2017 = splitingfunction(stackoverflow_database_2017, 'HaveWorkedDatabase')
wanted_database_2017 = splitingfunction(stackoverflow_database_2017, 'WantWorkDatabase')
worked_database_2019 = splitingfunction(stackoverflow_database_2019, 'DatabaseWorkedWith')
wanted_database_2019 = splitingfunction(stackoverflow_database_2019, 'DatabaseDesireNextYear')

worked_platform_2017 = splitingfunction(stackoverflow_platform_2017, 'HaveWorkedPlatform')
wanted_platform_2017 = splitingfunction(stackoverflow_platform_2017, 'WantWorkPlatform')
worked_platform_2019 = splitingfunction(stackoverflow_platform_2019, 'PlatformWorkedWith')
wanted_platform_2019 = splitingfunction(stackoverflow_platform_2019, 'PlatformDesireNextYear')


# https://www.geeksforgeeks.org/python-convert-a-nested-list-into-a-flat-list/
# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
# The task is to convert a nested list into a single list in python i.e no matter how many 
# levels of nesting is there in python list, all the nested has to be removed in order to convert
# it to a single containing all the values of all the lists inside the outermost brackets but without any brackets inside.
def tonestedlist(array_list):
    objects = []
    for row in array_list:
        for obj in row:
            objects.append(obj.strip())
    return objects

# Apply the conversation of nested lists to flat list for all column series
list_worked_languages_2017 = tonestedlist(worked_lang_2017)
list_wanted_languages_2017 = tonestedlist(wanted_lang_2017)
list_worked_languages_2019 = tonestedlist(worked_lang_2019)
list_wanted_languages_2019 = tonestedlist(wanted_lang_2019)


list_worked_database_2017 = tonestedlist(worked_database_2017)
list_wanted_database_2017 = tonestedlist(wanted_database_2017)
list_worked_database_2019 = tonestedlist(worked_database_2019)
list_wanted_database_2019 = tonestedlist(worked_database_2019)


list_worked_platform_2017 = tonestedlist(worked_platform_2017)
list_wanted_platform_2017 = tonestedlist(worked_platform_2017)
list_worked_platform_2019 = tonestedlist(worked_platform_2019)
list_wanted_platform_2019 = tonestedlist(worked_platform_2019)

# Dynammic Function to group list and count the values and dict 
# https://stackoverflow.com/questions/11068986/how-to-convert-counter-object-to-dict
# https://docs.python.org/2/library/collections.html
# A Counter is a dict subclass for counting hashable objects. It is an unordered collection 
# where elements are stored as dictionary keys and their counts are stored as dictionary values. 
# Counts are allowed to be any integer value including zero or negative counts. 
# The Counter class is similar to bags or multisets in other languages.
def create_new_pair(data_list, year, my_label):
    new_pair_list = dict(Counter(data_list))
    new_pair_dict = [{my_label:key, 'Count': value, 'Year': year} for key, value in new_pair_list.items()]
    return new_pair_dict

# Apply the grouping for languages, database and platforms
dict_worked_languages_2017 = create_new_pair(list_worked_languages_2017, '2017','Programming Language')
dict_wanted_languages_2017 = create_new_pair(list_wanted_languages_2017, '2017','Programming Language')
dict_worked_languages_2019 = create_new_pair(list_worked_languages_2019, '2019','Programming Language')
dict_wanted_languages_2019 = create_new_pair(list_wanted_languages_2019, '2019','Programming Language')

dict_worked_database_2017 = create_new_pair(list_worked_database_2017, '2017','Database Engine')
dict_wanted_database_2017 = create_new_pair(list_wanted_database_2017, '2017','Database Engine')
dict_worked_database_2019 = create_new_pair(list_worked_database_2019, '2019','Database Engine')
dict_wanted_database_2019 = create_new_pair(list_wanted_database_2019, '2019','Database Engine')

dict_worked_platforms_2017 = create_new_pair(list_worked_platform_2017, '2017','Platform Types')
dict_wanted_platforms_2017 = create_new_pair(list_wanted_platform_2017, '2017','Platform Types')
dict_worked_platforms_2019 = create_new_pair(list_worked_platform_2019, '2019','Platform Types')
dict_wanted_platforms_2019 = create_new_pair(list_wanted_platform_2019, '2019','Platform Types')


# Create dataframe and append them in one dataframe to be used, it will include Count, Year, Type such as language, platform or database
# https://www.geeksforgeeks.org/python-pandas-dataframe-append/
# This function return the top 6 rows in each dataframe, so for language, it will return the top 6 language in 2017 and top 6 in 2019
def create_final_dataframe(data_dicts):
    df1 = pd.DataFrame(data_dicts[0]).sort_values(by=['Count']).head(6)
    df2 = pd.DataFrame(data_dicts[1]).sort_values(by=['Count']).head(6)
    my_final_dataframe = df1.append(df2)
    return my_final_dataframe

# Apply the creation function of dataframes. 
worked_languages = create_final_dataframe([dict_worked_languages_2017, dict_worked_languages_2019])
wanted_languages = create_final_dataframe([dict_wanted_languages_2017, dict_wanted_languages_2019])

worked_database = create_final_dataframe([dict_worked_database_2017, dict_worked_database_2019])
wanted_database = create_final_dataframe([dict_wanted_database_2017, dict_wanted_database_2019])

worked_platforms = create_final_dataframe([dict_worked_platforms_2017, dict_worked_platforms_2019])
wanted_platforms = create_final_dataframe([dict_wanted_platforms_2017, dict_wanted_platforms_2019])

print('Now, Select the area of comparision between two years (2017,2019) and based on the inputed data mainly Country, Gender which entered before')
print('Select your option to compare')


def my_visualization(my_dataframe, my_label):
    plt.figure(figsize=(14,8))    
    g = sns.barplot(x = 'Count',
            y = my_label,
            hue = 'Year',
            data = my_dataframe)
    # I am trying to show the value of each bar, but it generate a problems. so this is another area of improvement the charts. 
    '''for index, row in my_dataframe.iterrows():
        g.text(row.name,row['Programming Language'], round(row['Count'],2), color='black', ha="center")
        print(row['Programming Language'])
        print(row['Count'])'''
    
    plt.xlabel('Count', fontsize = 20)
    plt.ylabel(my_label, fontsize = 20)
    plt.legend(fontsize='large', title_fontsize='30')
    plt.title('Comparision between 2017 & 2019 based on ' + country_2017  , size = 20)
    plt.show()
    
def my_menu():
    print('Select your option to compare')
    print('1. Programming Language Wanted in 2017 & 2019')
    print('2. Programming Language Worked and desire to work in 2017 & 2019')
    print('3. Database Engine Wanted in 2017 & 2019')
    print('4. Database Engine Worked and desire to work in 2017 & 2019')
    print('5. Platforms Wanted in 2017 & 2019')
    print('6. Platforms Worked and desire to work  in 2017 & 2019')
    print('7. Return to select another choice')
    print('8. EXIT the tool')
    
    user_input = input("Enter the number")
    if user_input == "1" :
        my_visualization(worked_languages,'Programming Language')
        my_menu()
    elif user_input == "2" :
        my_visualization(wanted_languages,'Programming Language')
        my_menu()
    elif user_input == "3" :
        my_visualization(worked_database,'Database Engine')
        my_menu()
    elif user_input == "4" :
        my_visualization(wanted_database,'Database Engine')
        my_menu()
    elif user_input == "5" :
        my_visualization(worked_platforms,'Platform Types')
        my_menu()
    elif user_input == "6" :
        my_visualization(wanted_platforms,'Platform Types')
        my_menu()
    elif user_input == "7" :
        my_menu()
    elif user_input == "8" :
        print('Thank you for using this tool')
    else:
        print('Wrong Entry')
        my_menu()
    
my_menu()



 




