

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt
from datetime import date
import base64
import collections
from vega_datasets import data
#random orange background color
components.html(
    """
    <body style="background-color:#ffcc00"
    </body>
    """
    )

st.title("⭐Towards a Better Spark UI⭐")
st.text("An Interactive Visualization")

st.markdown("---")
st.markdown("_**Welcome!**_" )
#st.markdown(" Stuff...and more stuff.")



#import altair as alt
source = data.movies.url
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    opacity: 1;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
st.set_page_config(layout="wide")
st.title("A Better Spark User Interface")
st.markdown("""
 * Use the menu at left to select data and set plot parameters
 * Your plots will appear below
""")


st.sidebar.markdown("## Select Optimization")
set_png_as_page_bg('apache-spark1.jpg')

#st.sidebar.markdown('#### Q-tranform plot')
#vmax = st.sidebar.slider('Colorbar Max Energy', 10, 500, 25)  # min, max, default
#qcenter = st.sidebar.slider('Data', 5, 120, 5)  # min, max, default
#qrange = (int(qcenter*0.8), int(qcenter*1.2))

task = st.selectbox(
        "Which problem do you want to Visualize?", ["Word Count","Spark for ML","Apply Optimizations to an Extract, Transform, Load (ETL) job"])
plot=alt.Chart(source).mark_bar().encode(
    alt.X("IMDB_Rating:Q"),
    y='count()',
    
).properties(width=400,
    height=200)
data_spill_button=st.sidebar.radio("Show data spill to memory and disk",("Yes","No"))

suffle_read_button=st.sidebar.radio("Show shuffle read and write quantities",("Yes","No"))

Dataio_button=st.sidebar.radio("Show data input and output",("Yes","No"))
#row2_1, row2_2, row2_3, row2_4 = st.beta_columns((2,1,1,1))
st.write("** Please select a checkbox to implement one or more optimization**")
if st.checkbox("Optimization 1"):
    #TODO
    st.write("Implement Optimization 1 on Data Set")
    
if st.checkbox("Optimization 2"):
    #TODO
    st.write("Implement Optimization 2 on Data Set")
    
    
if st.checkbox("Optimization 3"):
    #TODO 
    st.write("Implement Optimization 3 on Data Set")
      

col1, col2, col3 = st.beta_columns(3)
if data_spill_button=="Yes":
    col1.header("Data Spill to Memory and Disk")
    col1.write(plot)
    #row2_1, row2_2, row2_3 = st.beta_columns((2,1,1))

if suffle_read_button=="Yes":
    col2.header("Shuffle Read and Write")
    col2.write(plot)
if Dataio_button=="Yes":
    col3.header("Data input and output")
    col3.write(plot)
st.write("** Display Data after Optimizations**")
optimized=st.radio("",("Yes","No"))
if optimized=="Yes":
    st.write(plot.properties(width=600,height=300))
#colapsible grouping, only shows items one at a time
#components.html(
#    """
#    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
#    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#    <div id="accordion">
#      <div class="card">
#        <div class="card-header" id="headingOne">
#          <h5 class="mb-0">
#            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
#            Team Members
#            </button>
#          </h5>
#        </div>
#        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
#          <div class="card-body">
#            Andre
#          </div>
#          <div class="card-body">
#            Catalina
#          </div>
#          <div class="card-body">
#            Janice
#          </div>
#          <div class="card-body">
#            Riddhiman
#          </div>
#        </div>
#      </div>
#      <div class="card">
#        <div class="card-header" id="headingTwo">
#          <h5 class="mb-0">
#            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
#            Random List of Stuff
#            </button>
#          </h5>
#        </div>
#        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
#          <div class="card-body">
#            First thing
#          </div>
#        </div>
#      </div>
#    </div>
    """,
#    height=500,
#)

#---A search field to nowhere example -css makes the blue background---#

#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#def remote_css(url):
#    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

#def icon(icon_name):
#    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

#local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

#icon("outdoor_grill") #use word list of google icons: https://fonts.google.com/icons
#selected = st.text_input("", "This text input bar goes nowhere right now...")
#button_clicked = st.button("OK")

#-----------------------------------------_
