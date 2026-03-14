import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ────────────────────────────────────────────────
# إعدادات الصفحة والـ CSS الرسمي
# ────────────────────────────────────────────────
st.set_page_config(page_title="حماية المستهلك - دبي", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
    font-family: 'Tajawal', sans-serif;
}
.custom-header {
    background-color: #E6192E;
    color: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(230, 25, 46, 0.3);
}
.stButton > button {
    width: 100%;
    background-color: #E6192E !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 0.75rem !important;
    font-weight: bold !important;
}
.info-card {
    background: white;
    padding: 20px;
    border-right: 5px solid #E6192E;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# الهيدر الرسمي
# ────────────────────────────────────────────────
st.markdown("""
<div class="custom-header">
    <h1>🛡️ بوابة المفتش الذكي</h1>
    <p>قطاع الرقابة التجارية وحماية المستهلك - دبي</p>
</div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# الـ Sidebar
# ────────────────────────────────────────────────
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag_of_the_United_Arab_Emirates.svg/255px-Flag_of_the_United_Arab_Emirates.svg.png", width=100)
    st.markdown("### إدارة العمليات الميدانية")
    st.write(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d')}")
    st.markdown("---")
    st.error("⚠️ **سري للغاية:** يمنع نشر البيانات خارج النطاق الرسمي.")

# ────────────────────────────────────────────────
# التبويبات
# ────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🔍 دليل الشركات", "📋 سجل المخالفات", "⚖️ المساعد القانوني"])

# ────────────────────────────────────────────────
# تبويب 1: دليل الشركات
# ────────────────────────────────────────────────
with tab1:
    st.markdown('<div class="info-card"><h3>البحث في قاعدة بيانات الشركات الكبرى</h3></div>', unsafe_allow_html=True)
    
    file_path = "Contacts.xlsb"
    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path, engine='pyxlsb')
            query = st.text_input("ادخل اسم الشركة أو القطاع (مثال: كارفور، أمازون):")
            if query:
                results = df[df.astype(str).apply(lambda x: x.str.contains(query, case=False, na=False)).any(axis=1)]
                st.success(f"تم العثور على {len(results)} مسؤول اتصال")
                st.dataframe(results, use_container_width=True)
            else:
                st.dataframe(df.head(10), use_container_width=True)
        except Exception as e:
            st.error(f"خطأ تقني: {e}")
    else:
        st.warning("🔄 يرجى رفع ملف 'Contacts.xlsb' إلى المجلد الرئيسي لتفعيل البحث.")

# ────────────────────────────────────────────────
# تبويب 2: تسجيل المخالفات
# ────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="info-card"><h3>تسجيل واقعة ميدانية</h3></div>', unsafe_allow_html=True)
    
    if "violations" not in st.session_state:
        st.session_state.violations = []
    
    with st.form("violation_form"):
        col1, col2 = st.columns(2)
        with col1:
            inspector_name = st.text_input("اسم المفتش")
            company_name = st.text_input("اسم المنشأة المخالفة")
        with col2:
            violation_type = st.selectbox("نوع المخالفة", [
                "سلع مقلدة", 
                "تلاعب بالأسعار", 
                "إعلان مضلل", 
                "عدم الالتزام باللغة العربية",
                "غير ذلك (حدد في الملاحظات)"
            ])
            fine_amount = st.number_input("قيمة الغرامة (درهم)", min_value=0, step=500)
        
        notes = st.text_area("وصف المخالفة بالتفصيل")
        
        submitted = st.form_submit_button("إرسال التقرير للأرشفة")
        
        if submitted:
            if not inspector_name or not company_name:
                st.error("يرجى تعبئة اسم المفتش واسم المنشأة")
            else:
                st.session_state.violations.append({
                    "الوقت": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "المفتش": inspector_name,
                    "المنشأة": company_name,
                    "النوع": violation