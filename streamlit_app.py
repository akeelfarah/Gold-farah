import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. حل مشكلة إثبات الملكية لـ AdSense (Meta Tag & ads.txt) ---
VERIFY_META = '<meta name="google-adsense-account" content="ca-pub-6456486381436649">'

if "ads" in st.query_params:
    if os.path.exists("ads.txt"):
        with open("ads.txt", "r") as f:
            st.text(f.read())
        st.stop()

try:
    import yfinance as yf
    YF_AVAILABLE = True
except ImportError:
    YF_AVAILABLE = False

# --- 2. إعدادات الصفحة والهوية البصرية ---
st.set_page_config(page_title="جوست ماركت - تسعير الذهب", page_icon="🔱", layout="wide")

ads_verify_and_script = f"""
{VERIFY_META}
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6456486381436649"
     crossorigin="anonymous"></script>
"""
components.html(ads_verify_and_script, height=0)

# --- 3. التنسيق الجمالي (CSS) - اللون #755220 والإطار الفني ---
st.markdown("""
    <style>
    /* إخفاء القوائم الافتراضية لتعزيز شكل اللوحة */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* تصميم الخلفية والإطار الذهبي الفاخر */
    [data-testid="stAppViewContainer"] {
        background-color: #755220; /* اللون المطلوب */
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.85)),
                          url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDUwIiBoZWlnaHQ9IjM5MSIgdmlld0JveD0iMCAwIDEwNTAgMzkxIj48cGF0aCBkPSJNOTU5IDM0NmwzNyAyMSAyNCA0NE04MjQgMjQ4bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMjU5IDEwOEwzMDQgMTI2bDM0LTQzbC0zNC00M0wyNTkgNjVNMzg0IDY1TDQyOCA4MmwzNC00M0w0MjggNGwtNDQtNDNMMzg0IDY1TTEzNSA2NWw0NCAxN2wzNC00M0wxNzkgNHwtNDQtNDNMMTM1IDY1TTAgNjVsNDQgMTdsMzQtNDNMNDQgNHwtNDQtNDNMMCA2NU01NTAgMjQ4bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMTA0OSAxMDhsLTEzLTQzbC0zNC00M0w5NTkgNjVNMTA0OSAxMDhsLTEzLTQzbC0zNC00M0w5NTkgNjVNMTA0OSAxMDhsLTEzLTQzbC0zNC00M0w5NTkgNjVNMTA0OSAxMDhsLTEzLTQzbC0zNC00M0w5NTkgNjVNODU5IDY1bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNNDQ5IDY1bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMTU5IDI0OGwzMi0xOCAzMiAxOCAzMiAxOC0zNi00NGwtMzIgMThsLTMyIDE4LTMyIDE4TTAgMjQ4bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNNDAwIDI0OGwzMi0xOCAzMiAxOCAzMiAxOC0zNi00NGwtMzIgMThsLTMyIDE4LTMyIDE4TTAgMzQ2bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMTA0OSAzNDZsLTEzLTQzbC0zNC00M0w5NTkgMzQ2TTQ5OSAzNDZsMzItMTggMzIgMTggMzIgMTgtMzYtNDRGNTMzIDM0NmwtMzIgMTgtMzIgMTgvPiA8cGF0aCBkPSJNMzQ5IDEwOGwzMi0xOCAzMiAxOCAzMiAxOC0zNi00NGwtMzIgMThsLTMyIDE4LTMyIDE4TTU0OSAxMDhsLTMyLTQzbC0zNC00M0w0NTkgNjVNMTE5IDY1bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMTA0OSAyNDhsLTEzLTQzbC0zNC00M0w5NTkgMjQ4TTczOSAyNDhsLTMyLTQzbC0zNC00M0w2NDkgMTc4TTMzOSAyNDhsLTMyLTQzbC0zNC00M0wyNDkgMTc4TTE0OSAzNDZ sMzItMTggMzIgMTggMzIgMTgtMzYtNDREMTgzIDM0NmwtMzIgMTgtMzIgMTgvPiA8L3N2Zz4=');
        background-repeat: repeat;
        background-attachment: fixed;
        background-size: 300px;
        animation: chartBackgroundSlide 100s linear infinite;
        
        /* إطار ذهبي فني (لوحة فنية) */
        border: min(15px, 2vw) solid #ffd700;
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(0,0,0,0.6);
        margin: min(10px, 1vw);
    }
    
    @keyframes chartBackgroundSlide {
        from { background-position: 0 0; }
        to { background-position: -600px 300px; }
    }
    
    * { direction: rtl; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* عناوين اللوحة */
    .main-title { text-align: center; color: #ffd700; font-size: clamp(28px, 6vw, 48px); font-weight: bold; margin-top: 10px; text-shadow: 2px 2px 15px rgba(0,0,0,0.5); }
    .sub-title { text-align: center; color: #e0e0e0; font-size: clamp(14px, 3vw, 20px); margin-bottom: 25px; }
    
    /* تنسيق متجاوب لخانة الإدخال */
    div.stNumberInput { max-width: 600px; margin: 0 auto !important; }
    .stNumberInput label { color: #ffd700 !important; font-size: 24px !important; font-weight: bold !important; text-align: center !important; width: 100%; display: block; }
    input { text-align: center !important; font-size: 28px !important; height: 65px !important; color: white !important; background-color: rgba(0,0,0,0.4) !important; border: 2px solid #ffd700 !important; border-radius: 12px !important; }

    /* بطاقات الأسعار - ترتيب مرن */
    .price-card { 
        border: 1px solid rgba(255,215,0,0.3); padding: 25px; border-radius: 15px; 
        text-align: center; background-color: rgba(0,0,0,0.4); margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
    }
    .price-card:hover { transform: translateY(-5px); border-color: #ffd700; }
    .price-val { color: #ffffff; font-size: clamp(30px, 5vw, 42px); font-weight: bold; }
    .gold-label { color: #ffd700; font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    
    /* القسم الجانبي (الأزرار) */
    .agency-box {
        border: 2px solid #ffd700; padding: 20px; border-radius: 15px; 
        background-color: rgba(0,0,0,0.5); text-align: center; margin-top: 20px;
    }
    .btn-gold { background-color: #ffd700; color: #000 !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 10px 0; font-weight: bold; font-size: 18px; }
    .btn-wa { background-color: #25d366; color: white !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 10px 0; font-weight: bold; font-size: 18px; }
    
    .developer-credit { text-align: center; color: #ffd700; font-size: 22px; font-weight: bold; margin-top: 40px; padding-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 4. جلب البيانات ---
def get_gold_spot_price():
    default_price = 4497.0
    if YF_AVAILABLE:
        try:
            gold = yf.Ticker("GC=F")
            data = gold.history(period="1d")
            if not data.empty: return round(data['Close'].iloc[-1], 2)
        except: return default_price
    return default_price

# --- 5. واجهة المستخدم ---
st.markdown("<div class='main-title'>🔱 جوست ماركت للذهب 🔱</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>الأسعار العالمية المباشرة بتنسيق فني دقيق</div>", unsafe_allow_html=True)

live_price = get_gold_spot_price()

# استخدام الحاويات لضمان التنسيق في الموبايل
col_main, col_side = st.columns([2.5, 1])

with col_main:
    ounce_input = st.number_input("أدخل سعر الأونصة ($)", value=float(live_price))
    
    troy_ounce = 31.1035
    p24 = ounce_input / troy_ounce
    p21 = p24 * 0.875
    p18 = p24 * 0.75
    
    # توزيع البطاقات بشكل متجاوب
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
    with c2: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
    with c3: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

with col_side:
    st.markdown(f"""
        <div class='agency-box'>
            <div style='font-size: 40px;'>🔱</div>
            <h3 style='color: #ffd700; margin-top:0;'>جوست ماركت</h3>
            <a class='btn-gold' href='https://justmarkets.com/'>فتح حساب تداول</a>
            <a class='btn-wa' href='https://wa.me/963950555563'>💬 واتساب مباشر</a>
            <p style='font-size: 13px; color: #bbb;'>الوكيل المعتمد: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

# سياسة الخصوصية
with st.expander("📄 سياسة الخصوصية"):
    st.write("هذا الموقع مخصص لعرض أسعار الذهب. نستخدم ملفات تعريف الارتباط لتحسين تجربة المستخدم عبر Google AdSense.")

st.markdown("<div class='developer-credit'>تم التطوير بواسطة: عقيل فرح 👨‍💻</div>", unsafe_allow_html=True)