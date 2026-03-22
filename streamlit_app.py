import streamlit as st
import streamlit.components.v1 as components
try:
    import yfinance as yf
    YF_AVAILABLE = True
except ImportError:
    YF_AVAILABLE = False

# 1. إعدادات الصفحة
st.set_page_config(page_title="جوست ماركت - تسعير الذهب", page_icon="🔱", layout="wide")

# 2. كود AdSense (للمراجعة والأرباح)
adsense_script = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6456486381436649"
     crossorigin="anonymous"></script>
"""
components.html(adsense_script, height=0)

# 3. التنسيق البصري الكامل (إخفاء Streamlit + التصميم الذهبي)
st.markdown("""
    <style>
    /* إخفاء الهوية الافتراضية لـ Streamlit تماماً */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* لون الخلفية والخطوط */
    [data-testid="stAppViewContainer"] { background-color: #1a1a16; color: white; }
    * { direction: rtl; }
    
    .main-title { text-align: center; color: #ffd700; font-size: 45px; font-weight: bold; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #888; font-size: 18px; margin-bottom: 30px; }
    
    /* تنسيق خانة إدخل السعر (كبيرة وواضحة) */
    .stNumberInput label { 
        width: 100% !important; text-align: center !important; 
        color: #ffd700 !important; font-size: 35px !important; 
        font-weight: bold !important; display: block !important; 
    }
    div.stNumberInput { max-width: 700px; margin: 0 auto !important; }
    input { 
        text-align: center !important; font-size: 35px !important; height: 75px !important; 
        color: white !important; background-color: #262621 !important; 
        border: 2px solid #ffd700 !important; border-radius: 15px !important; 
    }
    
    /* بطاقات عيارات الذهب */
    .price-card { 
        border: 1px solid #3d3d36; padding: 35px; border-radius: 15px; 
        text-align: center; background-color: #262621; margin-top: 20px; 
    }
    .price-val { color: white; font-size: 50px; font-weight: bold; margin-top: 10px; }
    .gold-label { color: #ffd700; font-size: 24px; font-weight: bold; }
    
    /* تنسيق الأزرار الجانبية الثلاثة */
    .btn-gold { background-color: #ffd700; color: #000 !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    .btn-white { background-color: white; color: #000 !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    .btn-wa { background-color: #25d366; color: white !important; padding: 15px; border-radius: 10px; text-decoration: none; display: block; margin: 12px 0; font-weight: bold; text-align: center; font-size: 18px; }
    
    .developer-credit { text-align: center; color: #ffd700; font-size: 25px; font-weight: bold; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

# 4. دالة جلب السعر مع السعر الافتراضي المحدث (4497.0)
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

# 5. عرض المحتوى الرئيسي
st.markdown("<div class='main-title'>🔱 نظام تسعير الذهب العالمي 🔱</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>دقة عالمية في متناول يدك لأسعار الذهب والسبائك</div>", unsafe_allow_html=True)

live_price = get_gold_spot_price()
col_main, col_side = st.columns([2.3, 1])

with col_main:
    # خانة الإدخال المكبرة
    ounce_input = st.number_input("أدخل سعر الأونصة العالمي الحالي ($)", value=float(live_price))
    
    # العمليات الحسابية
    troy_ounce = 31.1035
    p24 = ounce_input / troy_ounce
    p21 = p24 * 0.875
    p18 = p24 * 0.75
    
    # عرض البطاقات
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
    with c2: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
    with c3: st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

with col_side:
    # القسم الجانبي (الأزرار والوكالة)
    st.markdown(f"""
        <div style='border: 1px solid #ffd700; padding: 25px; border-radius: 15px; background-color: #262621; text-align: center;'>
            <h2 style='color: #ffd700; margin-bottom: 20px;'>📈 استثمر في الذهب</h2>
            <a class='btn-gold' href='https://justmarkets.com/'>فتح حساب تحت وكالتنا</a>
            <a class='btn-white' href='#'>تحميل تطبيق مباشر</a>
            <a class='btn-wa' href='https://wa.me/963950555563'>💬 تواصل واتساب مباشر</a>
            <p style='font-size: 14px; color: #888; margin-top: 15px;'>الوكيل المعتمد: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

# 6. قسم سياسة الخصوصية (أساسي لقبول أدسنس)
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📄 سياسة الخصوصية واستخدام البيانات"):
    st.write("""
    هذا الموقع يوفر أسعار الذهب للأغراض المعلوماتية فقط. نحن لا نجمع بيانات شخصية عن زوارنا. 
    يتم عرض الإعلانات بواسطة Google AdSense والتي قد تستخدم ملفات تعريف الارتباط (cookies) لتحسين تجربتك.
    """)

# 7. التوقيع الذهبي المكبر
st.markdown("<div class='developer-credit'>تم التطوير بواسطة: عقيل فرح 👨‍💻</div>", unsafe_allow_html=True)