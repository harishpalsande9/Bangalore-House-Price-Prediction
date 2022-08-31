import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__datamodel = None


def get_estimated_price(location , sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return  round(__datamodel.predict([x])[0] , 2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading Saved Artifacts .. Start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json" , 'r') as f:
        __data_columns =  json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __datamodel
    with open("./artifacts/banglore_home_prices_model.pickle" , 'rb') as f:
        __datamodel = pickle.load(f)


    print("Loading saved artifacts .. Done")





if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st block jayanagar' , 1000 , 3 , 3))
    print(get_estimated_price('1st block jayanagar' , 1000 , 2 , 2))
    print(get_estimated_price('kalhalli' , 1000 , 2 , 2)) #Other Location
    print(get_estimated_price('Ejipura' , 1000 , 2 , 2))