import streamlit as st

st.set_page_config(layout="centered", page_title="Printer Eco-calculator")
st.markdown("## Printer Cost Calculator")


paper_num = st.number_input('Input the page your printed', step=100)
paper_cost = paper_num * 0.07
st.write('Page Expenditure: ', round(paper_cost, 2))

printer_list = ["EPSON L4168"]
printer_selected = st.selectbox("Please Select Your Printer", printer_list)

if printer_selected == 'EPSON L4168':
    price = 1599

ink_cost = st.number_input('Input your expenditure of Ink', step=1)
st.write('Ink Expenditure', ink_cost)

if paper_num == 0:
    paper_num = 1

total_cost = paper_cost + ink_cost + price
st.write('The total cost is ', total_cost)
cost_perpage = round(total_cost / paper_num, 4)
st.write('The cost of every single page is ', cost_perpage)


st.button('Reset')
