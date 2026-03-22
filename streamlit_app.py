import streamlit as st
import yfinance as yf

# 1. إعدادات الصفحة والهوية
st.set_page_config(page_title="جوست ماركت - حاسبة الذهب", page_icon="👻", layout="centered")

# إخفاء أدوات المطور وإضافة التنسيق الخاص بك
hide_style = """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    * {direction: rtl; text-align: right;}
    .gold-card {
        border: 2px solid #ffd700;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        background-color: #1a1a1a;
        margin-bottom: 10px;
    }
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

# 2. دالة جلب السعر المباشر (Gold Spot)
@st.cache_data(ttl=60) # تحديث كل دقيقة لضمان الدقة
def get_real_gold_price():
    try:
        gold = yf.Ticker("GC=F")
        data = gold.history(period="1d")
        return round(data['Close'].iloc[-1], 2)
    except:
        return 0.0 # إذا فشل، سيطلب من المستخدم الإدخال يدوياً

# 3. الهوية البصرية (جوست ماركت)
st.markdown("<h1 style='text-align: center; color: #ffd700;'>👻 جـوست مـاركت</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>لخدمات التسعير والوساطة</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>تواصل معنا: 01024344449</p>", unsafe_allow_html=True)
st.divider()

# جلب السعر الحقيقي الآن
live_price = get_real_gold_price()

# 4. لوحة التحكم
st.subheader("⚙️ أسعار البورصة العالمية")
if live_price == 0.0:
    st.warning("⚠️ لم نتمكن من جلب السعر تلقائياً، يرجى إدخاله يدوياً.")

# خانة السعر (تضع السعر الحقيقي تلقائياً إذا توفر)
ounce_price = st.number_input("سعر الأونصة الآن ($)", min_value=0.0, value=float(live_price) if live_price > 0 else 2400.0)

# 5. الحسابات الفنية
troy_ounce = 31.1035
g24 = ounce_price / troy_ounce
g21 = g24 * 0.875
g18 = g24 * 0.75

# 6. عرض النتائج
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"<div class='gold-card'><h4 style='color: #ffd700;'>عيار 24</h4><h2 style='color: white;'>${g24:.2f}</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='gold-card'><h4 style='color: #ffd700;'>عيار 21</h4><h2 style='color: white;'>${g21:.2f}</h2></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='gold-card'><h4 style='color: #ffd700;'>عيار 18</h4><h2 style='color: white;'>${g18:.2f}</h2></div>", unsafe_allow_html=True)

st.info(f"📊 مصدر السعر: البورصة العالمية (Yahoo Finance) | السعر المباشر: ${live_price}")