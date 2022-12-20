import pandas as pd
from linksList import test_links


linkList = {
            'test_links': pd.Series(test_links)}


linksDF = pd.DataFrame(linkList)
print(linksDF)
linksDF.to_csv('links.csv')