from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('price_prediction.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    bedrooms = int(request.form.get('bedrooms'))
    bathrooms = int(request.form.get('bathrooms'))
    sqft_living = int(request.form.get('sqft_living'))
    sqft_lot = int(request.form.get('sqft_lot'))
    floors = int(request.form.get('floors'))
    waterfront = int(request.form.get('waterfront'))
    view = int(request.form.get('view'))
    condition = int(request.form.get('condition'))
    sqft_above = int(request.form.get('sqft_above'))
    sqft_basement = int(request.form.get('sqft_basement'))
    yr_built= int(request.form.get('yr_built'))
    yr_renovated= int(request.form.get('yr_renovated'))
    city = int(request.form.get('city'))
    # prediction
    results = model.predict(np.array([bedrooms,bathrooms,sqft_living,sqft_lot,  floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated,city]).reshape(1,13))
    return render_template('price_prediction.html',result=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)