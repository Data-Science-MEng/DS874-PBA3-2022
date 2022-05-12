from flask import Flask, render_template, request
import streamlit as st
from predict_page import show_predict_page

show_predict_page()

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return render_template("index.html")


# @app.route("/sub", methods = ['POST'])
# def submit():
#     # HTML -> .py
#     if request.method == "POST":
#         name = request.form["username"]
#     # .py -> HTML
#     return render_template("sub.html", n=name)

# if __name__ == "__main__":
#     app.run(debug=True)



# defining a new instance - will be the user's input
#new_instance = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

# mass comment cntrl k c
# Data columns (total 34 columns):
#    Column                               Non-Null Count   Dtype  
# ---  ------                               --------------   -----  
#  0   BMI                                  319795 non-null  float64
#  1   PhysicalHealth                       319795 non-null  float64
#  2   MentalHealth                         319795 non-null  float64
#  3   AgeCategory                          319795 non-null  float64
#  4   GenHealth                            319795 non-null  float64
#  5   SleepTime                            319795 non-null  float64
#  6   Smoking_No                           319795 non-null  uint8  
#  7   Smoking_Yes                          319795 non-null  uint8  
#  8   AlcoholDrinking_No                   319795 non-null  uint8  
#  9   AlcoholDrinking_Yes                  319795 non-null  uint8  
#  10  Stroke_No                            319795 non-null  uint8  
#  11  Stroke_Yes                           319795 non-null  uint8  
#  12  DiffWalking_No                       319795 non-null  uint8  
#  13  DiffWalking_Yes                      319795 non-null  uint8  
#  14  Sex_Female                           319795 non-null  uint8  
#  15  Sex_Male                             319795 non-null  uint8  
#  16  Race_American Indian/Alaskan Native  319795 non-null  uint8  
#  17  Race_Asian                           319795 non-null  uint8  
#  18  Race_Black                           319795 non-null  uint8  
#  19  Race_Hispanic                        319795 non-null  uint8  
#  20  Race_Other                           319795 non-null  uint8  
#  21  Race_White                           319795 non-null  uint8  
#  22  Diabetic_No                          319795 non-null  uint8  
#  23  Diabetic_No, borderline diabetes     319795 non-null  uint8  
#  24  Diabetic_Yes                         319795 non-null  uint8  
#  25  Diabetic_Yes (during pregnancy)      319795 non-null  uint8  
#  26  PhysicalActivity_No                  319795 non-null  uint8  
#  27  PhysicalActivity_Yes                 319795 non-null  uint8  
#  28  Asthma_No                            319795 non-null  uint8  
#  29  Asthma_Yes                           319795 non-null  uint8  
#  30  KidneyDisease_No                     319795 non-null  uint8  
#  31  KidneyDisease_Yes                    319795 non-null  uint8  
#  32  SkinCancer_No                        319795 non-null  uint8  
#  33  SkinCancer_Yes                       319795 non-null  uint8  




# # Select boxes
# age_category = st.selectbox("Please select your age", ['55-59','80 or older','65-69','75-79','40-44','70-74','60-64','50-54','45-49','18-24','35-39','30-34','25-29'])
# if age_category == '55-59':
#     new_instance[:,3]=57
# if age_category == '80 or older':
#     new_instance[:,3]=80
# if age_category == '65-69':
#     new_instance[:,3]=67
# if age_category == '75-79':
#     new_instance[:,3]=77
# if age_category == '40-44':
#     new_instance[:,3]=42
# if age_category == '70-74':
#     new_instance[:,3]=72
# if age_category == '60-64':
#     new_instance[:,3]=62
# if age_category == '50-54':
#     new_instance[:,3]=52
# if age_category == '45-49':
#     new_instance[:,3]=47
# if age_category == '18-24':
#     new_instance[:,3]=21
# if age_category == '35-39':
#     new_instance[:,3]=37
# if age_category == '30-34':
#     new_instance[:,3]=32
# if age_category == '25-29':
#     new_instance[:,3]=27

# # Radio buttons
# smoking = st.radio("Do you smoke?",("Yes","No"))
# if smoking == "No":
#     new_instance[:,6]=1 #Smoking_No=True=1
#     new_instance[:,7]=0 #Smoking_Yes=False=0
# else:
#     new_instance[:,6]=0 
#     new_instance[:,7]=1 