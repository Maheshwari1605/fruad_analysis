import pandas as pd
import streamlit as st 
from pickle import load
import base64
from sklearn.preprocessing import LabelEncoder

st.image("excelr.png")


      
    # display the front end aspect



html_temp = """ 
    <div>
    <h1 style ="color:green;;"> Project Mentor : Vinod</h1> 
    </div> 
    """
      
    # display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True)

    # display the front end aspect



if st.button("About Project"):
         st.text("Building a model that detect Health insurance  Fruad  using  Machine Learning")

if st.checkbox("Team Member"):
    
 
 st.text("Priyanka")
 st.text("Maheshwari")
 st.text("Tejaswini")               
 st.text("Abhijit" )
 st.text ("Sanu") 

 st.text ("Adil")


html_temp = """ 
    <div style ="background-color:pink;padding:5px"> 
    <h1 style ="color:black;text-align:center;">Insurance Fraud Detection </h1> 
    </div> 
    """

st.markdown(html_temp, unsafe_allow_html = True)       



def user_input_features():
 
    Age = st.selectbox("Age ",('0 to 17', '18 to 29', '30 to 49', '50 to 69', '70 or Older'))
    Gender = st.selectbox('Gender',('Male','Female'))
  
  
    Admission_type =  st.selectbox('Admission Type',('Elective', 'Emergency', 
                                                      'Newborn', 'Not Available', 'Trauma','Urgent'))
    Hospital_County = st.selectbox('Hospital County',('Allegany','Chautauqua','Erie','Niagara','Orleans','Wyoming','Wyoming','Livingston','Monroe','Ontario','Steuben','Wayne','Oswego','Cayuga','Cortland','Jefferson','Madison','Onondaga','St Lawrence','Tompkins','Albany','Clinton','Columbia','Delaware','Franklin','Fulton ','Montgomery','Otsego','Rensselaer','Saratoga','Schenectady','Warren','Dutchess','Orange','Putnam','Rockland','Sullivan','Ulster','Westchester','Bronx','Rockland','Sullivan'))
    Payment_Typology=st.selectbox('Payment Typology',(1,2,3,4,5))
    emergency_dept= st.selectbox('Emergency Dept',('Yes','No'))  
    home_or_selfcare=st.selectbox('Home or Selfcare',('Home/Self care','Another Type','Cancer Center','Court/Law Enforcement','Critical Access','Expired','Facility','Federal','HHS','Hosp-Medicare','Hospice-Home','Hospice-Medical','Inpatient','Lef-Advice','MedicAid-Nursing','Medicare-Long Term','Psychiatric','Short-term','Skilled'))
    mortalityrisk=st.selectbox('mortalityrisk',(1,2,3,4))
    
    code_illness =st.selectbox("Code illness",(0,1,2,3,4))
    ccs_diagnosis_code = st.number_input(" Diagnosis Code")
    Tot_charg =  st.number_input("Total Charge")
    Days_spend_hsptl = st.number_input("Days Spend in hospital")
    css_procedure_code=st.number_input("Procedure Code")
   
   
   
    ratio_ofcost_to_charge=st.number_input("Ratio of cost to charge")

        

  
  
    
    data = {
        'Age':Age,
        'Gender':Gender,
        'Hospital_County':Hospital_County,
        'Days_spend_hsptl':Days_spend_hsptl,
        'Admission_type':Admission_type,
        'ccs_diagnosis_code':ccs_diagnosis_code,
       
        'Tot_charg':Tot_charg, 
        'css_procedure_code':css_procedure_code,
        'home_or_selfcare': home_or_selfcare,
        'Payment_Typology': Payment_Typology,

        'code_illness ':code_illness,
        'emergency_dept':emergency_dept,
        'ratio_ofcost_to_charge':ratio_ofcost_to_charge,
 
        'mortalityrisk':mortalityrisk,
        }
    
    features = pd.DataFrame(data,index = [0])
    
    
    return features

df = user_input_features()

st.write(df)

lst = ['Age','Gender','Hospital_County','Tot_charg','Admission_type','Days_spend_hsptl',
       'ccs_diagnosis_code', 'mortalityrisk','ratio_ofcost_to_charge','emergency_dept', 'Payment_Typology','home_or_selfcare','css_procedure_code']

for i in lst:
   df[i] = LabelEncoder().fit_transform(df[i])
    

#loading model 
loaded_model=load(open('model_Final' ,'rb'))

prediction_proba = loaded_model.predict_proba(df)


prediction = loaded_model.predict(df)






if st.button("Predict"): 

 ('Claim: Genuine :thumbsup:' if  prediction_proba[0][1] > 0.48 else 'Claim: Fraud:thumbsdown:')


st.write("\n")
st.write("\n")





