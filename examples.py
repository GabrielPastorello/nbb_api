#########################
########## NBB ##########
#########################

from nbb_api import nbb

###### get_stats ######

# Médias dos jogadores na temporada regular (pontos) em 2022-23
df = nbb.get_stats('2022-23','regular','cestinhas','avg','athletes')
print(df)
# Total dos jogadores nos playoffs (rebotes) em 2021-22
df = nbb.get_stats('2021-22','playoffs','rebotes','sum','athletes')
print(df)
# Médias dos jogadores em tudo (regular+playoffs) (arremessos) em 2008-09
df = nbb.get_stats('2008-09','total','arremessos','avg','athletes')
print(df)
# Total dos times em tudo (regular+playoffs) (erros) em 2008-09
df = nbb.get_stats('2008-09','total','erros','sum','teams')
print(df)
# Médias (sofridas) dos times em tudo (regular+playoffs) (eficiencia) em 2008-09
df = nbb.get_stats('2008-09','total','eficiencia','avg','teams',sofrido=True)
print(df)

###### get_classificacao ######

# Classificação temp. regular 2022-23
df = nbb.get_classificacao('2022-23')
print(df)

###### get_placares ######

# Placares da temporada regular de 2022-23
df = nbb.get_placares('2022-23','regular')
print(df)
# Todos os placares (regular+playoffs) de 2014-15
df = nbb.get_placares('2014-15','total')
print(df)


#########################
####### Liga Ouro #######
#########################

from nbb_api import liga_ouro

###### get_placares ######

# Todos os placares (regular+playoffs) de 2019
df = liga_ouro.get_placares(2019,'total')
print(df)

###### get_classificacao ######

# Classificação temp. regular 2014
df = liga_ouro.get_classificacao(2014)
print(df)


#########################
########## LDB ##########
#########################

from nbb_api import ldb # Liga de Desenvolvimento de Basquete

###### get_stats ######

# Médias dos jogadores na temporada regular (pontos) em 2022
df = ldb.get_stats(2022,'regular','cestinhas','avg','athletes')
print(df)
# Total dos jogadores nos playoffs (duplos-duplos) em 2011
df = ldb.get_stats(2011,'total','duplos-duplos','sum','athletes')
print(df)
# Total dos times na temporada regular (enterradas) em 2014
df = ldb.get_stats(2014,'regular','enterradas','sum','teams')
print(df)

###### get_classificacao ######

# Classificação temp. regular 2011
df = ldb.get_classificacao(2011)
print(df)

###### get_placares ######

# Todos os placares (regular+playoffs) de 2022
df = ldb.get_placares(2022,'total')
print(df)
