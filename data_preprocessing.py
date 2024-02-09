import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import ast
class DataPreprocessing:
    def __init__(self, data_frame : pd.DataFrame)->None:
        self.data_frame=data_frame

    def rename_cols(self)->None:
        self.data_frame.columns= ['text','target']
    
    def get_dataframe(self)->pd.DataFrame:
        return self.data_frame

    def show_shape(self)->None:
        print(f'Shape of Dataframe is: {self.data_frame.shape}')

    def show_null_values(self)->None:
        print(f'Total num values are as follows: {self.data_frame.isna().sum()}')
    
    def remove_null_values(self)->None:
        self.data_frame.dropna(inplace=True)
        print('Null values are being removed')
    
    def show_duplicates(self)->None:
        print(f'Total duplicate values are : {self.data_frame.duplicated()}')
    
    def remove_duplicates(self)->None:
        self.data_frame.drop_duplicates(inplace=True)
        print('Duplicates values are being removed')
    
    def prepare_dataset(self, filter_cols, save_dataset=False):
        self.data_frame=self.data_frame[filter_cols]
        cols_to_convert=['genres','keywords','cast','crew']
        for col in cols_to_convert:
            self.data_frame[col]=self.data_frame[col].apply(self.convert_string_to_list)
        self.data_frame['keywords']=self.data_frame['keywords'].apply(self.fetch_keywords)
        self.data_frame['genres']=self.data_frame['genres'].apply(self.fetch_keywords)
        self.data_frame['crew']=self.data_frame['crew'].apply(self.fetch_crew)
        self.data_frame['cast']=self.data_frame['cast'].apply(self.fetch_cast)
        self.data_frame['cast_ws'] = self.data_frame['cast'].apply(lambda x: [self.remove_spaces(x) for x in x])
        self.data_frame['genres_ws'] = self.data_frame['genres'].apply(lambda x: [self.remove_spaces(x) for x in x])
        self.data_frame['overview']=self.data_frame['overview'].apply(lambda x: str(x).split())
        self.data_frame['tags']=self.data_frame['overview'] + self.data_frame['genres_ws'] + self.data_frame['keywords'] + self.data_frame['cast_ws'] + self.data_frame['crew']
        self.data_frame['tags']=self.data_frame['tags'].apply(lambda x: ' '.join(x))
        self.data_frame['tags']=self.data_frame['tags'].apply(lambda x: x.lower())
        self.data_frame['crew_new']=self.data_frame['crew'].apply(lambda x: ", ".join(x))
        self.data_frame['cast_new']=self.data_frame['cast'].apply(lambda x: ", ".join(x))
        if save_dataset:
            self.data_frame.to_csv('processed_data_frame.csv')
   
    def convert_string_to_list(self , txt):
        return ast.literal_eval(txt)
    
    def fetch_keywords(self, text_list):
        keywords=[]
        for txt in text_list:
            keywords.append(txt['name'])
        return keywords # We can use same function for genres and keywords
    
    def fetch_crew(self, crew_list): # In a movie the most important crew and for people also search is director so we have to fetch him/her.
        crew=list()
        for crw in crew_list:
            if crw['job']=='Director':
                crew.append(crw['name'])
        return crew
    
    def fetch_cast(self, cast_list):
        cast=list()
        for i,cst in enumerate(cast_list):
            if i<3:
                cast.append(cst['name'])
            else:
                break
        return cast
    
    def remove_spaces(self, text):
        return text.replace(" ","")



    

        



        

            
