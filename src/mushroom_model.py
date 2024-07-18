"""
mushroom_model

Functions for predicting whether a given mushroom is poisonous or not.
"""


"""
mushroom_model

Functions for predicting whether a given mushroom is poisonous or not.
"""
import joblib
import pandas as pd

PATH = "models/artifacts.joblib"
ARTIFACT = joblib.load(PATH)
MODEL = ARTIFACT['lr_model']
PREPROCESSOR = ARTIFACT['preprocessor']


def predict_mushroom(df):
    """
    Returns ndarray of predictions (poisonous=1) 
    given a properly formatted DataFrame of observations.
    
    observation = {
    'cap-diameter': [cap_dia],
    'stem-height': [stem_h],
    'stem-width': [stem_w],
    'has-ring': [has_ring],
    'cap-shape': [cap_shape]
    }
    """
    single_ob = pd.DataFrame(df)
    single_ob_proc = PREPROCESSOR.transform(single_ob)
    prediction = MODEL.predict(single_ob_proc)
    probability = MODEL.predict_proba(single_ob_proc)
    return prediction


if __name__ == "__main__":
    observation = {
    'cap-diameter': [50],
    'stem-height': [20],
    'stem-width': [30],
    'has-ring': ['t'],
    'cap-shape': ['c']
}

    # confirm ARTIFACT dictionary
    print(predict_mushroom(observation))