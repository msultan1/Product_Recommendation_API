from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import sys
from Model import ModelHandler

app = Flask(__name__)
api = Api(app)

class Custmor_info :
    age = ""
    seniority =""
    segment = ""
    gender = ""
    relation_type = ""
    annual_income = ""
    activity_lvl = ""
    region = ""

    def __init__(self,age , seniority , segment , gender , relation_type , annaual_income ,activity_lvl ,region):
        self.age = age
        self.seniority = seniority
        self.segment = segment
        self.gender =gender
        self.region =region
        self.relation_type = relation_type
        self.annual_income =annaual_income
        self.activity_lvl = activity_lvl



class ModelExec(Resource):

    def get(self):
        return {'Success' : "GET Rest API Called Successfully"}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('age', required=True)
        parser.add_argument('seniority', required=True)
        parser.add_argument('segment', required=True)
        parser.add_argument('gender', required=True)
        parser.add_argument('relationship_type', required=True)
        parser.add_argument('annaul_income', required=True)
        parser.add_argument('activity_level', required=True)
        parser.add_argument('region', required=True)
        args = parser.parse_args()



        Input_data = pd.DataFrame({
            'age'               : [args['age']],
            'seniority'         : [args['seniority']],
            'segment'           : [args['segment']],
            'gender'            : [args['gender']],
            'relationship_type' : [args['relationship_type']],
            'annaul_income'     : [args['annaul_income']],
            'activity_level'    : [args['activity_level']],
            'region'            : [args['region']]
        })

        myCustmorInfo = Custmor_info(args['age'],args['seniority'],args['segment'],args['gender'],
                                     args['relationship_type'],args['annaul_income'],
                                     args['activity_level'],args['region'])

        myModelHandler = ModelHandler.ModelHandler()

        result = myModelHandler.Predict(myCustmorInfo)

        return {'Input_data': Input_data.to_dict('records') ,
                'Products_Prediction' : result }, 201


# Add URL endpoints
api.add_resource(ModelExec, '/api/v1.0/Prod-Recomm/')

if __name__ == '__main__':
    app.run()