#Importing libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")
print("The modules are imported")



name2 = pd.DataFrame(df.groupby("Publisher")[["NA_Sales"]].mean().sort_values(by=['NA_Sales'],ascending=[False]).reset_index())
name2.rename(columns = {'Publisher':'Publisher_NA'}, inplace = True)

name3 = pd.DataFrame(df.groupby("Publisher")[["EU_Sales"]].mean().sort_values(by=['EU_Sales'],ascending=[False]).reset_index())
name3.rename(columns = {'Publisher':'Publisher_EU'}, inplace = True)

name4 = pd.DataFrame(df.groupby("Publisher")[["JP_Sales"]].mean().sort_values(by=['JP_Sales'],ascending=[False]).reset_index())
name4.rename(columns = {'Publisher':'Publisher_JP'}, inplace = True)

name5 = pd.DataFrame(df.groupby("Publisher")[["Other_Sales"]].mean().sort_values(by=['Other_Sales'],ascending=[False]).reset_index())
name5.rename(columns = {'Publisher':'Publisher_other'}, inplace = True)

#Concatenating the results.
name_df=pd.concat([name2,name3,name4,name5],axis=1)



#plot graph
subplot_name1 = make_subplots(rows=4, cols=1, shared_yaxes=True,subplot_titles=("North American top publisher","Europe top publisher", "Japan top publisher","Other regions top publisher",'other region top publisher'))

#Subplot for North America
subplot_name1.add_trace(go.Bar(x=name_df['Publisher_NA'][:10], y=name_df['NA_Sales'][:10],marker=dict(color=[1, 2, 3],coloraxis="coloraxis")),1, 1)

#Subplot for Europe
subplot_name1.add_trace(go.Bar(x=name_df['Publisher_EU'][:10], y=name_df['EU_Sales'][:10],marker=dict(color=[1, 2, 3], coloraxis="coloraxis")), 2, 1)

#Subplot for Japan
subplot_name1.add_trace(go.Bar(x=name_df['Publisher_JP'][:10], y=name_df['JP_Sales'][:10],marker=dict(color=[1, 2, 3], coloraxis="coloraxis")),3, 1)

#Subplot for other regions
subplot_name1.add_trace(go.Bar(x=name_df['Publisher_other'][:10], y=name_df['Other_Sales'][:10],marker=dict(color=[1, 2, 3], coloraxis="coloraxis")),4, 1)

subplot_name1.update_layout(height=1000,width=500,coloraxis=dict(colorscale='Mint_r'), showlegend=False)
subplot_name1.update_xaxes(tickangle=45)
subplot_name1.show()