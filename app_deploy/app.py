import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
 
# loading the trained model
pickle_in = open('model.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Age, CreditScore, EstimatedSalary):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0

    data = {'X2':[Gender],'X3':[Age],'X4':[CreditScore],'X5':[EstimatedSalary]}
    data = pd.DataFrame(data)
    data = pd.DataFrame(StandardScaler().fit_transform(data),columns = data.columns)    
 
    # Making predictions 
    prediction = classifier.predict(data)
     
    if prediction == 0:
        pred = 'Not Churn'
    else:
        pred = 'Churn'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Customer Churn Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Age = st.number_input("Age") 
    CreditScore = st.number_input("Credit Score") 
    EstimatedSalary = st.number_input("Estimated Salary")
    HasCrCard = st.selectbox('Has Credit Card?',("Yes","No"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Age, CreditScore, EstimatedSalary) 
        st.success('Customer is {}'.format(result))
        print('Gender: ',Gender)
        print('Age: ', Age)
        print('CreditScore: ', CreditScore)
        print('EstimatedSalary: ',EstimatedSalary)
        print('Prediction: Customer is ',result)
     
if __name__=='__main__': 
    try:
        main()
    except KeyboardInterrupt:
        clean_up()
        sys.exit(0)