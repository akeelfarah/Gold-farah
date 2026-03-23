import streamlit as st
import streamlit.components.v1 as components
import os

# إعدادات AdSense
VERIFY_META = '<meta name="google-adsense-account" content="ca-pub-6456486381436649">'

if "ads" in st.query_params:
    if os.path.exists("ads.txt"):
        with open("ads.txt", "r") as f:
            st.text(f.read())
        st.stop()

try:
    import yfinance as yf
    YF_AVAILABLE = True
except:
    YF_AVAILABLE = False

st.set_page_config(page_title="جوست ماركت - تسعير الذهب", page_icon="🔱", layout="wide")

# حقن كود التحقق
components.html(VERIFY_META + '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6456486381436649" crossorigin="anonymous"></script>', height=0)

# التنسيق
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stAppViewContainer"] {
        background-color: #755220;
        border: 15px solid #ffd700;
        border-radius: 20px;
        color: white;
        direction: rtl;
    }
    .main-title { text-align: center; color: #ffd700; font-size: 40px; font-weight: bold; }
    .price-card { border: 1px solid #ffd700; padding: 20px; border-radius: 10px; text-align: center; background: rgba(0,0,0,0.5); }
    .partner-box { border: 2px solid #ffd700; padding: 15px; background: #000; color: #ffd700; font-family: monospace; font-size: 20px; text-align: center; margin: 10px 0; }
    .btn-gold { background: #ffd700; color: black; padding: 10px; display: block; text-align: center; text-decoration: none; border-radius: 5px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🔱 نظام تسعير الذهب العالمي 🔱</div>", unsafe_allow_html=True)

# جلب السعر
def get_price():
    if YF_AVAILABLE:
        try:
            return round(yf.Ticker("GC=F").history(period="1d")['Close'].iloc[-1], 2)
        except: return 4497.0
    return 4497.0

live_p = get_price()
col1, col2 = st.columns([2, 1])

with col1:
    val = st.number_input("سعر الأونصة ($)", value=float(live_p))
    p24 = val / 31.1035
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='price-card'>عيار 24<br>${p24:.2f}</div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='price-card'>عيار 21<br>${p24*0.875:.2f}</div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='price-card'>عيار 18<br>${p24*0.75:.2f}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='text-align:center;'><h3>وكالة جوست ماركت</h3><p>كود الشريك المعتمد:</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='partner-box'>4f59i0rjez</div>", unsafe_allow_html=True)
    st.markdown("<a href='https://justmarkets.com/' class='btn-gold'>فتح حساب تداول</a>", unsafe_allow_html=True)

st.markdown("<center><br>تم التطوير بواسطة: عقيل فرح</center>", unsafe_allow_html=True)