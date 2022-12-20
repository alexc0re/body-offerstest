from links.googleFetch import linksDF
import pandas as pd



def list_nan_cleaner(the_list):   # removes empty values from the list

    cleanedList = [x for x in the_list if pd.notnull(x)]
    return cleanedList


# getting offer URL lists from the corresponding columns of the Google File
test_links = linksDF['test'] #сюда название рядка
linksListRaw = test_links.tolist()
linksList = list_nan_cleaner(linksListRaw)



#SSRl = linksDF['SSRlinks']
#SSRlraw = SSRl.tolist()
#ssr_links = list_nan_cleaner(SSRlraw)


