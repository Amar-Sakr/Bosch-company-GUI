import pandas as pd
import numpy as np

from page2 import *

class functions:

    def data_frame(path):
        df= pd.read_excel(path)
        return df
    
    def BRC_Template(IdM_Liste,Benötigte_Anwendungen,Cluster_Liste,BRC_Template):
        IdM_Liste = IdM_Liste[['User ID', 'Application', 'IT-Role', 'IT-Role Description']]
        
        Benötigte_Anwendungen=Benötigte_Anwendungen[['Application' , 'IT-Role']]
        IdM_Liste= IdM_Liste[IdM_Liste.set_index(['Application' , 'IT-Role']).index.isin(Benötigte_Anwendungen.set_index(['Application' , 'IT-Role']).index)]

        Cluster_Liste = Cluster_Liste.rename(columns = { 'Unnamed: 1' : 'User ID', 'Unnamed: 2':'Organization'})
        Cluster_Liste.drop([0], inplace = True)
        Cluster_Liste = Cluster_Liste.dropna(axis=1, how='all')
        Cluster_Liste = functions.clusters(Cluster_Liste)  # calling the algorithm

        arr = Cluster_Liste['Business Role Name'].unique()

        IdM_Liste =pd.merge(Cluster_Liste,IdM_Liste, how='left')
        IdM_Liste=IdM_Liste.drop(['Stellenbeschreibung:','Organization'], axis=1)

        ex=pd.DataFrame()

        for i in arr:
            test =IdM_Liste[IdM_Liste['Business Role Name'] == i]
    
            count = test.groupby(['IT-Role','Application']).count()
            df_4=count.stack().reset_index().sort_values(by=['IT-Role','Application']) # unpivot 
            df_4=df_4.drop('level_2', axis=1)
            df_5 =pd.merge(test,df_4) # merge
            df_5 = pd.DataFrame.drop_duplicates(df_5)
            df_6 = df_5.drop_duplicates(subset = ['User ID'],keep = 'last').reset_index(drop = True) 
            users= len(df_6.axes[0])
            rows=len(df_5.axes[0]) # no rows in the table
            df_5['precentage']= 0

            for i in range(rows):  
                precentage =float((df_5.iloc[i,5]/users)*100)
                if float(precentage)>=100.0:
                    df_5.iloc[i,6]=precentage

            ex=pd.concat([df_5,ex])
        
        df_7 = ex[(ex['precentage'] >= 100.0)] 
        df_7 = df_7.drop(['User ID',0,'precentage'], axis=1)
        df_7 =df_7.drop_duplicates(subset = ['IT-Role','Application','Business Role Name'],keep = 'last')


        BRC_Template = BRC_Template.drop(BRC_Template.index[[0]])
        BRC_Template = BRC_Template.rename(columns={'Business Role Description (technical language)':'Business Role Name', 'Unnamed: 1':'Application', 'Unnamed: 2':'IT-Role','Unnamed: 3':'IT-Role Description','Unnamed: 4':'Risks (optional)'} )
        

        df_8 =pd.concat([BRC_Template, df_7], axis=0, sort= True)
        df_8 = pd.DataFrame.drop_duplicates(df_8)


        return df_8

    # used in BRC_Template
    def clusters(df):
        df['Business Role Name'] = ' '
        names = list(df.columns)
        i, c = np.where(df == 'x')  # positions for all 'x'
        a, b = np.where(df == 'X')  # positions for all 'X'  
        row = np.append(i,a) #append together
        column = np.append(c,b)
        for i in range(row.size):
            df.iat[row[i],len(names)-1]= names[column[i]]     
        df = df.dropna(axis=1)

        return df

    def Berechtigungsmatrix(IdM_Liste,Benötigte_Anwendungen):
        Benötigte_Anwendungen=Benötigte_Anwendungen[['Application' , 'IT-Role']]
        IdM_Liste=IdM_Liste[['User ID','Application','IT-Role','IT-Role Description']]
        IdM_Liste = IdM_Liste.drop_duplicates(keep=False)
        IdM_Liste= IdM_Liste[IdM_Liste.set_index(['Application' , 'IT-Role']).index.isin(Benötigte_Anwendungen.set_index(['Application' , 'IT-Role']).index)]
        IdM_Liste = IdM_Liste.pivot_table(IdM_Liste, index=['User ID'],columns= ['IT-Role','Application','IT-Role Description' ],aggfunc=','.join )
        df_3 = IdM_Liste.replace(['User ID,Application,IT-Role,IT-Role Description'],'X')
        return df_3

    def Ubereinstimmungsliste(IdM_Liste,Benötigte_Anwendungen, precent):

        IdM_Liste = IdM_Liste[['User ID','Application','IT-Role','IT-Role Description']]
        Benötigte_Anwendungen=Benötigte_Anwendungen[['Application' , 'IT-Role']]
        IdM_Liste= IdM_Liste[IdM_Liste.set_index(['Application' , 'IT-Role']).index.isin(Benötigte_Anwendungen.set_index(['Application' , 'IT-Role']).index)]
        count = IdM_Liste.groupby(['IT-Role','Application']).count()  # count no. users in each IT Role

        df_3=count.stack().reset_index().sort_values(by=['IT-Role','Application']) # unpivot 
        df_3=df_3.drop('level_2', axis=1)

        df_4 =pd.merge(IdM_Liste,df_3) # merge
        df_4 = pd.DataFrame.drop_duplicates(df_4)

        df_5 = df_4.drop_duplicates(subset = ['User ID'],keep = 'last').reset_index(drop = True) # user once appearence
        users= len(df_5.axes[0]) # total no of users

        rows=len(df_4.axes[0]) # no rows in the table
        df_4['precentage']= 0
        for i in range(rows):  # to get 80 to 100 precent
            precentage = (df_4.iloc[i,4]/users)*100
            if float(precentage)>=float(precent):
                df_4.iloc[i,5]=precentage

        final = df_4[~(df_4['precentage']<float(precent))]  # drop less than 80 precent

        df_6 =final[['User ID','Application','IT-Role','IT-Role Description']] #create pivot table
        df_6 = df_6.pivot_table(df_6, index=['User ID'],columns= ['IT-Role','Application','IT-Role Description'],aggfunc=','.join )
        df_6 = df_6.replace(['User ID,Application,IT-Role,IT-Role Description'],'X')
        return df_6
