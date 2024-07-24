import streamlit as st

st.title("Marks Calc")
st.write("Enter your midterm and assignment scores to find out the marks you need to achieve your desired Grade.")
x = st.slider('Mid 1',0,20)
y=st.slider('Mid 2',0,20)
q=st.slider('Quiz + OBT',0,5)
a=st.slider('Assignment',0,5)
st.write(f'Mid Average: {(x+y)/2}')
cie=(x+y)/2+q+a
st.write(f'CIE total:{cie}')

grades = {
    'A+': 90,
    'A': 80,
    'B': 70,
    'C': 60,
    'D': 50,
    'E': 40
}

option = st.selectbox("What grade are you aiming for?", ('Select a Grade', 'A+', 'A', 'B', 'C', 'D', 'E'))

if option!='Select a Grade':
    required_marks = grades[option] - cie
    if required_marks > 70:
        st.write(f"Given your current CIE score, it is not feasible to obtain the grade you chose, as you would need a score greater than 70. Required Marks:{required_marks}.")
    else:
        st.write(f"You require a minimum of {required_marks} marks to achieve grade {option}.")
