import pandas as pd
import json
#import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from flask import Flask, render_template, request
disease=[]
desc=[]
with open('config.json', 'r', encoding="utf8") as c:
    disdesc = json.load(c)["parms"]
'''model section which is used to get the disease'''
def disease_detect(l):
    df = pd.read_csv('dataset.csv')
    df1 = pd.read_csv('Testing.csv')
    df2 = pd.read_csv('Training.csv')
    # df1
    cols1 = df2.columns
    cols2 = df1.columns
    # print(cols1)
    # print(cols2)
    train_x = cols1[:-1]
    train_y = cols1[-1]
    test_x = cols2[:-1]
    test_y = cols2[-1]
    model = LogisticRegression()
    model.fit(df2[train_x], df2[train_y])
    y_predict = model.predict(df1[test_x])
    # 'fatigue', 'weight_loss', 'restlessness', 'lethargy', 'irregular_sugar_level', 'blurred_and_distorted_vision','obesity', 'excessive_hunger', 'increased_appetite','polyuria'
    l1 = list(train_x)
    l2 = [0] * 132
    for i in l:
        l2[l1.index(i)] = 1
    dpredict = model.predict([l2])
    return dpredict
app = Flask(__name__)
@app.route("/", methods = ['GET','POST'] )
def Home():
    lsym=["itching","skin_rash","nodal_skin_eruptions","continuous_sneezing","shivering","chills","joint_pain","stomach_pain","acidity","ulcers_on_tongue","muscle_wasting","vomiting","burning_micturition","spotting_urination","fatigue","weight_gain","anxiety","cold_hands_and_feets","mood_swings","weight_loss"
,"restlessness","lethargy","patches_in_throat","irregular_sugar_level","cough","high_fever","sunken_eyes"
,"breathlessness","sweating","dehydration","indigestion","headache","yellowish_skin","dark_urine","nausea","loss_of_appetite","pain_behind_the_eyes","back_pain","constipation","abdominal_pain","diarrhoea"
,"mild_fever","yellow_urine","yellowing_of_eyes","acute_liver_failure","fluid_overload","swelling_of_stomach"
,"swelled_lymph_nodes","malaise","blurred_and_distorted_vision","phlegm","throat_irritation","redness_of_eyes","sinus_pressure","runny_nose","congestion","chest_pain","weakness_in_limbs","fast_heart_rate","pain_during_bowel_movements","pain_in_anal_region","bloody_stool","irritation_in_anus","neck_pain","dizziness"
,"cramps","bruising","obesity","swollen_legs","swollen_blood_vessels","puffy_face_and_eyes","enlarged_thyroid","brittle_nails","swollen_extremeties","excessive_hunger","extra_marital_contacts","drying_and_tingling_lips","slurred_speech","knee_pain","hip_joint_pain"
,"muscle_weakness","stiff_neck","swelling_joints","movement_stiffness","spinning_movements","loss_of_balance","unsteadiness","weakness_of_one_body_side","loss_of_smell","bladder_discomfort","foul_smell_ofurine","continuous_feel_of_urine","passage_of_gases"
,"internal_itching","toxic_look_(typhos)","depression","irritability","muscle_pain","altered_sensorium","red_spots_over_body","belly_pain","abnormal_menstruation","dischromic_patches","watering_from_eyes","increased_appetite"
,"polyuria","family_history","mucoid_sputum","rusty_sputum","lack_of_concentration","visual_disturbances","receiving_blood_transfusion","receiving_unsterile_injections"
,"coma","stomach_bleeding","distention_of_abdomen","history_of_alcohol_consumption","fluid_overload","blood_in_sputum","prominent_veins_on_calf","palpitations","painful_walking","pus_filled_pimples","blackheads"
,"scurring","skin_peeling","silver_like_dusting","small_dents_in_nails","inflammatory_nails","blister","red_sore_around_nose","yellow_crust_ooze"
]
    if (request.method == 'POST'):
        i=1
        l=[]
        while i<7:
            symptoms = request.form.get(f'sym{i}')
            print(symptoms)
            l.append(symptoms)
            i=i+1
        print(l)
        for i in range(0,l.count('')):
            l.remove('')
        print(l)
        global disease
        disease1 = disease_detect(l)
        if len(disease)>0:
            disease.pop()
        disease.append(disease1[0])
        print(f"you are suffering from {disease[0]} ")
        #print(disdesc[disease[0]])
        global desc
        desc1= disdesc[disease[0]]
        print(desc1)
        if len(desc)>0:
            desc.pop()
        desc.append(desc1)
        print(desc[0])
    return render_template('index.html', lsym=lsym)
@app.route("/login", methods = ['GET','POST'] )
def login():
    if( request.method == 'POST' ):
        user = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        l=[]
        l.append(user)
        l.append(password)
        l.append(email)
        print(l)
    return render_template('inner-page.html')
@app.route("/register")
def register():
    return render_template('register.html')
@app.route("/inner")
def inner():
    with open('config1.json', 'r', encoding="utf8") as c1:
        disdesc1 = json.load(c1)["parms1"]
    with open('config2.json', 'r', encoding="utf8") as c2:
        disdesc2 = json.load(c2)["parms2"]
    with open('config3.json', 'r', encoding="utf8") as c3:
        disdesc3 = json.load(c3)["parms3"]
    global disease
    global desc
    print(disease)
    print(type(disease))
    print(desc)
    return render_template('inner-page2.html', disease=disease, desc=desc, symp=disdesc1[disease[0]], pre=disdesc2[disease[0]], img=disdesc3[disease[0]] )
app.run( debug= True)






