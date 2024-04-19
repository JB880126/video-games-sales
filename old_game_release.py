#Importing libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")
print("The modules are imported")

def visualise_games_old_releases(df):

 old_games = pd.DataFrame(df.query('Year<2000', inplace=False))
 
 
 #plot graph
 print(old_games.query('Global_Sales>7.8235', inplace=False))

 