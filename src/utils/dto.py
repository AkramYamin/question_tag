import mysql.connector
import pandas as pd


def read_from_db(db, host="127.0.0.1", user="root", password="", save_to="../data/row/training1_data.csv"):
    """Fetch training questions and tags from Database

    Parameters
    ----------
    db : str
        Database name
    host : str
        Database host url or ip
    user : str
        Database username
    password : str
        Database password
    save_to : str
        path to save feched data as csv file

    Returns
    -------
    str
        generated csv file path
    """
    cnx = mysql.connector.connect(user=user, password=password,
                                  host=host,
                                  database=db)
    my_cursor = cnx.cursor()
    my_cursor.execute("select questions.text, tags.name from questions, tags,"
                      " question_tag where questions.id=question_tag.question_id and tags.id=question_tag.tag_id")
    my_result = my_cursor.fetchall()
    df = pd.DataFrame({
        "post": [],
        "tags": []
    })
    for x in my_result:
        df = df.append({"post": x[0], "tags": x[1]}, ignore_index=True)

    df.to_csv(save_to, index=False)
    return save_to
