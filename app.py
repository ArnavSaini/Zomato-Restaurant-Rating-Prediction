import numpy as np

from flask import Flask, request, jsonify, render_template

import pickle

import logging

import pymongo

logging.basicConfig(filename='info.txt', 
                    level=logging.INFO,
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M-%S')

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')

def home():

    logging.info("Someone is accessing index.html!!!")

    return render_template('index.html')



@app.route('/predict',methods=['POST'])

def predict():

    '''
    For rendering results on HTML GUI
    '''

    if request.method == 'POST':
            a = request.form["Online Order"]
            b = request.form["Book Table"]
            c = request.form["Votes"]
            d = request.form["Location"]
            e = request.form["Restaurant Type"]
            f = request.form["Dishes Liked"]
            g = request.form["Cuisines"]
            h = request.form["Cost For 2 Person"]
            i = request.form["Type"]


            logging.info("Successfully retrieved information from user...! ")

    default_connection_url ="mongodb+srv://arnav:iafsu30mki@cluster0.wzrwu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(default_connection_url)
    logging.info("Database connection established..!")

    db_name = "zomato"
    database = client[db_name]
    print("DB created!!")
    collection_name = "user_details"
    collection = database[collection_name]
    print("collection Created!!")


    features = [int(x) for x in request.form.values()]

    final_features = [np.array(features)]

    prediction = model.predict(final_features)


    output = round(prediction[0], 1)

    info = {
                'Online Order':a,
                'Book Table': b,
                'Votes': c,
                'Location': d,
                'Restaurant Type': e,
                'Dishes Liked': f,
                'Cuisines': g,
                'Cost For 2 Person': h,
		'Type': i,
		'Rating Prediction' : output,
            }
        
    collection.insert_one(info)
    logging.info("data inserted")


    logging.info("successfully predicted")
    return render_template('index.html', prediction_text='Your Rating is: {}'.format(output))


if __name__ == "__main__":

    app.run(host='0.0.0.0',port=8080)
    #app.run(debug=True)