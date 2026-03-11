import streamlit as st

st.set_page_config(page_title="حماية المستهلك - دبي", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    h1, h2, h3 { color: #E5152E; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #E5152E; color: white; font-weight: bold; }
    .stButton>button:hover { background-color: #A6192E; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ نظام مفتشي حماية المستهلك")
st.subheader("دائرة الاقتصاد والسياحة - دبي | قسم المتابعة (DET)")

tab1, tab2, tab3, tab4 = st.tabs(["⚖️ القرار الذكي", "💰 الغرامات", "📚 التشريع", "📖 عن التطبيق"])

with tab1:
    st.write("### مصفوفة القرارات الفورية")
    sector = st.selectbox("اختر القطاع المستهدف:", ["السيارات", "الإلكترونيات", "التجزئة", "المطاعم", "الأثاث"])
    cases = { ... }  # (الكود كامل من الرسالة السابقة - أكمله من هناك)
    # باقي الكود كامل من النسخة 1.2 اللي أعطيتك إياها قبل شوي

with tab4:
    st.write("### 📖 عن التطبيق")
    st.markdown("""
    🛡️ **نظام مفتشي حماية المستهلك**  
    تطبيق داخلي رسمي لقسم المتابعة في **دائرة الاقتصاد والسياحة - دبي**.  
    يعتمد على اللائحة التنفيذية رقم 66 لسنة 2023.  
    **النسخة الذهبية 1.2** - رقم المفتش: DXB-990
    """)

# باقي الأقسام (tab2, tab3, sidebar) كاملة من الكود السابق