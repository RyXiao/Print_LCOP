import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="centered", page_title="Printer Eco-calculator")
st.markdown("## Printer Cost Calculator")

global total_cost, paper_cost, ink_cost, paper_num, cost_perpage

paper_num = st.number_input('Input the page your printed', step=100)
paper_cost = paper_num * 0.07
st.write('Page Expenditure: ', round(paper_cost, 2))

printer_list = ["EPSON L4168"]
printer_selected = st.selectbox("Please Select Your Printer", printer_list)

if printer_selected == 'EPSON L4168':
    price = 1599

#
# def auto_cal():
#
#     total_cost = paper_cost + ink_cost + price
#     cost_perpage = round(total_cost / paper_num, 4)

# ink_cost = st.number_input('Input your expenditure of Ink',value = 289, step=1, on_change=auto_cal)
ink_cost = st.number_input('Input your expenditure of Ink', value=289, step=1)
st.write('Ink Expenditure', ink_cost)

if paper_num == 0:
    paper_num = 1

total_cost = paper_cost + ink_cost + price
total = st.write('The total cost is ', total_cost)
cost_perpage = round(total_cost / paper_num, 4)
st.write('The cost of every single page is ', cost_perpage)





if st.button('Reset'):
    paper_num = 6000
    ink_cost = 289

j=[]

for i in range(1000, 100000, 100):
    j.append((i*0.07+price+289/8000*i)/i)


chart_data = {"Num":range(1000,100000,100),"Cost":j}

data = pd.DataFrame(chart_data)
data.head()

fig = px.scatter(data, x="Num", y="Cost")
st.plotly_chart(fig, use_container_width=True)