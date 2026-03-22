import streamlit as st
import yfinance as yf

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="جوست ماركت - تسعير الذهب", page_icon="🔱", layout="wide")

# تنسيق CSS لاستخدام لون الخلفية المحدد وتنسيق الخطوط
st.markdown("""
    <style>
    /* إخفاء عناصر Streamlit غير الضرورية */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* لون الخلفية الدقيق المستخرج من الصورة */
    [data-testid="stAppViewContainer"] {
        background-color: #1a1a16; /* الدرجة الداكنة المطلوبة */
        color: white;
    }
    
    * { direction: rtl; }
    
    /* تنسيق العنوان الرئيسي */
    .main-title { text-align: center; color: #ffd700; font-size: 45px; font-weight: bold; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #888; font-size: 18px; margin-bottom: 40px; }
    
    /* توسيط وتكبير عنوان مدخل السعر */
    .stNumberInput label { 
        width: 100% !important; 
        text-align: center !important; 
        color: #ffd700 !important; 
        font-size: 30px !important; 
        font-weight: bold !important;
        display: block !important;
    }
    
    /* تنسيق خانة إدخال السعر */
    div.stNumberInput { max-width: 500px; margin: 0 auto !important; }
    input { 
        text-align: center !important; 
        font-size: 26px !important; 
        color: white !important; 
        background-color: #262621 !important; 
        border: 1px solid #ffd700 !important; 
        border-radius: 12px !important;
    }

    /* تنسيق بطاقات الأسعار */
    .price-card {
        border: 1px solid #3d3d36;
        padding: 35px;
        border-radius: 15px;
        text-align: center;
        background-color: #262621;
        margin-top: 20px;
    }
    .price-val { color: white; font-size: 50px; font-weight: bold; margin-top: 10px; }
    .gold-label { color: #ffd700; font-size: 24px; font-weight: bold; }

    /* تنسيق العمود الجانبي */
    .sidebar-card {
        border: 1px solid #ffd700;
        padding: 25px;
        border-radius: 15px;
        background-color: #262621;
        text-align: center;
    }
    .btn-gold {
        background-color: #ffd700; color: black; padding: 12px; border-radius: 8px;
        text-decoration: none; display: block; margin: 10px 0; font-weight: bold; font-size: 18px;
    }
    .btn-white {
        background-color: white; color: black; padding: 12px; border-radius: 8px;
        text-decoration: none; display: block; margin: 10px 0; font-weight: bold; font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. دالة جلب السعر المباشر
@st.cache_data(ttl=60)
def get_gold_spot_price():
    try:
        gold = yf.Ticker("GC=F")
        price = gold.history(period="1d")['Close'].iloc[-1]
        return round(price, 2)
    except:
        return 2290.0

# 3. واجهة المستخدم
st.markdown("<div class='main-title'>🔱 نظام تسعير الذهب العالمي 🔱</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>دقة عالمية في متناول يدك</div>", unsafe_allow_html=True)

live_price = get_gold_spot_price()

col_main, col_side = st.columns([2.3, 1])

with col_main:
    # مدخل السعر (في المنتصف وبخط كبير)
    ounce_input = st.number_input("أدخل سعر الأونصة الحالي ($)", value=float(live_price))
    
    # الحسابات
    troy_ounce = 31.1035
    p24 = ounce_input / troy_ounce
    p21 = p24 * 0.875
    p18 = p24 * 0.75

    st.markdown("<br>", unsafe_allow_html=True)
    
    # بطاقات الأسعار
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

with col_side:
    st.markdown(f"""
        <div class='sidebar-card'>
            <h2 style='color: #ffd700;'>📈 استثمر في الذهب</h2>
            <p style='font-size: 14px; color: #ccc;'>JustMarkets تداول الذهب بروافع مالية وسبريد منخفض جداً</p>
            <a class='btn-gold' href='#'>فتح حساب تداول وكيل</a>
            <a class='btn-white' href='#'>تحميل التطبيق المباشر</a>
            <p style='margin-top: 20px; font-size: 16px; color: #ffd700;'>💬 واتساب: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #555;'>تم التطوير بواسطة: عقيل فرح 👨‍💻</p>", unsafe_allow_html=True)