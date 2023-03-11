import pandas as pd
import warnings
import numpy as np

season_dict = {'2014':'19','2015':'24','2016':'32','2017':'39',
               '2018':'44','2019':'51'}

fase_dict = {'regular':'1',
            'playoffs':'2',
            'total':'=on&phase%5B%5D=1&phase%5B%5D=2'}

seasons = ['2014','2015','2016','2017','2018','2019']

fases = ['regular','playoffs','total']

def get_placares(season, fase):
    
    if str(season) not in seasons:
        raise ValueError(str(season)+' não é um valor válido. Tente um de: "'+'", "'.join(seasons)+'".')
    
    if fase not in fases:
        raise ValueError(str(fase)+' não é um valor válido. Tente um de: "'+'", "'.join(fases)+'".')
    
    season2 = season_dict[str(season)]
    
    fase = fase_dict[fase]
    
    if fase!='=on&phase%5B%5D=1&phase%5B%5D=2': # total
        url = 'https://lnb.com.br/liga-ouro/tabela-de-jogos/?season%5B%5D='+season2+'&phase%5B%5D='+fase
    else:
        url = 'https://lnb.com.br/liga-ouro/tabela-de-jogos/?season%5B%5D='+season2
    
    df = pd.read_html(url)[0]
    
    df = df.drop(columns=['#','CASA','Unnamed: 15','GINÁSIO','RODADA'])
    df = df.dropna(how='all', axis=1)
    
    df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y  %H:%M')
    
    df = df.rename(columns={'TRANSMISSÃO':'GINASIO',
                            'FASE':'RODADA',
                           'CAMPEONATO':'FASE',
                           'Unnamed: 3':'EQUIPE CASA',
                           'Unnamed: 7':'EQUIPE VISITANTE'})
    
    df['Unnamed: 5'] = df['Unnamed: 5'].str.replace('  VER RELATÓRIO','')
    df['PLACAR CASA'] = df['Unnamed: 5'].str[:2]
    df['PLACAR VISITANTE'] = df['Unnamed: 5'].str[-2:]
    
    df['PLACAR CASA'] = df['PLACAR CASA'].apply(lambda x: np.nan if 'X' in x else x)
    df['PLACAR VISITANTE'] = df['PLACAR VISITANTE'].apply(lambda x: np.nan if 'X' in x else x)
    
    df = df.drop(columns=['Unnamed: 5'])
    
    df['VENCEDOR'] = np.where(df['PLACAR CASA']>df['PLACAR VISITANTE'],df['EQUIPE CASA'],df['EQUIPE VISITANTE'])
    
    df['VENCEDOR'] = np.where(df['PLACAR CASA']==np.nan, np.nan, df['VENCEDOR'])
    
    df['TEMPORADA'] = season
    
    df = df[['DATA','EQUIPE CASA','PLACAR CASA','PLACAR VISITANTE','EQUIPE VISITANTE',
            'VENCEDOR','RODADA','FASE','GINASIO','TEMPORADA']]
    
    return df

def get_classificacao(season):
    
    if str(season) not in seasons:
        raise ValueError(str(season)+' não é um valor válido. Tente um de: "'+'", "'.join(seasons)+'".')
    
    season2 = season_dict[str(season)]
    
    url = 'https://lnb.com.br/liga-ouro/?season='+season2
    
    df = pd.read_html(url)[0]
    
    df = df.iloc[::2].reset_index(drop=True)
    
    df = df.dropna(how='all', axis=1)
    
    df['EQUIPES'] = df['EQUIPES'].str[3:]
    df['TEMPORADA'] = season
    
    return df
