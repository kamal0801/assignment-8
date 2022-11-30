import streamlit as st

st.write("""
# Finding multiplication of the 2 input parameters
""")
# Get Input
st.header('User Input Parameters')
def user_input_features():
  number1=st.number_input("Input 1st number here :")
  number2=st.number_input("Input 2nd number here :")
  
  data={'number1':number1,'number2':number2}
 
  multiply = number1 * number2

  return multiply

df = user_input_features()
st.write('Multiplication answer :')
st.write(df)



