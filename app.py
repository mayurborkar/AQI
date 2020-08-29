from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle

app = Flask(__name__)
model=pickle.load(open('aqi_rf.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    df=pd.read_csv('C:/Users/Lenovo/Desktop/Python/End-To-End Project/AQI/Real CSV.csv')
    my_prediction=model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
    