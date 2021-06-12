import requests
import pandas as pd
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()
pp = PrettyPrinter()
api_Key = 'UnZRD0DwrqAw3ehWKILATTh1xgB4oo8ZcUeT2jpl'
def fetchAPOD():
    
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    date = '2021-06-11'
    params = {
      'api_key':api_Key,
      'date':date,
      'hd':'True'
       }
    response = requests.get(URL_APOD,params=params).json()
    #pp.pprint(response)
    print(type(response))
    #print(response)
    data = pd.DataFrame.from_dict(response,orient ='index')
    print(data)
    data.to_excel("output1.xlsx")


def fetchAst():
    
    URL_NEO = "https://api.nasa.gov/neo/rest/v1/neo/browse/"
    date = '2021-06-12'
    params = {
      'api_key':api_Key,
      'date':date,
      'hd':'True'
       }
    response1 = requests.get(URL_NEO,params=params).json()
    #pp.pprint(response1)
    print(type(response1))
    print(response1)
    data = pd.DataFrame.from_dict(response1,orient ='index')
    print(data)
    data.to_excel("output12.xlsx")

fetchAst()
fetchAPOD()
