import pandas as pd
import warnings

def get_awards(award):
    
    values = ['mvp','roy','dpoy','mip','ipoy','all_gleague','all_rookie','all_defense','sc_mvp']
    
    if award not in values:
        raise ValueError(str(award)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url = 'https://www.basketball-reference.com/gleague/awards/'+award+'.html'

    df = pd.read_html(url)[0]

    df.columns = df.columns.droplevel(0)
    df = df.dropna(how='all', axis=0) 
    df = df.dropna(how='all', axis=1)  
    df = df[(df['Player'].notna())&(df['Player']!='Player')].reset_index(drop=True)
    
    return df

def get_standings(season, info='total', showcase=False):
    
    values = ['total','east','west']
    
    if info not in values:
        raise ValueError(str(info)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url = 'https://www.basketball-reference.com/gleague/years/'+str(season)+'.html'
    
    try:
        df = pd.read_html(url)
    except:
        raise ValueError(str(season)+' is not a valid season.')
    
    if showcase==False:
        if info=='total':
            df1 = df[0]
            df1 = df1.rename(columns={'Eastern':'Tm'})
            df2 = df[1]
            df2 = df2.rename(columns={'Western':'Tm'})
            df = pd.concat([df1,df2],ignore_index=True).drop(columns=['GB'])
        elif info=='east':
            df = df[0]
            df = df.rename(columns={'Eastern':'Tm'})
        elif info=='west':
            df = df[1]
            df = df.rename(columns={'Western':'Tm'})
    elif showcase==True:
        if info=='total':
            df1 = df[2]
            df1 = df1.rename(columns={'Eastern':'Tm'})
            df2 = df[3]
            df2 = df2.rename(columns={'Western':'Tm'})
            df = pd.concat([df1,df2],ignore_index=True).drop(columns=['GB'])
        elif info=='east':
            df = df[2]
            df = df.rename(columns={'Eastern':'Tm'})
        elif info=='west':
            df = df[3]
            df = df.rename(columns={'Western':'Tm'})
            
    df = df.sort_values(by='W/L%', ascending=False).reset_index(drop=True)

    df['Seed'] = df.index+1    
    
    return df
