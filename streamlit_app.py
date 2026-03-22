import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. حل مشكلة إثبات الملكية لـ AdSense (Meta Tag & ads.txt) ---
# هذا الكود سيجعل جوجل يرى الملف والكود الخاص بك فوراً عند الطلب
VERIFY_META = '<meta name="google-adsense-account" content="ca-pub-6456486381436649">'

# معالجة طلب ads.txt المباشر (مثل الصورة التي أرسلتها سابقاً)
if "ads" in st.query_params:
    if os.path.exists("ads.txt"):
        with open("ads.txt", "r") as f:
            st.text(f.read())
        st.stop()

# مكتبة جلب السعر العالمي (إذا لم تكن مثبتة، استخدم السعر الافتراضي)
try:
    import yfinance as yf
    YF_AVAILABLE = True
except ImportError:
    YF_AVAILABLE = False

# --- 2. إعدادات الصفحة والهوية البصرية ---
# تعيين العنوان والأيقونة لخانة المتصفح
st.set_page_config(page_title="جوست ماركت - تسعير الذهب", page_icon="🔱", layout="wide")

# حقن كود التحقق وكود الإعلانات في "رأس" الموقع
ads_verify_and_script = f"""
{VERIFY_META}
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6456486381436649"
     crossorigin="anonymous"></script>
"""
components.html(ads_verify_and_script, height=0)

# --- 3. التنسيق الجمالي (CSS) - خلفية مخصصة، إطار ذهبي، وتصميم متجاوب ---
st.markdown("""
    <style>
    /* إخفاء علامات Streamlit الافتراضية (القوائم والتذييل) */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* تصميم الخلفية الفخمة باللون البني الجديد وإضافة الإطار الذهبي المحيط */
    [data-testid="stAppViewContainer"] {
        background-color: #313129; /* هذا هو اللون الفخم الذي أرسلته */
        background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.95)),
                          url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDUwIiBoZWlnaHQ9IjM5MSIgdmlld0JveD0iMCAwIDEwNTAgMzkxIj48cGF0aCBkPSJNOTU5IDM0NmwzNyAyMSAyNCA0NE04MjQgMjQ4bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMjU5IDEwOEwzMDQgMTI2bDM0LTQzbC0zNC00M0wyNTkgNjVNMzg0IDY1TDQyOCA4MmwzNC00M0w0MjggNGwtNDQtNDNMMzg0IDY1TTEzNSA2NWw0NCAxN2wzNC00M0wxNzkgNHwtNDQtNDNMMTM1IDY1TTAgNjVsNDQgMTdsMzQtNDNMNDQgNHwtNDQtNDNMMCA2NU01NTAgMjQ4bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMTA0OSAxMDhsLTEzLTQzbC0zNC00M0w5NTkgNjVNMTA0OSAxMDhsLTEzLTQzbC0zNC00M0w5NTkgNjVNMTA0OSAxMDhsLTEzLTQzbC0zNC00M0w5NTkgNjVNMTA0OSAxMDhsLTEzLTQzbC0zNC00M0w5NTkgNjVNODU5IDY1bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNNDQ5IDY1bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMTU5IDI0OGwzMi0xOCAzMiAxOCAzMiAxOC0zNi00NGwtMzIgMThsLTMyIDE4LTMyIDE4TTAgMjQ4bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNNDAwIDI0OGwzMi0xOCAzMiAxOCAzMiAxOC0zNi00NGwtMzIgMThsLTMyIDE4LTMyIDE4TTAgMzQ2bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMTA0OSAzNDZsLTEzLTQzbC0zNC00M0w5NTkgMzQ2TTQ5OSAzNDZsMzItMTggMzIgMTggMzIgMTgtMzYtNDRGNTMzIDM0NmwtMzIgMTgtMzIgMTgvPiA8cGF0aCBkPSJNMzQ5IDEwOGwzMi0xOCAzMiAxOCAzMiAxOC0zNi00NGwtMzIgMThsLTMyIDE4LTMyIDE4TTU0OSAxMDhsLTMyLTQzbC0zNC00M0w0NTkgNjVNMTE5IDY1bDMyLTE4IDMyIDE4IDMyIDE4LTM2LTQ0bC0zMiAxOGwtMzIgMTgtMzIgMThNMTA0OSAyNDhsLTEzLTQzbC0zNC00M0w5NTkgMjQ4TTczOSAyNDhsLTMyLTQzbC0zNC00M0w2NDkgMTc4TTMzOSAyNDhsLTMyLTQzbC0zNC00M0wyNDkgMTc4TTE0OSAzNDZ sMzItMTggMzIgMTggMzIgMTgtMzYtNDREMTgzIDM0NmwtMzIgMTgtMzIgMTgvPiA8L3N2Zz4=');
        background-repeat: repeat;
        background-attachment: fixed;
        background-size: 300px;
        color: white;
        animation: chartBackgroundSlide 60s linear infinite;
        
        /* الإطار الذهبي الفني المحيط بالموقع */
        border: 15px solid #ffd700;
        border-radius: 20px;
        box-sizing: border-radius;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.3) inset, 0 0 30px rgba(255, 215, 0, 0.3);
        margin: 10px; /* لإعطاء مسافة للإطار */
    }
    
    /* أنيميشن تحرك الخلفية */
    @keyframes chartBackgroundSlide {
        from { background-position: 0 0; }
        to { background-position: -600px 300px; }
    }
    
    * { direction: rtl; } /* اتجاه الكتابة عربي */
    
    /* تنسيق العناوين الرئيسية */
    .main-title { text-align: center; color: #ffd700; font-size: 45px; font-weight: bold; margin-bottom: 5px; text-shadow: 2px 2px 10px rgba(255, 215, 0, 0.4); }
    .sub-title { text-align: center; color: #888; font-size: 18px; margin-bottom: 30px; }
    
    /* تنسيق خانة إدخال السعر - متجاوبة وموسعة */
    .stNumberInput label { 
        width: 100% !important; text-align: center !important; 
        color: #ffd700 !important; font-size: 35px !important; 
        font-weight: bold !important; display: block !important; 
    }
    div.stNumberInput { max-width: 700px; margin: 0 auto !important; }
    input { 
        text-align: center !important; font-size: 35px !important; height: 75px !important; 
        color: white !important; background-color: rgba(60, 60, 50, 0.8) !important; 
        border: 2px solid #ffd700 !important; border-radius: 15px !important; 
    }
    
    /* بطاقات عرض أسعار الذهب - متجاوبة وفخمة */
    .price-card { 
        border: 1px solid #3d3d36; padding: 35px; border-radius: 15px; 
        text-align: center; background-color: rgba(60, 60, 50, 0.9); margin-top: 20px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        min-width: 200px; /* لضمان عدم صغر الحجم في الموبايل */
    }
    .price-val { color: white; font-size: 50px; font-weight: bold; margin-top: 10px; }
    .gold-label { color: #ffd700; font-size: 24px; font-weight: bold; }
    
    /* تنسيق القسم الجانبي (الأزرار) */
    .agency-box {
        border: 2px solid #ffd700; padding: 25px; border-radius: 15px; 
        background-color: rgba(60, 60, 50, 0.9); text-align: center;
        box-shadow: 0 4px 20px rgba(255, 215, 0, 0.2);
    }
    .agency-logo-container { text-align: center; margin-bottom: 20px; color: #ffd700; }
    .btn-gold { background-color: #ffd700; color: #000 !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    .btn-white { background-color: white; color: #000 !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    .btn-wa { background-color: #25d366; color: white !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    
    /* التوقيع الذهبي */
    .developer-credit { text-align: center; color: #ffd700; font-size: 25px; font-weight: bold; margin-top: 50px; text-shadow: 2px 2px 10px rgba(255, 215, 0, 0.4); }
    </style>
""", unsafe_allow_html=True)

