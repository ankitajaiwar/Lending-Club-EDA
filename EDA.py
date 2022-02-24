#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


class EDA:
    
        
    def navalues(self, df):
        sns.set(rc={'figure.figsize':(20,15)})
        sns.heatmap(df.isna(), cmap = "mako")
        
    def coldrop(self, df):
        col_to_drop = (df.isna().sum() * 100 / len(df)).to_frame(name = "na_perc")
        col_to_drop = col_to_drop.sort_values("na_perc", ascending = False)
        col_to_drop = col_to_drop.reset_index()
        col_to_drop = col_to_drop[col_to_drop['na_perc']>75]
        df = df.drop(col_to_drop['index'], axis = 1)
        
        return df
    
    def percentagebarplot(self, df, listt, xx, order = None):
        sns.set(rc={'figure.figsize':(20,15)})
        target = (df.loc[(df.loan_status == listt[0]) | (df.loan_status == listt[1])][xx]).to_frame()
        target = target[xx].value_counts().to_frame(name = 'target')
        original = df[xx].value_counts().to_frame(name = 'original')
        per = pd.concat((target, original), axis =1)
        per['perc'] = (per.target/per.original)*100
        sns.barplot(x = per.index, y = per['perc'])
        
    def violin(self, df, x, y, hue):
        sns.set(rc={'figure.figsize':(15,10)})
        sns.violinplot(x=x,y=y,data=df, hue=hue, split=True,palette='mako')
        plt.title(str(hue)+"  -   "+str(y), fontsize=20)
        plt.xlabel(x, fontsize=15)
        plt.ylabel(y, fontsize=15);
        
    def correlation(self, df):
        corr = df.corr()
        s = corr.unstack()
        s = s.sort_values(kind="quicksort", ascending = False)
        return s

