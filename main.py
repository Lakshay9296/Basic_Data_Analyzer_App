import streamlit as st
import pandas as pd

st.title("Simple Data Analyser")

file= st.file_uploader("Upload a CSV file",type='csv')

if file is not None:
    df= pd.read_csv(file)
    
    st.subheader("File Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filters")
    columns=df.columns.to_list()
    selected_column= st.selectbox("Select Column to Filter by",columns)
    values= df[selected_column].unique()
    selected_value= st.selectbox("Select a Value",values)
    filtered_df= df[df[selected_column]==selected_value]
    st.write(filtered_df)
    
    csv_data= filtered_df.to_csv(index=False)
    st.download_button("Save Filtered CSV",csv_data,file_name='filter.csv')
    
    st.subheader("Plot")
    x = st.selectbox("Select X Axis Column",columns)
    y = st.selectbox("Select Y Axis Column",columns)
    button= st.button("Generate Plot")
    if button:
        st.bar_chart(df.set_index(x)[y])
        
else:
    st.write("Waiting for file upload....")