from fastapi import FastAPI 
import pickle
from pydantic import BaseModel ,Field
from typing import Annotated
from fastapi.responses import JSONResponse

with open('model.pkl','rb') as f :
    model = pickle.load(f)


class data_validation(BaseModel):
    sepal_length : Annotated[float,Field(...,description='Enter the sepal length',examples=['0.1 to 10'],gt=0,le=10)]
    sepal_width  : Annotated[float,Field(...,description='Enter the sepal width',examples=['0.1 to 10'],gt=0 ,le=10)]
    petal_length : Annotated[float,Field(...,description='Enter the petal legth',examples=['0.1 to 10'],gt=0,le=10)]
    petal_width : Annotated[float,Field(...,description='Enter the petal width',examples=['0.1 to 10'],gt=0,le=10)]




app = FastAPI()


@app.get("/")
def start():
    return {'message':'Welcome to iris classifier'}



@app.post("/prediction")
def prediction_by_model(data:data_validation):

    input_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = model.predict(input_data)[0]
    def prediction_class(prediction:prediction):
        
        if int(prediction)==0:
            return 'ris setosa'
        
        elif int(prediction)==1:
            return  'Iris virginica'
        
        elif int(prediction)==2:
            return  'Iris versicolo'
        
        else:
            return "unknow"
    


    return  JSONResponse(status_code=200,content={'Predicted Class':prediction_class(prediction)})
    
    



