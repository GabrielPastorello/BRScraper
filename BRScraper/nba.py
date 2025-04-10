import pandas as pd
import warnings
import re
from datetime import date

dict_teams = {'Utah Jazz':'UTA','Phoenix Suns':'PHO',
             'Philadelphia 76ers':'PHI','Brooklyn Nets':'BRK',
             'Denver Nuggets':'DEN','Los Angeles Clippers':'LAC',
             'Milwaukee Bucks':'MIL','Dallas Mavericks':'DAL',
             'Los Angeles Lakers':'LAL','Portland Trail Blazers':'POR',
             'Atlanta Hawks':'ATL','New York Knicks':'NYK',
             'Miami Heat':'MIA','Golden State Warriors':'GSW',
             'Memphis Grizzlies':'MEM','Boston Celtics':'BOS',
             'Washington Wizards':'WAS','Indiana Pacers':'IND',
             'Charlotte Hornets':'CHO','Charlotte Bobcats':'CHA',
             'San Antonio Spurs':'SAS','Chicago Bulls':'CHI',
             'New Orleans Pelicans':'NOP','Sacramento Kings':'SAC',
             'Toronto Raptors':'TOR','Minnesota Timberwolves':'MIN',
             'Cleveland Cavaliers':'CLE','Oklahoma City Thunder':'OKC',
             'Orlando Magic':'ORL','Detroit Pistons':'DET',
             'Houston Rockets':'HOU','New Jersey Nets':'NJN',
             'New Orleans Hornets':'NOH','Seattle SuperSonics':'SEA'}

