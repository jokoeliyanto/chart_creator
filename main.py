import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(page_title="Chart Creator", page_icon=":bar_chart:", layout="wide")

st.write("""

# Hobi Data Chart Creator Ver 0.0 

Here the dataframe for your visualisations

""")

df = pd.read_csv('supermarket.csv')

st.dataframe(df)

# ---- SIDEBAR ----
st.sidebar.header("Create Your First Chart:")

# Data Type Selection

x_axis = st.sidebar.selectbox(
    "Select the X Axis:",
    options=df.select_dtypes(exclude=np.number).columns)

y_axis = st.sidebar.selectbox(
    "Select the Y Axis:",
    options=df.select_dtypes(include=np.number).columns)

Choices = {"sum":"Sum", np.mean:"Mean", "median":"Median"}

formula = st.sidebar.selectbox(
    "Select the Formula:",
    options=Choices.keys(),
    format_func=lambda x: Choices[x])



# ---- MAINPAGE ----
st.header(":bar_chart: Bar Chart")
st.markdown("##")


# -- DATA PREPARATION --
df_use = df.groupby(x_axis).agg({y_axis:formula}).reset_index()

fig, ax = plt.subplots()
ax = plt.bar(df_use[x_axis], df_use[y_axis])

plt.xlabel(str.upper(df_use.columns[0]), fontweight='bold')
plt.ylabel(str.upper(df_use.columns[1]), fontweight='bold')
plt.title('Bar Chart of {} x {}'.format(df_use.columns[0], df_use.columns[1]) , loc='center')

st.pyplot(fig)