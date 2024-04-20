import pandas as pd
import warnings
import numpy as np

season_dict = {'2011':'5','2012':'10','2013':'14',
                '2014':'21','2015':'29','2016':'36','2017':'42',
               '2018':'48','2019':'53','2021':'64','2022':'69','2023':'78'}

fase_dict = {'regular':'%5B%5D=1',
            'total':'%5B%5D=1&phase%5B%5D=2&phase%5B%5D=3&phase%5B%5D=4'}

seasons = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2021','2022','2023']

fases = ['regular','total']

sofrido_dict = {False:'0',True:'1'} # só muda p/times

categs = ['cestinhas','rebotes','assistencias','arremessos','bolas-recuperadas','tocos',
        'erros','eficiencia','duplos-duplos','enterradas']

tipos = ['avg','sum']

quems = ['athletes','teams']

sofridos = [True,False]

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

def get_stats(season, fase, categ, tipo='avg', quem='athletes', sofrido=False):

    if str(season) not in seasons:
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
    
    season2 = season_dict[str(season)]
    
    sofrido = sofrido_dict[sofrido]
    
    fase = fase_dict[fase]
    
    url = 'https://lnb.com.br/ldb/estatisticas/'+categ+'/?aggr='+tipo+'&type='+quem+'&suffered_rule='+sofrido+'&season%5B%5D='+season2+'&phase'+fase

    df = pd.read_html(url)[0]

    if quem=='athletes':
        df['Camisa'] = df['Jogador'].str.split(' #').str[1]
        df['Jogador'] = df['Jogador'].str.split(' #').str[0]

    df = df.drop(columns=['Pos.'])
        
    df['Temporada'] = season                  
    
    return df

def get_placares(season, fase):
    
    if str(season) not in seasons:
        raise ValueError(str(season)+' não é um valor válido. Tente um de: "'+'", "'.join(seasons)+'".')
    
    if fase not in fases:
        raise ValueError(str(fase)+' não é um valor válido. Tente um de: "'+'", "'.join(fases)+'".')
    
    season2 = season_dict[str(season)]
    
    fase = fase_dict[fase]
    
    if fase!='%5B%5D=1&phase%5B%5D=2&phase%5B%5D=3&phase%5B%5D=4': # total
        url = 'https://lnb.com.br/liga-ouro/tabela-de-jogos/?season%5B%5D='+season2+'&phase'+fase
    else:
        url = 'https://lnb.com.br/liga-ouro/tabela-de-jogos/?season%5B%5D='+season2
    
    df = pd.read_html(url)[0]
    
    try:
        df = df.drop(columns=['#','CASA','Unnamed: 15','GINÁSIO','RODADA'])
    except:
        df = df.drop(columns=['#','CASA','Unnamed: 14','GINÁSIO','RODADA'])
        
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
    
    try:
        df = df[['DATA','EQUIPE CASA','PLACAR CASA','PLACAR VISITANTE','EQUIPE VISITANTE',
                'VENCEDOR','RODADA','FASE','GINASIO','TEMPORADA']]
    except:
        df = df[['DATA','EQUIPE CASA','PLACAR CASA','PLACAR VISITANTE','EQUIPE VISITANTE',
                'VENCEDOR','RODADA','FASE','TEMPORADA']]    
    
    return df
