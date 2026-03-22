import streamlit as st
import yfinance as yf

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="نظام تسعير الذهب العالمي", page_icon="🔱", layout="wide")

# تنسيق CSS لاستعادة التصميم الفخم
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    body { background-color: #0e1117; color: white; }
    * { direction: rtl; }
    .main-title { text-align: center; color: #ffd700; font-size: 40px; font-weight: bold; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #888; font-size: 16px; margin-bottom: 30px; }
    .price-card {
        border: 1px solid #333;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        background-color: #161a23;
    }
    .price-val { color: white; font-size: 45px; font-weight: bold; margin-top: 10px; }
    .gold-label { color: #ffd700; font-size: 20px; font-weight: bold; }
    .sidebar-card {
        border: 1px solid #ffd700;
        padding: 20px;
        border-radius: 15px;
        background-color: #161a23;
        text-align: center;
    }
    .btn-gold {
        background-color: #ffd700;
        color: black;
        padding: 10px;
        border-radius: 8px;
        text-decoration: none;
        display: block;
        margin: 10px 0;
        font-weight: bold;
    }
    .btn-white {
        background-color: white;
        color: black;
        padding: 10px;
        border-radius: 8px;
        text-decoration: none;
        display: block;
        margin: 10px 0;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 2. دالة جلب السعر الحقيقي من البورصة
@st.cache_data(ttl=60)
def get_gold_spot_price():
    try:
        # رمز الذهب في Yahoo Finance هو GC=F
        gold = yf.Ticker("GC=F")
        price = gold.history(period="1d")['Close'].iloc[-1]
        return round(price, 2)
    except:
        return 2290.0 # سعر افتراضي في حال فشل الاتصال

# 3. الجزء العلوي (العنوان)
st.markdown("<div class='main-title'>🔱 نظام تسعير الذهب العالمي 🔱</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>دقة عالمية في متناول يدك</div>", unsafe_allow_html=True)

# جلب السعر المباشر
live_price = get_gold_spot_price()

# 4. توزيع المحتوى (الأعمدة)
col_main, col_side = st.columns([2, 1])

with col_main:
    # مدخل السعر (يأخذ السعر المباشر تلقائياً)
    ounce_input = st.number_input("($) أدخل سعر الأونصة", value=float(live_price))
    
    # الحسابات
    troy_ounce = 31.1035
    p24 = ounce_input / troy_ounce
    p21 = p24 * 0.875
    p18 = p24 * 0.75

    st.write("")
    # عرض الأسعار في مربعات
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

with col_side:
    # بطاقة الاستثمار (JustMarkets)
    st.markdown(f"""
        <div class='sidebar-card'>
            <h3 style='color: #ffd700;'>📈 استثمر في الذهب</h3>
            <p style='font-size: 12px;'>JustMarkets لتداول الذهب بروافع مالية وسبريد منخفض جداً</p>
            <a class='btn-gold' href='#'>فتح حساب تداول وكيل</a>
            <a class='btn-white' href='#'>تحميل التطبيق المباشر</a>
            <p style='margin-top: 15px; font-size: 14px;'>💬 واتساب: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

# تذييل الصفحة
st.markdown("<br><p style='text-align: center; color: #555;'>تم التطوير بواسطة: عقيل فرح 👨‍💻</p>", unsafe_allow_html=True)