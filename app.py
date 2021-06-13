from flask import *
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('Corp_recomend.pkl','rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict",methods = ['POST'])
def predict():
    
    int_features = [float(x) for x in request.form.values()]
    data = [np.array(int_features)]
    final_feature=model.predict(data)
    output=final_feature[0]
    
     
        
        
        
  
    return render_template('index.html',result = "Recommended Crop as per your soil condition is {}".format(output))
    
    
if __name__ =="__main__":
    app.run(debug=True)