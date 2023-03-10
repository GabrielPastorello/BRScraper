import pandas as pd
import warnings
import re

def get_player_stats(name):
    
    name2 = re.sub('[^a-zA-Z0-9 \n\.]', '', name)

    if name2!=name:
        raise ValueError(name+' has special characters and is not a valid name. Try replacing the special characters.')
    
    try:
        name_url = name.lower().strip().replace(' ','-')

        url = 'https://www.basketball-reference.com/international/players/'+name_url+'-1.html'
    except:
        raise ValueError(name+''' is not in a valid name format.
                        Valid names would be "Bruno Caboclo", 'bruno caboclo' or "BRUNO CABOCLO" for example.''')
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(name+' is not a valid name. Check for mispelling errors or if that players exists.')
                         
    df = df.dropna(how='all', axis=0)
    
    df = df.iloc[:-1]
    
    df = df.rename(columns={'Unnamed: 3':'Country'})
    
    return df

def get_mvps():

    url = 'https://www.basketball-reference.com/international/awards/mvp.html'

    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(name+' is not a valid name. Check for mispelling errors or if that players exists.')

    df.columns = df.columns.droplevel(0)
    df = df.dropna(how='all', axis=0)  
    df = df[(df['Player'].notna())&(df['Player']!='Player')].reset_index(drop=True)
    
    return df
