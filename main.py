import pandas as pd
import streamlit as st

# Ma'lumotlar
data = {
    "Ismlar": ["Ali", "Vali", "Hasan", "Husan", "Rustam"],
    "Yoshlar": [20, 25, 30, 35, 40],
    "Shaharlar": ["Toshkent", "Samarqand", "Buxoro", "Qarshi", "Andijon"]
}

# Dataframe yaratish
df = pd.DataFrame(data)

# Streamlit foydalanuvchiga interfeys yaratish
st.title("Ma'lumotlar Jadvalli")
st.write("Jadvallga qidirish va tartiblash imkoniyati mavjud.")

# Qidirish qismi
search_input = st.text_input("Qidirish")

# Jadvallni chiqarish
st.write(df[df["Ismlar"].str.contains(search_input, case=False)])

# Jadvallni tartiblash qismi
st.write("Jadvallni tartiblash:")
columns = df.columns.tolist()
selected_column = st.selectbox("Tartiblash uchun stolni tanlang", columns)
order = st.selectbox("Tartiblash usuli", ["Asosan katta", "Asosan kichik"])
if st.button("Tartiblash"):
    if order == "Asosan katta":
        st.write(df.sort_values(by=selected_column, ascending=False))
    elif order == "Asosan kichik":
        st.write(df.sort_values(by=selected_column, ascending=True))
```

Bu kodda, Streamlit kutubxonasidan foydalanib, ma'lumotlar jadvalli yaratiladi. Foydalanuvchi interfeysida qidirish qismi mavjud bo'lib, u ma'lumotlar jadvallida qidirish imkoniyatiga ega. Shuningdek, jadvallni tartiblash qismi mavjud bo'lib, u foydalanuvchi interfeysida tartiblash uchun stolni tanlash va tartiblash usulini tanlash imkoniyatiga ega.
