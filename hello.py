import pandas as pd
import streamlit as st
import mysql.connector

connection = mysql.connector.connect(**st.secrets)

if connection.is_connected()==False:
    print("Not Connected")
if connection.is_connected()==True:
    print("Connected")

def create_user_df():
    df = pd.read_sql_query("select  * from mytable", connection)
    return df
df=create_user_df()

st.write("Hello World")
st.write(df)
