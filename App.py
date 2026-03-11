import import import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="حماية المستهلك - دبي",
    page_icon="🛡️",
    layout="centered"
)

# 2. تنسيق الواجهة ودعم اللغة العربية (RTL)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    div[data-testid="stSelectbox"] label { text-align: right; width: 100%; font-weight: bold; }
    div[data-baseweb="select"] { direction: rtl; }
    button[data-baseweb="tab"] { direction: rtl; font-size: 18px; }
    h1, h2, h3 { color: #D32F2F; text-align: center; }
    .stButton>button { 
        width: 100%; border-radius: 12px; background-color: #D32F2F; 
        color: white; font-size: 18px; height: 3em; 
    }
    .stButton>button:hover { background-color: #B71C1C; color: white; }
    .stAlert { direction: rtl; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة بيانات الغرامات
fines = {
    "عدم عرض الأسعار بوضوح": 100000,
    "الامتناع عن خدمات الضمان/الإصلاح": 250000,
    "تقديم معلومات مضللة/إعلان كاذب": 200000,
    "الامتناع عن تقديم فاتورة بالعربية": 50000,
    "وضع شروط تعسفية (البضاعة لا ترد)": 100000
}

# 4. واجهة التطبيق
st.title("🛡️ نظام مفتشي حماية المستهلك")
st.subheader("دائرة الاقتصاد والسياحة - دبي")

tab1, tab2, tab3 = st.tabs(["⚖️ القرار الذكي", "💰 الحاسبة", "📚 التشريع"])

with tab1:
    st.write("### مصفوفة القرارات الفورية")
    sector = st.selectbox("اختر القطاع:", ["السيارات", "الإلكترونيات", "التجزئة", "المطاعم"])
    
    cases = {
        "السيارات": {"حالة": "تأخر التسليم ورفض رد العربون", "حكم": "نعم، يحق للمستهلك استرداد المبلغ.", "مادة": "المادة (10)"},
        "التجزئة": {"حالة": "اختلاف السعر عند الدفع عن الرف", "حكم": "البيع بالسعر الأقل المعلن.", "مادة": "المادة (7)"},
        "المطاعم": {"حالة": "إضافة رسوم خدمة غير معلنة", "حكم": "إلغاء الرسوم فوراً.", "مادة": "المادة (7)"},
        "الإلكترونيات": {"حالة": "عيب مصنعي خلال فترة الضمان", "حكم": "الاستبدال أو الإصلاح مجاناً.", "مادة": "المادة (13)"}
    }
    
    case_data = cases.get(sector)
    st.info(f"**الحالة:** {case_data['حالة']}")
    if st.button(f"أصدر القرار لقطاع {sector}"):
        st.success(f"**التوجيه:** {case_data['حكم']}")
        st.warning(f"**السند القانوني:** {case_data['مادة']}")

with tab2:
    st.write("### حاسبة الغرامات")
    violation = st.selectbox("حدد نوع المخالفة:", list(fines.keys()))
    if st.button("احسب الغرامة"):
        amount = fines[violation]
        st.error(f"قيمة الغرامة: {amount:,} درهم إماراتي")

with tab3:
    st.write("### ملخص التشريعات")
    st.markdown("""
    * **المادة 7:** الالتزام بالأسعار المعلنة.
    * **المادة 10:** حظر الشروط الجائرة.
    * **المادة 13:** ضمان العيوب المصنعية.
    """)

st.sidebar.write("إصدار المفتشين 1.1")
