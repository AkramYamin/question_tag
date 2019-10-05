import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
import pickle


def train(cleaner, data_source, save_to="../models/model.pkl"):
    """Train machine learning model and serialize it

    Parameters
    ----------
    cleaner : function
        how to clean row data
    data_source : str
        training data source path
    save_to : str
        path to save trained model as pickle file

    Returns
    -------
    pipeline
        pipeline for prediction process
    """
    df = pd.read_csv(data_source)
    df = df[pd.notnull(df['tags'])]
    print("Start :  Pre-cleaning process . . . ")
    print("         HTML decoding . . . done")
    print("         lowercase text . . . done")
    print("         replace [/(){}\[\]\|@,;] symbols by space . . . done")
    print("         remove remaining symbols . . . done")
    print("         remove stopwords . . . done")
    df['post'] = df['post'].apply(cleaner)
    print("End :    Pre-cleaning process")
    x = df.post
    y = df.tags
    # no need for split data in final training stage
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)
    print("Start :  model creation process . . . ")
    sgd = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5,
                                          tol=None)),
                    ])
    # sgd.fit(X_train, y_train)
    sgd.fit(x, y)
    print("End :   model creation process")
    model = open(save_to, 'wb')
    pickle.dump(sgd, model)
    model.close()
    print("Trained model saved to " + save_to)
    return sgd
