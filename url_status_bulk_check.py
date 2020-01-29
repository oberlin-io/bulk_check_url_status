'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

                                                                      888
                                                            .d8888b.  888888b.
                                                           d88'  '88b 888  '88b
                                                           888    888 888   888
joberlin@acr.org                                           Y88.  .88Y 888  d88P
oberlijhn@gmail.com                                         'Y8888Y'  888888P'


Takes Pandas dataframe, grabs the column named 'url', dedupes, gets URL status
code, joins codes to the dataframe, and returns the updated dataframe.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

import pandas as pd
import requests as req
import sys

def url_status(df):
    requests.packages.urllib3.disable_warnings()
        # Warning due to get() trying to verify certs.
    urls = df.url.unique().tolist()
    #
    statuses = list()
    for url in urls:
        try:
            response = req.get(url, verify=False)
                # If cert verify=True, SSL error fo rmy context,
                # but safer to try True.
            statuses.append(response.status_code)
        except:
            statuses.append(sys.exc_info()[1])
        #
    if len(urls) == len(statuses):
        url_status = pd.DataFrame({'url': urls, 'url_status': statuses})
        df = pd.merge(df, url_status, how='left', left_on='url', right_on='url')
        return df
    else:
        print('Error: Number of statuses different than URLs.')  
