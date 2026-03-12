import streamlit as st
import pandas as pd

# 1. إصلاح التنسيق (RTL) ليدعم العربية بشكل ثابت
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { direction: rtl; text-align: right; }
    [data-testid="stHeader"] { direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ نظام حماية المستهلك - دبي")

# 2. إضافة التبويبات (Tabs) لتنظيم الشغل
tab1, tab2 = st.tabs(["🔍 بحث الشركات", "💬 مساعد ذكي"])

with tab1:
    st.header("دليل اتصالات الشركات")
    uploaded_file = st.file_uploader("ارفع ملف الإكسل هنا", type=["xlsx"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        search = st.text_input("اكتب اسم الشركة اللي تبحث عنها:")
        if search:
            result = df[df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)]
            st.dataframe(result)

with tab2:
    st.header("المساعد الذكي (Chat)")
    # هنا محاكاة بسيطة للشات
    user_msg = st.chat_input("كيف أقدر أساعدك اليوم؟")
    if user_msg:
        with st.chat_message("user"):
            st.write(user_msg)
        with st.chat_message("assistant"):
            st.write(f"أنا نظام ذكي، أنت سألت عن: '{user_msg}'. حالياً أقدر أبحث لك في الملفات، قريباً سأرتبط بالذكاء الاصطناعي!")
