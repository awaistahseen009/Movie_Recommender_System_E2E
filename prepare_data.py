from data_ingestion import DataIngestion
from data_preprocessing import DataPreprocessing

data_ingest=DataIngestion()
credits=data_ingest.get_data('data/tmdb_5000_credits.csv')
movies=data_ingest.get_data('data/tmdb_5000_movies.csv')
print('***********Data has been ingested***********')
print("---------------------------------------------")
'''
DATA PREPROCESSING CLASS IS USED TO PREPROCESS THE DATA AND MAKE
IT READY FOR THE MODEL
'''
movies=movies.merge(credits , on='title')
clean_data=DataPreprocessing(movies)
clean_data.show_shape()
clean_data.remove_null_values()
clean_data.remove_duplicates()
filter_movie = ['movie_id','title','overview','genres','keywords','cast','crew','homepage','runtime']
clean_data.prepare_dataset(filter_cols=filter_movie, save_dataset=True)
print('***********Data has been cleaned***********')
print("---------------------------------------------")