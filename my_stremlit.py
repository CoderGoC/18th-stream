import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns


st.write("# My first code")


st.write("# My second header")

df = pd.read_csv("ds_salaries_clean.csv")

st.line_chart(df["Salary_USD"])
bin = st.select_slider(
    "select bin number",
    options=list(range(1, 26)))
st.write("My favorite color is", bin)

fig, ax = plt.subplots()
sns.histplot(df['Salary_USD'], bins=bin, ax=ax)

st.pyplot(fig)

genre = st.radio(
    label = "Tajriba Darajasini Tanlang",
    options = df['Experience'].unique().tolist(),
    index=None,
)

if st.button("Jadvalni Ko'rsat"):
    # st.write("Why hello there")
    st.write("You selected:", genre)
    
    st.dataframe(df[df["Experience"]==genre])
else:
    pass

with st.sidebar:
    
    st.line_chart(df["Salary_USD"])
    
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")


tab1, tab2, tab3 = st.tabs(["Mushu", "Kuchu", "Ukku"])


with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
   st.image("https://yt3.googleusercontent.com/cLOWEn8IJcc3L2Dg8DcAi2Yb8qj3vRW4VcgCJFrvuvwn8XFR_dHq2ZX_oeCClKjuLEuxdqbHmg=s900-c-k-c0x00ffffff-no-rj", width=200)


with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   