from flask import Flask, request
# import pickel

import pickle
with open ('classifier.pkl', "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>Welcome to Loan Approval app</h1>"

@app.route("/predict", methods=['GET'])
def predict():
    return "I will predict lona amount..!"

@app.route("/predict", methods=['POST'])
def predict_post():
    loan_req= request.get_json()
    print(loan_req)
    
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "No":
        Married = 0
    else:
        Married = 1


    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    CreditHistory = loan_req['CreditHistory']

    input_data = [Gender, Married, ApplicantIncome, LoanAmount, CreditHistory]
    res = model.predict([input_data])
    if res[0] == 1:
        pred = "Approved"
    else:
        pred = "Rejected"

    return {"loan_approval_status": pred}

   
@app.route("/carpredict", methods=['GET'])
def predict_car():
    return "<h1>Predict the car price </h1>"
