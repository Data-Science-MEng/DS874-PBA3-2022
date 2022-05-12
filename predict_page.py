import streamlit as st
import pickle 
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data 

data = load_model()
rf_model_loaded = data["model"]

def show_predict_page():

    st.title("Are you at risk of having heart disease? 💔")
    
    # defining a new instance - will be the user's input
    new_instance = np.array([[0.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

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

    #  14  Sex_Female                           
    #  15  Sex_Male 
    Sex = st.radio("What is your sex?",("Female","Male"))
    if Sex == "Female":
        new_instance[:,14]=1 #Sex_Female=True=1
        new_instance[:,15]=0 #Sex_Male=False=0
    else:
        new_instance[:,14]=0 
        new_instance[:,15]=1 
    #st.write(new_instance)

    #  0   BMI - Text input 
    BMI = st.number_input("What is your BMI? (2 decimals is enough info and you need to use a comma ' , ' not a fullstop ' . ')",min_value=0.0, max_value=90.0,format="%.2f")
    new_instance[:,0]=(BMI-12.02)/(94.85-12.02)
    #st.write(new_instance)

    #  1   PhysicalHealth                       
    PhysicalHealth = st.number_input("How many days, over the last 30 days, was your physical health not good?",min_value=0, max_value=30,step=1)
    new_instance[:,1]=(PhysicalHealth-0.0)/(30.0-0.0)
    #st.write(new_instance)

    #  2   MentalHealth                         
    MentalHealth = st.number_input("How many days, over the last 30 days, was your mental health not good?",min_value=0, max_value=30,step=1)
    new_instance[:,2]=(MentalHealth-0.0)/(30.0-0.0)
    #st.write(new_instance)

    #  3   AgeCategory                          
    age_category = st.selectbox("How old are you?", ['18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older'])
    if age_category == '55-59':
        new_instance[:,3]=(57-21)/(80-21)
    if age_category == '80 or older':
        new_instance[:,3]=(80-21)/(80-21)
    if age_category == '65-69':
        new_instance[:,3]=(67-21)/(80-21)
    if age_category == '75-79':
        new_instance[:,3]=(77-21)/(80-21)
    if age_category == '40-44':
        new_instance[:,3]=(42-21)/(80-21)
    if age_category == '70-74':
        new_instance[:,3]=(72-21)/(80-21)
    if age_category == '60-64':
        new_instance[:,3]=(62-21)/(80-21)
    if age_category == '50-54':
        new_instance[:,3]=(52-21)/(80-21)
    if age_category == '45-49':
        new_instance[:,3]=(47-21)/(80-21)
    if age_category == '18-24':
        new_instance[:,3]=(21-21)/(80-21)
    if age_category == '35-39':
        new_instance[:,3]=(37-21)/(80-21)
    if age_category == '30-34':
        new_instance[:,3]=(32-21)/(80-21)
    if age_category == '25-29':
        new_instance[:,3]=(27-21)/(80-21)
    #st.write(new_instance)
    
    #  16  Race_American Indian/Alaskan Native   
    #  17  Race_Asian                             
    #  18  Race_Black                             
    #  19  Race_Hispanic                          
    #  20  Race_Other                           
    #  21  Race_White   
    Race = st.selectbox("Please select your race", ['American Indian / Alaskan Native','Asian','Black','Hispanic','White','Other'])
    if Race == 'American Indian / Alaskan Native':
        new_instance[:,16]=1
        new_instance[:,(17,18,19,20,21)]=0
    if Race == 'Asian':
        new_instance[:,17]=1
        new_instance[:,(16,18,19,20,21)]=0
    if Race == 'Black':
        new_instance[:,18]=1
        new_instance[:,(16,17,19,20,21)]=0
    if Race == 'Hispanic':
        new_instance[:,19]=1
        new_instance[:,(16,17,18,20,21)]=0
    if Race == 'Other':
        new_instance[:,20]=1
        new_instance[:,(16,17,18,19,21)]=0
    if Race == 'White':
        new_instance[:,21]=1
        new_instance[:,(16,17,18,19,20)]=0
    #st.write(new_instance)
    
    #  4   GenHealth 
    GenHealth = st.radio("How would you rate your general health?",("Poor","Fair", "Good","Very good","Excellent"))
    if GenHealth == "Poor":
        new_instance[:,4]=0 
    if GenHealth == "Fair":
        new_instance[:,4]=0.25 
    if GenHealth == "Good":
        new_instance[:,4]=0.5 
    if GenHealth == "Very good":
        new_instance[:,4]=0.75    
    if GenHealth == "Excellent":
        new_instance[:,4]=1     
    #st.write(new_instance)                     

    #  5   SleepTime                            
    SleepTime = st.number_input("How many hours of sleep do you get per day on average?",min_value=1, max_value=24,step=1)
    new_instance[:,5]=(SleepTime-1.0)/(24.0-1.0)
    #st.write(new_instance)

    #  6   Smoking_No                           
    #  7   Smoking_Yes    
    smoking = st.radio("Do you smoke? Or have you smoked over 5 packs of cigarettes in your lifetime?",("Yes","No"))
    if smoking == "No":
        new_instance[:,6]=1 #Smoking_No=True=1
        new_instance[:,7]=0 #Smoking_Yes=False=0
    else:
        new_instance[:,6]=0 
        new_instance[:,7]=1 
    #st.write(new_instance)
                           
    #  8   AlcoholDrinking_No                    
    #  9   AlcoholDrinking_Yes 
    alcohol = st.radio("If you are a female, do you have more than 7 alcoholic drinks per week? If you are a male, do you have more than 14 alcoholic drinks per week?",("Yes","No"))
    if alcohol == "No":
        new_instance[:,8]=1 #Alcohol_No=True=1
        new_instance[:,9]=0 #Alcohol_Yes=False=0
    else:
        new_instance[:,8]=0 
        new_instance[:,9]=1
    #st.write(new_instance)
                             
    #  12  DiffWalking_No                        
    #  13  DiffWalking_Yes 
    DiffWalking = st.radio("Do you have difficulty walking, or climbing stairs?",("Yes","No"))
    if DiffWalking == "No":
        new_instance[:,12]=1 #DiffWalking_No=True=1
        new_instance[:,13]=0 #DiffWalking_Yes=False=0
    else:
        new_instance[:,12]=0 
        new_instance[:,13]=1  
    #st.write(new_instance)
    
    #  26  PhysicalActivity_No                   
    #  27  PhysicalActivity_Yes   
    PhysicalActivity = st.radio("Have you been physically active over the last 30 days? EXCLUDING: physical activity related to your occupation",("Yes","No"))
    if PhysicalActivity == "No":
        new_instance[:,26]=1 #PhysicalActivity_No=True=1
        new_instance[:,27]=0 #PhysicalActivity_Yes=False=0
    else:
        new_instance[:,26]=0 
        new_instance[:,27]=1 
    #st.write(new_instance)                                           
    
    #  22  Diabetic_No                            
    #  23  Diabetic_No, borderline diabetes       
    #  24  Diabetic_Yes                           
    #  25  Diabetic_Yes (during pregnancy)
    Diabetic = st.radio("What is your diabetic status?",("Not diabetic","Borderline diabetic", "Diabetic","Diabetic and pregnant"))
    if Diabetic == "Not diabetic":
        new_instance[:,22]=1 #Diabetic_No=True=1
        new_instance[:,(23,24,25)]=0
    if Diabetic == "Borderline diabetic":
        new_instance[:,23]=1 
        new_instance[:,(22,24,25)]=0
    if Diabetic == "Diabetic":
        new_instance[:,24]=1 
        new_instance[:,(22,23,25)]=0
    if Diabetic == "Diabetic and pregnant":
        new_instance[:,25]=1 
        new_instance[:,(22,23,24)]=0
    #st.write(new_instance)
    
    #  10  Stroke_No                             
    #  11  Stroke_Yes 
    stroke = st.radio("Have you ever had a stroke?",("Yes","No"))
    if stroke == "No":
        new_instance[:,10]=1 #Stroke_No=True=1
        new_instance[:,11]=0 #Stroke_Yes=False=0
    else:
        new_instance[:,10]=0 
        new_instance[:,11]=1   
    #st.write(new_instance)             
    
    #  28  Asthma_No                             
    #  29  Asthma_Yes  
    Asthma = st.radio("Do you have asthma?",("Yes","No"))
    if Asthma == "No":
        new_instance[:,28]=1 #Asthma_No=True=1
        new_instance[:,29]=0 #Asthma_Yes=False=0
    else:
        new_instance[:,28]=0 
        new_instance[:,29]=1  
    #st.write(new_instance)     
                        
    #  30  KidneyDisease_No                     
    #  31  KidneyDisease_Yes 
    KidneyDisease = st.radio("Have been diagnosed with kidney disease? EXCLUDING: kidney stones, bladdar infection, and incontinence",("Yes","No"))
    if KidneyDisease == "No":
        new_instance[:,30]=1 #KidneyDisease_No=True=1
        new_instance[:,31]=0 #KidneyDisease_Yes=False=0
    else:
        new_instance[:,30]=0 
        new_instance[:,31]=1 
    #st.write(new_instance)      
                     
    #  32  SkinCancer_No                        
    #  33  SkinCancer_Yes                       
    SkinCancer = st.radio("Do you have skin cancer?",("Yes","No"))
    if SkinCancer == "No":
        new_instance[:,32]=1 #SkinCancer_No=True=1
        new_instance[:,33]=0 #SkinCancer_Yes=False=0
    else:
        new_instance[:,32]=0 
        new_instance[:,33]=1    
    #st.write(new_instance) 

    to_predict_or_not_to_predict = st.button("Predict heart disease likelihood")
    if to_predict_or_not_to_predict:
        prediction = rf_model_loaded.predict(new_instance)
        #prediction = rf_model_loaded.predict(np.array([[0.372570,  0.166667,  0.000000,  0.271186,  0.50,  0.173913,  0.0,  1.0,  1.0,  0.0, 1.0,  0.0 , 1.0 , 0.0 , 0.0 , 1.0,  0.0 , 0.0 , 0.0 , 0.0,  0.0 , 1.0,  1.0,  0.0,  0.0, 0.0,  0.0 , 1.0,  0.0,  1.0,  1.0,  0.0,  0.0,  1.0]]))
        #st.write(prediction)
        #st.write(prediction[0])
        #st.write(new_instance)
        #prediction = 0 # predicts 0 for no heart disease
        #prediction = [1] # predicts 1 for yes heart disease
        if prediction[0]:
            st.warning("Heart disease predicted 💔" )
        else: 
            st.success("No heart disease predicted! ❤️")


    st.write("Disclaimer: These results are not an official diagnosis. If you have physical health or mental health concerns contact your health care provider. This page was generated for the purpose of a university assignment.")
    url = "https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease"
    st.write("These results are generated by providing a Random Forest Machine Learning model with your answers. This model was trained using a 2020 Heart Disease dataset, avaiable [here](%s)." % url)