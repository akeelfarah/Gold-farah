import streamlit as st
import yfinance as yf

# 1. إعدادات الصفحة وإخفاء العناصر غير الضرورية
st.set_page_config(page_title="نظام تسعير الذهب العالمي", page_icon="🔱", layout="centered")

# كود لإخفاء القوائم والعلامات لجعله يبدو كتطبيق موبايل احترافي
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    div.block-container {padding-top: 2rem;}
    * {direction: rtl; text-align: right;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

# 2. دالة جلب السعر المباشر
@st.cache_data(ttl=300) # تحديث تلقائي كل 5 دقائق
def get_live_price():
    try:
        # استخدام رمز الذهب العالمي في البورصة
        gold_data = yf.Ticker("GC=F")
        price = gold_data.history(period="1d")['Close'].iloc[-1]
        return round(price, 2)
    except Exception:
        return 2290.0 # سعر احتياطي في حال وجود مشكلة في الإنترنت

# 3. واجهة المستخدم الرئيسية
st.markdown("<h1 style='text-align: center; color: #ffd700;'>🔱 حاسبة الذهب الملكية</h1>", unsafe_allow_html=True)

# جلب السعر المباشر لوضعه كقيمة افتراضية
current_live = get_live_price()

st.write("### ⚙️ الإعدادات")
# خانة إدخال السعر (تعرض السعر المباشر تلقائياً ويمكنك تعديله)
price_input = st.number_input("سعر الأونصة العالمي الحالي ($)", min_value=0.0, value=float(current_live), step=1.0)

# 4. الحسابات (الأونصة = 31.1035 غرام)
troy_ounce = 31.1035
p24 = price_input / troy_ounce
p21 = p24 * 0.875
p18 = p24 * 0.75

st.divider()

# 5. عرض النتائج بتصميم بطاقات جذابة
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"<div style='border: 2px solid #ffd700; padding: 15px; border-radius: 15px; text-align: center; background-color: #0e1117;'>"
                f"<h4 style='color: #ffd700;'>عيار 24</h4><h2 style='color: white;'>${p24:.2f}</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div style='border: 2px solid #ffd700; padding: 15px; border-radius: 15px; text-align: center; background-color: #0e1117;'>"
                f"<h4 style='color: #ffd700;'>عيار 21</h4><h2 style='color: white;'>${p21:.2f}</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div style='border: 2px solid #ffd700; padding: 15px; border-radius: 15px; text-align: center; background-color: #0e1117;'>"
                f"<h4 style='color: #ffd700;'>عيار 18</h4><h2 style='color: white;'>${p18:.2f}</h2></div>", unsafe_allow_html=True)

st.write("")
st.info(f"💡 السعر المسحوب حالياً من البورصة: ${current_live}")