def get_current_salaries(info='players'):
    
    values = ['players','teams']
    
    if info not in values:
        raise ValueError(str(info)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url_salary = ['https://www.basketball-reference.com/contracts/players.html', # players
                'https://www.basketball-reference.com/contracts/'] # teams

    if info=='players':
        df = pd.read_html(url_salary[0])[0]
        df.columns = df.columns.droplevel(0)
        df = df[(df['Player'].notna())&(df['Player']!='Player')].drop(columns=['Rk']).reset_index(drop=True)

    elif info=='teams':
        df = pd.read_html(url_salary[1])[0]
        df.columns = df.columns.droplevel(0)
        df = df.drop(columns=['Rk'])
        df = df.rename(columns={'Team':'Tm'})
        df['Tm'] = df['Tm'].replace(dict_teams)

        for col in df.columns:
            if col != 'Tm':
                df = df.rename(columns={col:'Team_'+col})
    
    return df

def get_stats(season, info='per_game', playoffs=False, rename=False):
    
    values = ['per_game','totals','advanced','per_36','per_100']
    
    if info not in values:
        raise ValueError(str(info)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    if playoffs:
        comp = 'playoffs'
    else:
        comp = 'leagues'
        
    url_stats = ['https://www.basketball-reference.com/'+comp+'/NBA_'+str(season)+'_per_game.html', # pergame
                'https://www.basketball-reference.com/'+comp+'/NBA_'+str(season)+'_totals.html', # total
                'https://www.basketball-reference.com/'+comp+'/NBA_'+str(season)+'_advanced.html', # advanced
                'https://www.basketball-reference.com/'+comp+'/NBA_'+str(season)+'_per_minute.html', # per 36 min
                'https://www.basketball-reference.com/'+comp+'/NBA_'+str(season)+'_per_poss.html', # per 100 poss
                ] 
    try:
        if info=='per_game':
            df = pd.read_html(url_stats[0])[0]
        elif info=='totals':
            df = pd.read_html(url_stats[1])[0]
        elif info=='advanced':
            df = pd.read_html(url_stats[2])[0]
            #df = df.drop(['Unnamed: 24','Unnamed: 19'], axis=1).reset_index(drop=True)
        elif info=='per_36':
            df = pd.read_html(url_stats[3])[0]
        elif info=='per_100':
            df = pd.read_html(url_stats[4])[0]
    except:
        raise ValueError(str(season)+' is not a valid season.')
            
    df = df[(df['Player'].notna())&(df['Player']!='Player')&(df['Player']!='League Average')].drop(['Rk'], axis=1).reset_index(drop=True)

    if rename:
        cols = ['Player','Pos','Age','Tm','G','GS']
        for column in df.columns:
            if column not in cols:
                new_column = column+'_'+info
                df = df.rename(columns={column:new_column})

    df['Season'] = str(int(str(season))-1)+'-'+str(season)[-2:]
        
    return df

def get_standings(season, info='total'):
    
    values = ['total','east','west']
    
    if info not in values:
        raise ValueError(str(info)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url = 'https://www.basketball-reference.com/leagues/NBA_'+str(season)+'_standings.html'
    
    try:
        df = pd.read_html(url)
    except:
        raise ValueError(str(season)+' is not a valid season.')
        
    if info=='total':
        df1 = df[0]
        df1 = df1.rename(columns={'Eastern Conference':'Tm'})
        df2 = df[1]
        df2 = df2.rename(columns={'Western Conference':'Tm'})
        df = pd.concat([df1,df2],ignore_index=True).drop(columns=['GB'])
    elif info=='east':
        df = df[0]
        df = df.rename(columns={'Eastern Conference':'Tm'})
    elif info=='west':
        df = df[1]
        df = df.rename(columns={'Western Conference':'Tm'})

    df = df.sort_values(by='W/L%', ascending=False).reset_index(drop=True)

    df['Seed'] = df.index+1    
    
    return df

def get_general_info():
    
    url = 'https://www.basketball-reference.com/leagues/'
    
    df = pd.read_html(url)[0]
    df.columns = df.columns.droplevel(0)
    
    return df

def get_season_leaders(season, info, n=10, playoffs=False, per_game=False):
    
    values = ['pts','reb','oreb','dreb','ast','stl','blk','fg%','ft%','3pt%','2pt%','efg%','ts%','fg','fga',
               '2p','2pa','3p','3pa','fgm','ft','fta','min','tov','pf','per','ws','ows','dws','ws48','bpm',
               'obpm','dbpm','vorp','ortg','drtg','usg%','trb%','orb%','ast%','drb%','stl%','blk%','tov%']
    
    if info not in values:
        raise ValueError(str(info)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    if n<=0:
        raise ValueError(str(n)+' is not a valid value. Try a value bigger than 0.')
    elif n>20 and playoffs==False:
        warnings.warn('WARNING: maximum of 20 players for regular season, selecting 20')
    elif n>10 and playoffs==True:
        warnings.warn('WARNING: maximum of 10 players for playoffs, selecting 10')
    
    if playoffs:
        comp = 'playoffs'
    else:
        comp = 'leagues'
    
    url='https://www.basketball-reference.com/'+comp+'/NBA_'+str(season)+'_leaders.html'
    
    try:
        df = pd.read_html(url)
    except:
        raise ValueError(str(season)+' is not a valid season.')
        
    if info=='pts':
        if per_game:
            df = df[1]
        else:
            df = df[0]
    elif info=='reb':
        if per_game:
            df = df[3]
        else:
            df = df[2]
    elif info=='oreb':
        df = df[4]
        if per_game:
            warnings.warn('WARNING: Only total info for '+info)
    elif info=='dreb':
        df = df[5]
        if per_game:
            warnings.warn('WARNING: Only total info for '+info)
    elif info=='ast':
        if per_game:
            df = df[7]
        else:
            df = df[6]
    elif info=='stl':
        if per_game:
            df = df[9]
        else:
            df = df[8]
    elif info=='blk':
        if per_game:
            df = df[11]
        else:
            df = df[10]
    elif info=='fg%':
        df = df[12]
    elif info=='ft%':
        df = df[13]
    elif info=='3pt%':
        df = df[14]
    elif info=='2pt%':
        df = df[15]
    elif info=='efg%':
        df = df[16]
    elif info=='ts%':
        df = df[17]
    elif info=='fg':
        df = df[18]
    elif info=='fga':
        df = df[19]
    elif info=='2p':
        df = df[20]
    elif info=='2pa':
        df = df[21]
    elif info=='3p':
        df = df[22]
    elif info=='3pa':
        df = df[23]
    elif info=='fgm':
        df = df[24]            
    elif info=='ft':
        df = df[25]            
    elif info=='fta':
        df = df[26]
    elif info=='min':
        if per_game:
            df = df[28]
        else:
            df = df[27]
    elif info=='tov':
        df = df[29]
        if per_game:
            warnings.warn('WARNING: Only total info for '+info)
    elif info=='pf':
        df = df[30]
        if per_game:
            warnings.warn('WARNING: Only total info for '+info)
    elif info=='per':
        df = df[31]
    elif info=='ws':
        df = df[32]
    elif info=='ows':
        df = df[33]
    elif info=='dws':
        df = df[34]
    elif info=='ws48':
        df = df[35]
    elif info=='bpm':
        df = df[36]
    elif info=='obpm':
        df = df[37]
    elif info=='dbpm':
        df = df[38]
    elif info=='vorp':
        df = df[39]
    elif info=='ortg':
        df = df[40]
    elif info=='drtg':
        df = df[41]
    elif info=='usg%':
        df = df[42]
    elif info=='trb%':
        df = df[43]
    elif info=='orb%':
        df = df[44]
    elif info=='ast%':
        df = df[45]
    elif info=='drb%':
        df = df[46]
    elif info=='stl%':
        df = df[47]
    elif info=='blk%':
        df = df[48]
    elif info=='tov%':
        df = df[49]

    df = df.drop(columns=[0])
    
    df.columns = ['Player',info.upper()]
    
    df['Rank'] = df.index+1
    df = df[df['Rank']<=n]
    
    df['Tm'] = df['Player'].str[-3:]
    df['Player'] = df['Player'].str[:-5]
    
    return df

def get_coach_data(season):
    
    url = 'https://www.basketball-reference.com/leagues/NBA_'+str(season)+'_coaches.html'
    
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(str(season)+' is not a valid season.')
        
    df.columns = df.columns.droplevel([0,1])
    df = df.drop(columns=['Unnamed: 2_level_2','Unnamed: 5_level_2','Unnamed: 16_level_2'])
    
    df.columns = ['Coach','Tm','Seasons Franchise','Seasons Career',
                  'RS_S_G','RS_S_W','RS_S_L','RS_FR_G','RS_FR_W','RS_FR_L',
                  'RS_CA_G','RS_CA_W','RS_CA_L','RS_CA_W%',
                  'PL_S_G','PL_S_W','PL_S_L','PL_FR_G','PL_FR_W','PL_FR_L',
                  'PL_CA_G','PL_CA_W','PL_CA_L']
        
    return df

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

        url = 'https://www.basketball-reference.com/players/'+first_l+'/'+name_url+'01.html'
    except:
        raise ValueError(name+''' is not in a valid name format.
                        Valid names would be "LeBron James", "lebron james" or "LEBRON JAMES" for example.''')
                         
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(name+' is not a valid name. Check for mispelling errors or if that players exists.')
                         
    df = df.dropna(how='all', axis=0)
    
    num = df[df['Season']=='Career'].index[0]
    
    df = df.iloc[:num]
    
    return df

def get_draft_info(season):
    
    url = 'https://www.basketball-reference.com/draft/NBA_'+str(season)+'.html'
    
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(str(season)+' is not a valid season.')
    
    df.columns = df.columns.droplevel(0)
    df = df[(df['Tm'].notna())&(df['Player']!='Player')].drop(columns=['Rk']).reset_index(drop=True)
    
    return df

def get_playoffs_probs(conf):
    
    values = ['east','west']
    
    if conf not in values:
        raise ValueError(str(conf)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url = 'https://www.basketball-reference.com/friv/playoff_prob.html'
    
    df = pd.read_html(url)
    
    if conf == 'east':
        df = df[0]
    elif conf == 'west':
        df = df[1]
        
    df.columns = df.columns.droplevel(0)
    df = df.dropna(how='all', axis=1)
    df = df[df['W'].notna()].drop(columns=['Rk']).reset_index(drop=True)
    
    return df

def get_rookies(season):
    
    url = 'https://www.basketball-reference.com/leagues/NBA_'+str(season)+'_rookies.html'
    
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError(str(season)+' is not a valid season.')
        
    df.columns = df.columns.droplevel(0)
    df = df[(df['Player'].notna())&(df['Player']!='Player')].drop(['Rk'], axis=1).reset_index(drop=True)
    
    return df

def get_birthdays():
    
    today = date.today()    
    month = today.month
    day = today.day
    
    url = 'https://www.basketball-reference.com/friv/birthdays.fcgi?month='+str(month)+'&day='+str(day)
    
    try:
        df = pd.read_html(url)[0]
    except:
        raise ValueError('It seems there are no birthdays today :(')
    
    df.columns = df.columns.droplevel(0)
    df = df.dropna(how='all', axis=1)
    df = df[df['Player'].notna()].drop(columns=['Rk']).reset_index(drop=True)
    
    return df

def get_awards(award):
    
    values = ['mvp','roy','dpoy','smoy','tmoy','mip','citizenship','finals_mvp','playoffs_mvp',
             'wcf_mvp','ecf_mvp','all_star_mvp','cpoy','player_of_the_seeding_games','tsn_mvp',
             'tsn_roy','hustle','social_justice','coy','nbca_coy','eoy']
    
    if award not in values:
        raise ValueError(str(award)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')
    
    url = 'https://www.basketball-reference.com/awards/'+award+'.html'

    df = pd.read_html(url)[0]
    
    if award not in ['eoy','coy','nbca_coy']:
        df.columns = df.columns.droplevel(0)
        df = df.dropna(how='all', axis=0) 
        df = df.dropna(how='all', axis=1)  
        df = df[(df['Player'].notna())&(df['Player']!='Player')].reset_index(drop=True)
    
    return df

def get_award_votings(award:str, season:int)->pd.DataFrame:
    """
    Get award voting data for a given award and season.
    Parameters
    ----------
    award : str, optional
        The award to get voting data for.
    season : int, optional
        The season to get voting data for.
    
    Returns
    -------
    pd.DataFrame
        A dataframe containing the voting data for the given award and season.
    """

    values = [
        'mvp'
        ,'roy'
        ,'all_nba'
        ,'all_defense'
    ]

    # Check if award is valid
    if award not in values:
        raise ValueError(str(award)+' is not a valid value. Try one of: "'+'", "'.join(values)+'".')

    # Check if season is valid
    if season < 1977:
        raise ValueError(str(season)+' is not a valid season. Try a value greater or equal than 1977.')

    # Build url
    url = 'https://www.basketball-reference.com/awards/awards_'+str(season)+'.html'

    # Get the index of the award
    if award == 'mvp':
        index = 0
    elif award == 'roy':
        index = 1
    elif award == 'all_nba':
        index = 2
    elif award == 'all_defense':
        index = 3

    # Read table from url
    try:
        df = pd.read_html(url)[index]
    except Exception as e:
        raise ValueError(str(season)+' is not a valid season.') from e

    # Remove multiindex level 0 where str contains Unnamed
    df.columns  = df.columns.map(lambda x: '_'.join(x) if 'Unnamed' not in x[0] else x[1]).str.strip('_')    

    # Remove rows where Player is NaN
    df = df[df['Player'].notna()].reset_index(drop=True)

    return df
