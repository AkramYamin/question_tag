from src.processing.pre_processing import clean_text
from src.modelling.train import train
from src.utils.dto import read_from_db

db_name = "DS"
host = "127.0.0.1"
user = "root"
password = ""
save_to = "../data/row/training_data_from_db.csv"
csv_path = read_from_db(db_name ,host, user, password, save_to)
model = train(clean_text, csv_path, "../models/model_from_db.pkl")
