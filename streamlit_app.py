import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. إثبات الملكية لـ AdSense (أهم جزء للتحقق) ---
# كود الـ Meta Tag الذي طلبته جوجل في صورتك
verify_meta = '<meta name="google-adsense-account" content="ca-pub-6456486381436649">'

# كود Script الإعلانات
ads_script = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6456486381436649" crossorigin="anonymous"></script>'

# دالة ذكية لإظهار ads.txt مباشرة لجوجل عند طلبه
if "ads" in st.query_params:
    if os.path.exists("ads.txt"):
        with open("ads.txt", "r") as f:
            st.text(f.read())
        st.stop()

# --- 2. إعدادات الصفحة ---
st.set_page_config(page_title="جوست ماركت - تسعير الذهب", page_icon="🔱", layout="wide")

# حقن كود التحقق في الطبقة العلوية للمتصفح لضمان رؤية جوجل له
st.markdown(f'<html><head>{verify_meta}{ads_script}</head></html>', unsafe_allow_html=True)

# --- 3. التصميم البصري (CSS) ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    [data-testid="stAppViewContainer"] { background-color: #1a1a16; color: white; }
    * { direction: rtl; text-align: right; }
    .main-title { text-align: center; color: #ffd700; font-size: 40px; font-weight: bold; }
    .stNumberInput label { color: #ffd700 !important; font-size: 24px !important; font-weight: bold !important; }
    input { text-align: center !important; font-size: 28px !important; color: white !important; background-color: #262621 !important; border: 2px solid #ffd700 !important; }
    .price-card { border: 1px solid #3d3d36; padding: 25px; border-radius: 15px; text-align: center; background-color: #262621; }
    .price-val { color: white; font-size: 35px; font-weight: bold; }
    .gold-label { color: #ffd700; font-size: 20px; }
    .btn-gold { background-color: #ffd700; color: #000 !important; padding: 12px; border-radius: 8px; text-decoration: none; display: block; margin: 10px 0; font-weight: bold; text-align: center; }
    .btn-wa { background-color: #25d366; color: white !important; padding: 12px; border-radius: 8px; text-decoration: none; display: block; margin: 10px 0; font-weight: bold; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 4. منطق التسعير ---
st.markdown("<div class='main-title'>🔱 نظام تسعير الذهب العالمي 🔱</div>", unsafe_allow_html=True)

# السعر الافتراضي المحدث
live_price = 4497.0 
ounce_input = st.number_input("سعر الأونصة العالمي ($)", value=live_price)

troy_ounce = 31.1035
p24, p21, p18 = ounce_input/troy_ounce, (ounce_input/troy_ounce)*0.875, (ounce_input/troy_ounce)*0.75

c1, c2, c3 = st.columns(3)
with c1: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
with c2: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
with c3: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

# الأزرار الجانبية
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='border: 1px solid #ffd700; padding: 20px; border-radius: 15px; background-color: #262621;'>
        <h3 style='color: #ffd700; text-align: center;'>استثمر في الذهب</h3>
        <a class='btn-gold' href='https://justmarkets.com/'>فتح حساب تحت وكالتنا</a>
        <a class='btn-wa' href='https://wa.me/963950555563'>تواصل واتساب مباشر</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; color: #ffd700; margin-top: 30px;'>تم التطوير بواسطة: عقيل فرح 👨‍💻</div>", unsafe_allow_html=True)