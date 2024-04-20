import pandas as pd
import warnings
import numpy as np

season_dict = {'2008-09':'1','2009-10':'2','2010-11':'3','2011-12':'4',
                 '2012-13':'8','2013-14':'15','2014-15':'20','2015-16':'27',
                 '2016-17':'34','2017-18':'41','2018-19':'47','2019-20':'54',
                 '2020-21':'59','2021-22':'63','2022-23':'71','2023-24':'80'}

fase_dict = {'regular':'%5B%5D=1',
            'playoffs':'%5B%5D=2',
            'total':'=on&phase%5B%5D=1&phase%5B%5D=2'}


sofrido_dict = {False:'0',True:'1'} # só muda p/times

seasons = ['2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16',
            '2016-17','2017-18','2018-19','2019-20','2020-21','2021-22','2022-23','2023-24']

fases = ['regular','playoffs','total']

categs = ['cestinhas','rebotes','assistencias','arremessos','bolas-recuperadas','tocos',
        'erros','eficiencia','duplos-duplos','enterradas']

tipos = ['avg','sum']

quems = ['athletes','teams']

sofridos = [True,False]

def get_stats(season, fase, categ, tipo='avg', quem='athletes', sofrido=False):

    if season not in seasons:
        raise ValueError(str(season)+' não é um valor válido. Tente um de: "'+'", "'.join(seasons)+'".')
    
    if fase not in fases:
        raise ValueError(str(fase)+' não é um valor válido. Tente um de: "'+'", "'.join(fases)+'".')
    
    if categ not in categs:
        raise ValueError(str(categ)+' não é um valor válido. Tente um de: "'+'", "'.join(categs)+'".')
        
    if tipo not in tipos:
        raise ValueError(str(tipo)+' não é um valor válido. Tente um de: "'+'", "'.join(tipos)+'".')
        
    if quem not in quems:
        raise ValueError(str(quem)+' não é um valor válido. Tente um de: "'+'", "'.join(quems)+'".')

    if sofrido not in sofridos:
        raise ValueError(str(sofrido)+' não é um valor válido. Tente um de: '+', '.join(sofridos)+'".')
    
    season2 = season_dict[season]
    
    sofrido = sofrido_dict[sofrido]
    
    fase = fase_dict[fase]
    
    url = 'https://lnb.com.br/nbb/estatisticas/'+categ+'/?aggr='+tipo+'&type='+quem+'&suffered_rule='+sofrido+'&season%5B%5D='+season2+'&phase'+fase

    df = pd.read_html(url)[0]

    if quem=='athletes':
        df['Camisa'] = df['Jogador'].str.split(' #').str[1]
        df['Jogador'] = df['Jogador'].str.split(' #').str[0]

    df = df.drop(columns=['Pos.'])
        
    df['Temporada'] = season                  
    
    return df

def get_classificacao(season):
    
    if season not in seasons:
        raise ValueError(str(season)+' não é um valor válido. Tente um de: "'+'", "'.join(seasons)+'".')
    
    season2 = season_dict[season]
    
    url = 'https://lnb.com.br/nbb/?season='+season2
    
    df = pd.read_html(url)[0]
    
    df = df.iloc[::2].reset_index(drop=True)
    
    df = df.dropna(how='all', axis=1)
    
    df['EQUIPES'] = df['EQUIPES'].str[3:]
    df['TEMPORADA'] = season
    
    return df

def get_placares(season, fase):
    
    if season not in seasons:
        raise ValueError(str(season)+' não é um valor válido. Tente um de: "'+'", "'.join(seasons)+'".')
    
    if fase not in fases:
        raise ValueError(str(fase)+' não é um valor válido. Tente um de: "'+'", "'.join(fases)+'".')
    
    season2 = season_dict[season]
    
    fase = fase_dict[fase]
    
    if fase!='=on&phase%5B%5D=1&phase%5B%5D=2': # total
        url = 'https://lnb.com.br/nbb/tabela-de-jogos/?season%5B%5D='+season2+'&phase'+fase
    else:
        url = 'https://lnb.com.br/nbb/tabela-de-jogos/?season%5B%5D='+season2
    
    df = pd.read_html(url)[0]
    
    try:
        if season!='2008-09':
            df = df.drop(columns=['#','CASA','Unnamed: 15','GINÁSIO','RODADA'])
        else:
            df = df.drop(columns=['#','CASA','Unnamed: 14','GINÁSIO','RODADA'])
        df = df.dropna(how='all', axis=1)
    except:
        raise ValueError('Provavelmente essa temporada ainda não chegou aos playoffs. Tente uma anterior.')
    
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
    
    if season!='2008-09':
        df = df[['DATA','EQUIPE CASA','PLACAR CASA','PLACAR VISITANTE','EQUIPE VISITANTE',
                 'VENCEDOR','RODADA','FASE','GINASIO','TEMPORADA']]
    else:
        df = df[['DATA','EQUIPE CASA','PLACAR CASA','PLACAR VISITANTE','EQUIPE VISITANTE',
             'VENCEDOR','RODADA','FASE','TEMPORADA']]
        
    return df
