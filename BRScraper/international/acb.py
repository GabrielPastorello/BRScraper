import pandas as pd
import warnings

def get_stats(season, info='per_game', rename=False):
    
    values = ['per_game','totals','per_36']
    
    if info not in values:
        raise ValueError(str(info)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url_stats = ['https://www.basketball-reference.com/international/spain-liga-acb/'+str(season)+'_per_game.html', # pergame
                'https://www.basketball-reference.com/international/spain-liga-acb/'+str(season)+'_totals.html', # total
                'https://www.basketball-reference.com/international/spain-liga-acb/'+str(season)+'_per_minute.html', # per 36 min
                ] 
    try:
        if info=='per_game':
            df = pd.read_html(url_stats[0])[0]
        elif info=='totals':
            df = pd.read_html(url_stats[1])[0]
        elif info=='per_36':
            df = pd.read_html(url_stats[2])[0]
    except:
        raise ValueError(str(season)+' is not a valid season.')
            
    df = df[(df['Player'].notna())&(df['Player']!='Player')].reset_index(drop=True)

    if rename:
        cols = ['Player','Team','G']
        for column in df.columns:
            if column not in cols:
                new_column = column+'_'+info
                df = df.rename(columns={column:new_column})

    df['Season'] = str(int(str(season))-1)+'-'+str(season)[-2:]
        
    return df

def get_standings(season):
    
    url = 'https://www.basketball-reference.com/international/spain-liga-acb/'+str(season)+'.html'
    
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(str(season)+' is not a valid season.')
    
    df = df.rename(columns={'Unnamed: 0_level_1':'Team'})
    df.columns = df.columns.droplevel(0)
    df['Seed'] = df.index+1    
    
    return df
