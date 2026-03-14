import streamlit as st
import pandas as pd

# إعدادات الصفحة والتنسيق العربي (RTL)
st.set_page_config(page_title="نظام دبي الذكي", layout="centered")

st.markdown("""
    <style>
    div[data-testid="stAppViewContainer"] { direction: rtl; text-align: right; }
    div.block-container { padding-top: 2rem; }
    input { direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ نظام حماية المستهلك الذكي")

# القائمة الجانبية
st.sidebar.title("إعدادات النظام")
st.sidebar.info("هذا التطبيق مخصص لمفتشي حماية المستهلك في دبي.")

# التبويبات (Tabs) لتنظيم الواجهة
tab1, tab2 = st.tabs(["🔍 دليل الشركات", "💬 مساعد المفتش (Chat)"])

with tab1:
    st.subheader("البحث في أرقام الشركات")
    uploaded_file = st.file_uploader("ارفع ملف الإكسل (Excel)", type=["xlsx"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        search = st.text_input("ابحث عن اسم الشركة:")
        if search:
            # كود البحث الذكي في كل الأعمدة
            mask = df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)
            results = df[mask]
            st.dataframe(results, use_container_width=True)
        else:
            st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("الدردشة الذكية")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض الرسائل القديمة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # إدخال رسالة جديدة
    if prompt := st.chat_input("كيف يمكنني مساعدتك؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = f"جاري معالجة طلبك بخصوص: {prompt}. نظام البحث جاهز لمساعدتك."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
