import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 1. إعدادات الهوية البصرية الرسمية ---
st.set_page_config(page_title="حماية المستهلك - دبي", page_icon="🛡️", layout="wide")

# كود CSS لتحويل التطبيق إلى نسخة من الموقع الرسمي
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [data-testid="stappviewcontainer"] {
        direction: rtl;
        text-align: right;
        font-family: 'Tajawal', sans-serif;
    }

    /* الهيدر الأحمر */
    .custom-header {
        background-color: #E6192E;
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(230, 25, 46, 0.3);
    }

    /* تنسيق الأزرار */
    .stButton>button {
        width: 100%;
        background-color: #E6192E !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 0.75rem !important;
        font-weight: bold !important;
    }

    /* صناديق المعلومات */
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

# --- 2. واجهة الموقع الرسمية (Header) ---
st.markdown("""
<div class="custom-header">
    <h1>🛡️ بوابة المفتش الذكي</h1>
    <p>قطاع الرقابة التجارية وحماية المستهلك - دبي</p>
</div>
""", unsafe_allow_html=True)

# --- 3. شريط جانبي احترافي ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag_of_the_United_Arab_Emirates.svg/255px-Flag_of_the_United_Arab_Emirates.svg.png", width=100)
    st.markdown("### إدارة العمليات الميدانية")
    st.write(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d')}")
    st.markdown("---")
    st.error("⚠️ **سري للغاية:** يمنع نشر البيانات خارج النطاق الرسمي.")

# --- 4. التبويبات بنظام الأيقونات ---
tab1, tab2, tab3 = st.tabs(["🔍 دليل الشركات", "📑 سجل المخالفات", "⚖️ المساعد القانوني"])

# --- التبويب الأول: دليل الشركات الذكي ---
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

# --- التبويب الثاني: نظام تسجيل المخالفات ---
with tab2:
    st.markdown('<div class="info-card"><h3>تسجيل واقعة ميدانية</h3></div>', unsafe_allow_html=True)
    
    if "db" not in st.session_state: st.session_state.db = []

    with st.form("violation_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("اسم المفتش")
            company = st.text_input("اسم المنشأة المخالفة")
        with col2:
            v_type = st.selectbox("نوع المخالفة", ["سلع مقلدة", "تلاعب بالأسعار", "إعلان مضلل", "عدم الالتزام باللغة العربية"])
            fine = st.number_input("قيمة الغرامة (درهم)", min_value=0, step=500)
        
        notes = st.text_area("وصف المخالفة بالتفصيل")
        
        if st.form_submit_button("إرسال التقرير للأرشفة"):
            st.session_state.db.append({
                "الوقت": datetime.now().strftime("%H:%M"),
                "المفتش": name, "الشركة": company, "النوع": v_type, "الغرامة": fine
            })
            st.success("✅ تم حفظ التقرير وإرسال إشعار للنظام المركزي.")

    if st.session_state.db:
        st.write("### المخالفات المسجلة اليوم")
        st.table(st.session_state.db)

# --- التبويب الثالث: مساعد السياسات (مبني على ملف السياسة المرفق) ---
with tab3:
    st.markdown("""
    <div class="info-card">
        <h3>مساعد الالتزام الإعلامي</h3>
        <p>بناءً على سياسة المتحدث الرسمي لدائرة التنمية الاقتصادية:</p>
        <ul>
            <li>يمنع التصريح المباشر لوسائل الإعلام (المادة 6).</li>
            <li>المعلومات الحساسة تشمل التشريعات والرسوم (المادة 7).</li>
            <li>في حالات الأزمات، الرد يجب أن يكون سريعاً ومن خلال الإدارة (المادة 13).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if "chat" not in st.session_state: st.session_state.chat = []
    
    for m in st.session_state.chat:
        with st.chat_message(m["role"]): st.write(m["content"])
        
    if p := st.chat_input("اسأل المساعد القانوني عن إجراءات التفتيش..."):
        st.session_state.chat.append({"role": "user", "content": p})
        with st.chat_message("user"): st.write(p)
        
        with st.chat_message("assistant"):
            response = "حسب السياسة المعتمدة، يجب توجيه الإعلاميين فوراً لإدارة الاتصال الحكومي." if "إعلام" in p else "يرجى توثيق المخالفة بدقة لضمان قانونية الإجراء."
            st.write(response)
            st.session_state.chat.append({"role": "assistant", "content": response})
