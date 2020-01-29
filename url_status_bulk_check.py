'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                              888                           888
                    .d8888b.  8888888b.   .d8888b.   .d888b 888       88b8888b.
                   d88'  '88b 888   '88b d88'  '88b d88'    888  888  888'  '88b
                   888    888 888    888 8888888P'  888     888  888  888    888
                   Y88.  .88Y 888   .88Y Y88        888     888  888  888    888
                    'Y8888Y'  8888888Y'   'Y8888Y'  888     888  888  888    888

                                                               oberljn@gmail.com

Takes Pandas dataframe, grabs the column named 'url', dedupes, gets URL status
code, logs data as YAML, joins data to the dataframe, and returns the updated
dataframe.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

import pandas as pd
import requests as req
import sys

def url_status(df, verbose=True):
    with open('url_status_log.yaml', 'w') as f: f.write('---\n')
    req.packages.urllib3.disable_warnings()
        # Warning due to get() not verifying certs.
    urls = df.url.drop_duplicates().tolist()
    statuses = list()
    
    for url in urls:
        try:
            response = req.get(url, timeout=5, verify=False)
                # If cert verify=True, SSL error
            code = response.status_code
            exc = '~'
            statuses.append(code)
        except:
            exc = sys.exc_info()[1]
            code = '~'
            statuses.append(exc)
        
        obj_yaml = '{}:\n'.format( str(urls.index(url)) )
        obj_yaml += '  url: {}\n'.format(url)
        obj_yaml += '  code: {}\n'.format(code)
        obj_yaml += '  exception: {}\n'.format(exc)
        
        if verbose: print(obj_yaml)
        with open('url_status_log.yaml', 'a') as f: f.write(obj_yaml)
        
    with open('url_status_log.yaml', 'a') as f: f.write('...\n')
    
    if len(urls) == len(statuses):
        url_status = pd.DataFrame({'url': urls, 'url_status': statuses})
        df = pd.merge(df, url_status, how='left', left_on='url', right_on='url')
        return df
    else:
        print('Error: Number of statuses different than URLs.')
