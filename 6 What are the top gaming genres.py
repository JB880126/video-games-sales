#Importing libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")
print("The modules are imported")




genre_df = df.groupby("Genre")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).reset_index()
genre_df #print the dataframe



#plot graph
bar_genre= px.bar(genre_df, x='Genre', y='Global_Sales',color='Global_Sales',color_continuous_scale='Burgyl')
bar_genre.show()