# --- 4. دالة جلب السعر العالمي ---
def get_gold_spot_price():
    default_price = 4497.0
    if YF_AVAILABLE:
        try:
            gold = yf.Ticker("GC=F")
            data = gold.history(period="1d")
            if not data.empty:
                return round(data['Close'].iloc[-1], 2)
        except:
            return default_price
    return default_price

# --- 5. واجهة المستخدم الرئيسية ---
st.markdown("<div class='main-title'>🔱 نظام تسعير الذهب العالمي 🔱</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>دقة عالمية في متناول يدك لأسعار الذهب والسبائك</div>", unsafe_allow_html=True)

live_price = get_gold_spot_price()
col_main, col_side = st.columns([2.3, 1])

with col_main:
    # خانة إدخال السعر
    ounce_input = st.number_input("أدخل سعر الأونصة العالمي الحالي ($)", value=float(live_price))
    
    # العمليات الحسابية بناءً على وزن الأونصة
    troy_ounce = 31.1035
    p24 = ounce_input / troy_ounce
    p21 = p24 * 0.875
    p18 = p24 * 0.75
    
    # عرض بطاقات الأسعار - متجاوبة
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
    with c2: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
    with c3: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

with col_side:
    # القسم الجانبي المخصص لـ "جوست ماركت" وشعار الوكالة
    st.markdown(f"""
        <div class='agency-box'>
            <div class='agency-logo-container'>
                <span style='font-size: 50px;'>🔱</span><br>
                <span style='font-size: 28px; font-weight: bold;'>جوست ماركت</span>
            </div>
            <h2 style='color: #ffd700; margin-bottom: 15px;'>📉 استثمر في الذهب</h2>
            <a class='btn-gold' href='https://justmarkets.com/'>فتح حساب تداول تحت وكالتنا</a>
            <a class='btn-white' href='#'>تحميل تطبيق مباشر</a>
            <a class='btn-wa' href='https://wa.me/963950555563'>💬 تواصل واتساب مباشر</a>
            <p style='font-size: 14px; color: #888; margin-top: 15px;'>الوكيل المعتمد لجوست ماركت: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

# --- 6. قسم سياسة الخصوصية واستخدام البيانات ---
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("📄 سياسة الخصوصية لموقع جوست ماركت"):
    st.write("""
    ### سياسة الخصوصية واستخدام البيانات
    هذا الموقع يوفر أسعار الذهب للأغراض المعلوماتية فقط. نحن لا نجمع أي بيانات شخصية أو حساسة عن زوارنا. 
    يتم استخدام كوكيز الطرف الثالث عبر **Google AdSense** لعرض الإعلانات بناءً على زياراتك السابقة.
    بإمكانك تعطيل ملفات تعريف الارتباط من إعدادات متصفحك في أي وقت.
    """)

# التوقيع الذهبي
st.markdown("<div class='developer-credit'>تم التطوير بواسطة: عقيل فرح 👨‍💻</div>", unsafe_allow_html=True)