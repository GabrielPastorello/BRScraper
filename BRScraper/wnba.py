import pandas as pd
import warnings
import re

def get_player_stats(name):
    
    name2 = re.sub('[^a-zA-Z0-9 \n\.]', '', name)

    if name2!=name:
        raise ValueError(name+' has special characters and is not a valid name. Try replacing the special characters.')

    try:
        name_url = name.lower().strip().split(' ')

        if len(name_url[1])>=5:
            len_name = 5
        else:
            len_name = len(name_url[1])

        name_url = name_url[1][:len_name] + name_url[0][:2]

        first_l = name.strip().split(' ')[1][0].lower()

        url = 'https://www.basketball-reference.com/wnba/players/'+first_l+'/'+name_url+'01w.html'
    except:
        raise ValueError(name+''' is not in a valid name format.
                        Valid names would be "Sabrina Ionescu", "sabrina ionescu" or "SABRINA IONESCU" for example.''')
                         
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(name+' is not a valid name. Check for mispelling errors or if that players exists.')
                         
    df = df.dropna(how='all', axis=0)
    
    num = df[df['Year']=='Career'].index[0]
    
    df = df.iloc[:num]
    
    return df

def get_standings(season, info='total'):
    
    values = ['total','east','west']
    
    if info not in values:
        raise ValueError(str(info)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url = 'https://www.basketball-reference.com/wnba/years/'+str(season)+'.html'
    
    try:
        df = pd.read_html(url)
    except:
        raise ValueError(str(season)+' is not a valid season.')

    if info=='total':
        df = df[0]
    elif info=='east':
        df = df[1]
        df = df.rename(columns={'Eastern Conference':'Tm'})
    elif info=='west':
        df = df[2]
        df = df.rename(columns={'Western Conference':'Tm'})
            
    df = df.sort_values(by='W/L%', ascending=False).reset_index(drop=True)

    df['Seed'] = df.index+1    
    
    return df

def get_general_info():
    
    url = 'https://www.basketball-reference.com/wnba/playoffs/'
    
    df = pd.read_html(url)[0]
    df.columns = df.columns.droplevel(0)
    df = df.dropna(how='all', axis=1)
    
    return df

def get_draft_info(season):
    
    url = 'https://www.basketball-reference.com/wnba/draft/'+str(season)+'.html'
    
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(str(season)+' is not a valid season.')
    
    df.columns = df.columns.droplevel(0)
    df = df[(df['Team'].notna())&(df['MP']!='Per Game')&(df['Player']!='Player')].reset_index(drop=True)
    df = df.dropna(how='all', axis=1)
    
    return df

def get_awards(award):
    
    values = ['mvp','roy','dpoy','swoy','mip','all_wnba','all_rookie','all_defense','coy',
              'fin_mvp','all_star_mvp','sportsmanship','community_assist','eoy']
    
    if award not in values:
        raise ValueError(str(award)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url = 'https://www.basketball-reference.com/wnba/awards/'+award+'.html'

    df = pd.read_html(url)[0]
    
    if award not in ['eoy','coy']:
        df.columns = df.columns.droplevel(0)
        df = df.dropna(how='all', axis=0) 
        df = df.dropna(how='all', axis=1)  
        df = df[(df['Player'].notna())&(df['Player']!='Player')].reset_index(drop=True)
    
    return df
