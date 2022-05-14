import streamlit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/all_df.csv', index_col=0)

streamlit.title('Test')

year = streamlit.slider('Year',min_value=min(df['year']),max_value=max(df['year']))

fig, ax = plt.subplots()
ax.scatter(x=df[df['year']==year]['ley'],y=np.log(df[df['year']==year]['pop']))
plt.xlabel('ley')
plt.ylabel('pop')

streamlit.pyplot(fig)

streamlit.write(df['gdi'])