from src.processing.pre_processing import clean_text
from src.modelling.train import train

# model = train(clean_text, "https://storage.googleapis.com/tensorflow-workshop-examples/stack-overflow-data.csv")
model = train(clean_text, "../data/row/training_data.csv")
