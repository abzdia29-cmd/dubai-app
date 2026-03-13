 streamlit as st
imprt pandas as pd
from datetime import datetime

# --- 1. إعدادات الصفحة والهوية البصرية ---
st.set_page_config(
    page_title="منصة حماية المستهلك | اقتصادية دبي", 
    page_icon="🛡️", 
    layout="wide"
)

# تصميم CSS لضبط الألوان الرسمية (أحمر دبي) والواجهة العربية
st.markdown("""
<style>
    /* تنسيق النص من اليمين لليسار */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
        direction: rtl;
        text-align: right;
    }
    
    /* أزرار باللون الأحمر الرسمي */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        background-color: #E6192E;
        color: white;
        border: none;
        font-weight: bold;
        height: 3em;
    }

    /* صناديق التنبيه الخاصة بالسياسة */
    .policy-box {
        padding: 20px;
        background-color: #fdf2f2;
        border-right: 6px solid #E6192E;
        border-radius: 4px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. القائمة الجانبية (Sidebar) ---
with st.sidebar:
    # شعار حكومة دبي / علم الإمارات
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag_of_the_United_Arab_Emirates.svg/255px-Flag_of_the_United_Arab_Emirates.svg.png", width=100)
    st.title("نظام المفتش الذكي 👮")
    st.write(f"📅 تاريخ العمليات: {datetime.now().strftime('%Y-%m-%d')}")
    st.markdown("---")
    st.warning("⚠️ **تذكير أمني:** المعلومات في هذا التطبيق سرية وحساسة. يمنع التصريح للإعلام دون إذن مسبق.")

# --- 3. العنوان الرئيسي للبرنامج ---
st.title("🛡️ المنصة الذكية لمفتشي الرقابة التجارية")
st.write("دائرة الاقتصاد والسياحة - قطاع الرقابة التجارية وحماية المستهلك")

# --- 4. التبويبات (Tabs) ---
tab1, tab2, tab3 = st.tabs(["📞 دليل شركات دبي", "📝 تسجيل مخالفة ميدانية", "💬 المساعد القانوني"])

# --- التبويب الأول: دليل الاتصال (مربوط بملف الإكسل المرفق) ---
with tab1:
    st.subheader("البحث في نقاط الاتصال المعتمدة")
    
    # محرك البحث عن الشركات
    uploaded_file = st.file_uploader("ارفع ملف Contacts.xlsb لتحديث البيانات", type=["xlsb", "xlsx"])
    
    if uploaded_file:
        try:
            # قراءة الملف (يدعم xlsb)
            df_contacts = pd.read_excel(uploaded_file, engine='pyxlsb')
            search_query = st.text_input("🔍 ابحث عن اسم الشركة أو القطاع أو اسم المسؤول:")
            
            if search_query:
                # بحث مرن يتجاهل حالة الأحرف
                mask = df_contacts.astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
                results = df_contacts[mask]
                st.success(f"تم العثور على {len(results)} نتيجة")
                st.dataframe(results, use_container_width=True)
            else:
                st.dataframe(df_contacts, use_container_width=True)
                
            st.info("🔒 تذكر: المادة (7) تصنف بيانات هذه الشركات كمعلومات حساسة لا يجوز مشاركتها.")
        except Exception as e:
            st.error(f"حدث خطأ أثناء قراءة ملف البيانات: {e}")
    else:
        st.info("💡 يرجى رفع ملف 'Contacts.xlsb' المرفق لعرض بيانات ضباط الامتثال.")

# --- التبويب الثاني: تسجيل المخالفات ---
with tab2:
    st.subheader("توثيق مخالفة تجارية جديدة")
    
    # حفظ البيانات مؤقتاً في الجلسة
    if "violation_records" not in st.session_state:
        st.session_state.violation_records = []

    with st.form("inspection_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            inspector_name = st.text_input("اسم المفتش")
            company_sector = st.selectbox("قطاع العمل", ["التجزئة", "السيارات", "الإلكترونيات", "المطاعم", "أخرى"])
        with c2:
            violation_type = st.selectbox("نوع التجاوز", ["سلع مقلدة", "تلاعب بالأسعار", "عدم وضع ملصقات", "إعلان مضلل"])
            fine_amount = st.number_input("قيمة الغرامة التقديرية (درهم)", min_value=0, value=2000)
        
        details = st.text_area("تفاصيل إضافية عن الواقعة")
        
        submit_btn = st.form_submit_button("حفظ وإرسال التقرير")
        
        if submit_btn:
            new_record = {
                "الوقت": datetime.now().strftime("%H:%M"),
                "المفتش": inspector_name,
                "القطاع": company_sector,
                "المخالفة": violation_type,
                "المبلغ": fine_amount
            }
            st.session_state.violation_records.append(new_record)
            st.balloons()
            st.success("✅ تم حفظ المخالفة بنجاح.")

    # عرض جدول المخالفات المسجلة حالياً
    if st.session_state.violation_records:
        st.write("### سجل العمليات الميدانية (اليوم)")
        st.table(st.session_state.violation_records)

# --- التبويب الثالث: المساعد القانوني (سياسة المتحدث الرسمي) ---
with tab3:
    st.subheader("💬 مساعد الالتزام والسياسات الإعلامية")
    
    # تنبيه ثابت من السياسة
    st.markdown("""
    <div class="policy-box">
    <strong>⚠️ تنبيه هام من إدارة الاتصال الحكومي:</strong><br>
    بناءً على السياسة المعتمدة، يمنع المفتش من إعطاء أي تصريح إعلامي ميداني. <br>
    في حال وجود صحافة، وجههم فوراً إلى مدير إدارة الاتصال (المتحدث الرسمي الأول).
    </div>
    """, unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # عرض المحادثة
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    if user_input := st.chat_input("اسألني عن إجراءات التعامل مع الإعلام أو الشركات..."):
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        with st.chat_message("assistant"):
            # منطق الرد بناءً على السياسة المرفقة
            if "إعلام" in user_input or "صحفي" in user_input:
                answer = "حسب المادة (6)، يجب توجيه الاستفسار لإدارة الاتصال. امتنع عن قول 'لا تعليق' وكن لبقاً."
            elif "حساسة" in user_input:
                answer = "المعلومات الحساسة (المادة 7) تشمل التشريعات والرسوم والبيانات الفنية. لا تفصح عنها أبداً."
            else:
                answer = f"بخصوص استفسارك عن '{user_input}'، يرجى مراجعة دليل إجراءات حماية المستهلك المعتمد أو التحدث مع المدير التنفيذي للقطاع."
            
            st.markdown(answer)
            st.session_state.chat_history.append({"role": "assistant", "content": answer})
