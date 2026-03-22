import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. حل مشكلة إثبات الملكية لـ AdSense (Meta Tag & ads.txt) ---
# هذا الكود سيجعل جوجل يرى ملف ads.txt الخاص بك فوراً عند الطلب
if "ads" in st.query_params:
    if os.path.exists("ads.txt"):
        with open("ads.txt", "r") as f:
            st.text(f.read())
        st.stop()

# كود التحقق (Meta Tag) الذي أرسلته في الصورة
verification_tag = '<meta name="google-adsense-account" content="ca-pub-6456486381436649">'

try:
    import yfinance as yf
    YF_AVAILABLE = True
except ImportError:
    YF_AVAILABLE = False

# --- 2. إعدادات الصفحة والهوية البصرية ---
st.set_page_config(page_title="جوست ماركت - تسعير الذهب", page_icon="🔱", layout="wide")

# حقن كود التحقق وكود الإعلانات في "رأس" الموقع
components.html(f"""
    {verification_tag}
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6456486381436649"
     crossorigin="anonymous"></script>
""", height=0)

# التنسيق البصري الكامل (CSS)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    [data-testid="stAppViewContainer"] { background-color: #1a1a16; color: white; }
    * { direction: rtl; }
    .main-title { text-align: center; color: #ffd700; font-size: 45px; font-weight: bold; }
    .stNumberInput label { width: 100% !important; text-align: center !important; color: #ffd700 !important; font-size: 35px !important; font-weight: bold !important; display: block !important; }
    div.stNumberInput { max-width: 700px; margin: 0 auto !important; }
    input { text-align: center !important; font-size: 35px !important; height: 75px !important; color: white !important; background-color: #262621 !important; border: 2px solid #ffd700 !important; border-radius: 15px !important; }
    .price-card { border: 1px solid #3d3d36; padding: 35px; border-radius: 15px; text-align: center; background-color: #262621; margin-top: 20px; }
    .price-val { color: white; font-size: 45px; font-weight: bold; }
    .gold-label { color: #ffd700; font-size: 24px; font-weight: bold; }
    .btn-gold { background-color: #ffd700; color: #000 !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    .btn-white { background-color: white; color: #000 !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    .btn-wa { background-color: #25d366; color: white !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    .developer-credit { text-align: center; color: #ffd700; font-size: 25px; font-weight: bold; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. جلب الأسعار والحسابات ---
def get_gold_spot_price():
    default_price = 4497.0
    if YF_AVAILABLE:
        try:
            gold = yf.Ticker("GC=F")
            data = gold.history(period="1d")
            if not data.empty: return round(data['Close'].iloc[-1], 2)
        except: return default_price
    return default_price

# --- 4. عرض الموقع ---
st.markdown("<div class='main-title'>🔱 نظام تسعير الذهب العالمي 🔱</div>", unsafe_allow_html=True)
live_price = get_gold_spot_price()
col_main, col_side = st.columns([2.3, 1])

with col_main:
    ounce_input = st.number_input("أدخل سعر الأونصة العالمي الحالي ($)", value=float(live_price))
    troy_ounce = 31.1035
    p24, p21, p18 = ounce_input/troy_ounce, (ounce_input/troy_ounce)*0.875, (ounce_input/troy_ounce)*0.75
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
    with c2: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
    with c3: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

with col_side:
    st.markdown(f"""
        <div style='border: 1px solid #ffd700; padding: 25px; border-radius: 15px; background-color: #262621; text-align: center;'>
            <h2 style='color: #ffd700; margin-bottom: 20px;'>📈 استثمر في الذهب</h2>
            <a class='btn-gold' href='https://justmarkets.com/'>فتح حساب تحت وكالتنا</a>
            <a class='btn-white' href='#'>تحميل تطبيق مباشر</a>
            <a class='btn-wa' href='https://wa.me/963950555563'>💬 تواصل واتساب مباشر</a>
            <p style='font-size: 14px; color: #888; margin-top: 15px;'>الوكيل المعتمد: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

# سياسة الخصوصية للقبول
st.divider()
with st.expander("📄 سياسة الخصوصية"):
    st.write("هذا الموقع يستخدم ملفات تعريف الارتباط لعرض الإعلانات. نحن لا نجمع بيانات شخصية.")

st.markdown(f"<div class='developer-credit'>تم التطوير بواسطة: عقيل فرح 👨‍💻</div>", unsafe_allow_html=True)