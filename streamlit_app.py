import streamlit as st
import pandas as pd
from datetime import datetime

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="حماية المستهلك - دبي", page_icon="🛡️", layout="centered")

# تنسيق الواجهة لتناسب اللغة العربية (RTL)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    div.stButton > button { width: 100%; border-radius: 10px; height: 3em; background-color: #D32F2F; color: white; }
    .stSelectbox label, .stTextInput label { text-align: right; display: block; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ نظام مفتشي حماية المستهلك")
st.subheader("دائرة الاقتصاد والسياحة - دبي")
st.info(f"تاريخ اليوم: {datetime.now().strftime('%Y-%m-%d')}")

# الأقسام الرئيسية
tab1, tab2, tab3 = st.tabs(["⚖️ إصدار قرار", "📸 توثيق ميداني", "📊 إحصائيات"])

with tab1:
    st.write("### 📝 تفاصيل المخالفة")
    inspector_name = st.text_input("اسم المفتش:")
    sector = st.selectbox("القطاع المستهدف:", ["السيارات", "التجزئة (هايبرماركت)", "المطاعم والمقاهي", "الإلكترونيات"])
    violation_type = st.selectbox("نوع التجاوز:", ["عدم وضع الأسعار", "إعلان مضلل", "سلعة مقلدة", "رفض استرجاع منتج معيب"])
    
    if st.button("تحليل الحالة وإصدار القرار"):
        if inspector_name:
            st.warning(f"تم تسجيل طلب المفتش: {inspector_name}")
            st.success("القرار: توجيه إنذار نهائي ومصادرة السلع المخالفة بناءً على القانون رقم 2 لسنة 2023.")
            st.error("الغرامة المقدرة: 10,000 درهم إماراتي.")
        else:
            st.error("يرجى إدخال اسم المفتش أولاً.")

with tab2:
    st.write("### 📷 تصوير الأدلة")
    picture = st.camera_input("التقط صورة للمخالفة من موقع الحدث")
    
    if picture:
        st.image(picture, caption="تم التقاط الدليل بنجاح", use_container_width=True)
        st.success("تم ربط الصورة بتقرير المخالفة رقم #DXB-2024-001")

with tab3:
    st.write("### 📈 ملخص الأداء اليومي")
    # بيانات تجريبية للرسم البياني
    chart_data = pd.DataFrame({
        'القطاع': ["السيارات", "التجزئة", "الإلكترونيات"],
        'المخالفات': [3, 12, 5]
    })
    st.bar_chart(chart_data.set_index('القطاع'))

st.divider()
st.caption("نظام داخلي - يحظر استخدامه من غير الموظفين المصرح لهم.")
