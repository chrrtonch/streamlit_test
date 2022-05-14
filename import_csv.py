import pandas as pd
import numpy as np

pop = pd.read_csv('data/population_total.csv',header=0).fillna(method='ffill',axis=0)
ley = pd.read_csv('data/life_expectancy_years.csv',header=0).fillna(method='ffill',axis=0)
gdi = pd.read_csv('data/ny_gnp_pcap_pp_cd.csv',header=0).fillna(method='ffill',axis=0)

pop = pd.melt(pop,['country'],var_name='year',value_name='pop')
ley = pd.melt(ley,['country'],var_name='year',value_name='ley')
gdi = pd.melt(gdi,['country'],var_name='year',value_name='gdi')

all_df = pd.merge(left=pop,right=ley,how='outer',on=['country','year'])
all_df = pd.merge(left=all_df,right=gdi,how='left',on=['country','year'])#.sort_values(['country','year'])#.fillna(method='backfill')

print(all_df[all_df['year']>='1990'])

all_df['pop'] = all_df['pop'].apply(value_to_float)
all_df['ley'] = all_df['ley'].apply(value_to_float)
all_df['gdi'] = all_df['gdi'].apply(value_to_float)

all_df.to_csv('data/all_df.csv')

print(all_df[all_df['year']>='1990']['gdi'])
print(min(all_df['gdi']))