from flask import Flask, jsonify, request
import pickle
import os
from src.processing.pre_processing import clean_text

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top


def load_model(source="models/model.pkl"):
    """Load pre-trained model

    Parameters
    ----------
    source : str
        The model_name.pkl file path

    Returns
    -------
    pipeline
        Loaded pipeline for prediction process
    """
    pkl = open(source, 'rb')
    model_pipeline = pickle.load(pkl)
    pkl.close()
    return model_pipeline


model = load_model()


def predict_tag(text):
    """Prediction most related tag for this text

    Parameters
    ----------
    text : str
        Plain text to predict most related tag for it

    Returns
    -------
    Array
            Predicted class label for this text.
    """
    text = clean_text(text)
    print(text)
    return model.predict([text])


@app.route('/')
def welcome_message():
    return """
    /tags "POST" >>>
    {
    "question_text":" question text ..."
    }
    """


@app.route("/tags", methods=["POST"])
def find_job_title():
    question_text = request.json['question_text']
    result = {"tag": str(predict_tag(question_text)[0])}
    return jsonify(result)


if __name__ == '__main__':
    app.run()
