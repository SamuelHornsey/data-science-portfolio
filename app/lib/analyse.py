from app import celery
import pandas as pd
from sklearn.externals import joblib

import json
import time

@celery.task
def run_model(data):
    time.sleep(3)

    df = pd.read_json(json.dumps([data]), orient='records')

    reg = joblib.load('./app/models/clf.pkl')

    predicted = reg.predict(df)

    print('Predicted', predicted)

    return predicted[0]


