import streamlit as st

st.write("""
# Subtraction of Two Numbers App

This app subtracts the two numbers given by input
""")

# Get Input

st.header('User Input Parameters')


def user_input_two_nums():
    first_num = st.number_input('Enter the 1st Number ')
    second_num = st.number_input('Enter the 2nd Number ')

    data = {'First Number': first_num,
            'Second Number': second_num
            }
    return (data)


data = user_input_two_nums()


f_no, s_no = data['First Number'], data['Second Number']
result = float(f_no) - float(s_no)
if (st.button('Subtract')):
    st.write("RESULT!!!")
    st.write("Subtraction of 2nd Num from 1st Num = ", f_no-s_no)

    data['Result'] = result
    st.subheader('User Input parameters')
    st.write(data)
