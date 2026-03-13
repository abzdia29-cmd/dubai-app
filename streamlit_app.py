import streamlit as st
import pandas as pd
import traceback

# Page config
st.set_page_config(page_title="نظام دبي الذكي", layout="centered")

# Scoped RTL CSS (keeps scope small by wrapping content in .app-rtl)
st.markdown(
    '''
    <style>
    .app-rtl { direction: rtl; text-align: right; }
    .app-rtl .block-container { padding-top: 2rem; }
    .app-rtl input { direction: rtl; }
    /* Keep selectors narrow so future Streamlit changes are less likely to break this CSS */
    </style>
    ''' ,
    unsafe_allow_html=True,
)

# Wrap major content in a container div so CSS scope is limited
st.markdown('<div class="app-rtl">', unsafe_allow_html=True)

st.title("🛡️ نظام حماية المستهلك الذكي")

# Sidebar
st.sidebar.title("إعدادات النظام")
st.sidebar.info("هذا التطبيق مخصص لمفتشي حماية المستهلك في دبي.")

# --- Tabs ---
tab1, tab2 = st.tabs(["🔍 دليل الشركات", "💬 مساعد المفتش (Chat)"])

with tab1:
    st.subheader("البحث في أرقام الشركات")
    uploaded_file = st.file_uploader("ارفع ملف الإكسل (Excel)", type=["xlsx")
    if uploaded_file:
        try:
            # Try to read Excel. Use a robust read with engine autodetection; provide helpful error to user.
            df = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error("حدث خطأ أثناء قراءة ملف الإكسل. تأكد أن الملف بصيغة XLSX وأن مكتبة openpyxl مثبتة.")
            with st.expander("تفاصيل الخطأ (لعين المطور)"):
                st.text(traceback.format_exc())
            df = None

        if df is not None:
            # UI for search
            search = st.text_input("ابحث عن اسم الشركة:")
            # For faster, safer searches: aggregate row text once and use vectorized .str.contains with na=False
            if not df.empty:
                try:
                    row_text = df.fillna("").astype(str).agg(" ".join, axis=1)
                except Exception:
                    # Fallback if aggregation fails for unusual dtypes
                    row_text = df.fillna("").astype(str).apply(lambda row: " ".join(row.values.astype(str)), axis=1)

                if search:
                    mask = row_text.str.contains(search, case=False, na=False)
                    results = df[mask]
                    st.write(f"نتائج البحث: {len(results)} صف")
                    st.dataframe(results, use_container_width=True)
                else:
                    st.dataframe(df, use_container_width=True)
            else:
                st.info("الملف المحمّل فارغ.")
    else:
        st.info("ارفع ملف إكسل لبدء البحث. تأكد أنّ الملف بصيغة .xlsx")

with tab2:
    st.subheader("الدردشة الذكية")

    # Chat history settings
    DEFAULT_MAX_HISTORY = 50
    if "max_history" not in st.session_state:
        st.session_state.max_history = DEFAULT_MAX_HISTORY

    # Allow the user to change max history from the sidebar
    st.sidebar.markdown("---")
    st.sidebar.number_input(
        "حد المحادثة (أقصى عدد رسائل محفوظة)",
        min_value=10,
        max_value=500,
        value=st.session_state.max_history,
        step=10,
        key="max_history_sidebar",
        help="اضبط عدد الرسائل التي يتم الاحتفاظ بها في الجلسة",
    )
    # Keep session_state.max_history synced
    st.session_state.max_history = st.session_state.get("max_history_sidebar", st.session_state.max_history)

    # Initialize messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Clear chat button
    if st.button("مسح المحادثة"):
        st.session_state.messages = []
        st.success("تم مسح المحادثة.")

    # Display existing messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # New message input
    if prompt := st.chat_input("كيف يمكنني مساعدتك؟"):
        # Append user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Example assistant response (replace with real LLM/API call if integrated)
        with st.chat_message("assistant"):
            response = f"جاري معالجة طلبك بخصوص: {prompt}. نظام البحث جاهز لمساعدتك."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

        # Enforce max history length (trim oldest)
        max_h = int(st.session_state.get("max_history", DEFAULT_MAX_HISTORY))
        if len(st.session_state.messages) > max_h:
            # Keep the last max_h messages
            st.session_state.messages = st.session_state.messages[-max_h:]

# Close the wrapper div
st.markdown("</div>", unsafe_allow_html=True)