import streamlit as st
import yfinance as yf

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="نظام تسعير الذهب العالمي", page_icon="🔱", layout="wide")

# تنسيق CSS مخصص لاستعادة الألوان والخطوط الكبيرة
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    body { background-color: #0e1117; color: white; }
    * { direction: rtl; }
    
    /* تنسيق العنوان الرئيسي */
    .main-title { text-align: center; color: #ffd700; font-size: 45px; font-weight: bold; margin-bottom: 0px; }
    .sub-title { text-align: center; color: #888; font-size: 18px; margin-bottom: 30px; }
    
    /* جعل تسمية مدخل السعر في المنتصف وبخط كبير */
    label { 
        width: 100% !important; 
        text-align: center !important; 
        color: #ffd700 !important; 
        font-size: 24px !important; 
        font-weight: bold !important;
        display: block !important;
    }
    
    /* تنسيق خانة إدخال السعر */
    div.stNumberInput { max-width: 400px; margin: 0 auto; }
    input { text-align: center !important; font-size: 22px !important; color: white !important; background-color: #161a23 !important; border: 1px solid #ffd700 !important; }

    /* تنسيق بطاقات الأسعار */
    .price-card {
        border: 1px solid #444;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        background-color: #161a23;
        transition: 0.3s;
    }
    .price-card:hover { border-color: #ffd700; }
    .price-val { color: white; font-size: 50px; font-weight: bold; margin-top: 10px; }
    .gold-label { color: #ffd700; font-size: 24px; font-weight: bold; }

    /* تنسيق العمود الجانبي (بطاقة استثمر) */
    .sidebar-card {
        border: 1px solid #ffd700;
        padding: 25px;
        border-radius: 15px;
        background-color: #161a23;
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

# 3. عرض العناوين
st.markdown("<div class='main-title'>🔱 نظام تسعير الذهب العالمي 🔱</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>دقة عالمية في متناول يدك</div>", unsafe_allow_html=True)

live_price = get_gold_spot_price()

# 4. تقسيم المحتوى
col_main, col_side = st.columns([2.2, 1])

with col_main:
    # مدخل السعر في المنتصف تماماً مع تكبير الخط
    ounce_input = st.number_input("أدخل سعر الأونصة ($)", value=float(live_price), step=1.0)
    
    # الحسابات الفنية
    troy_ounce = 31.1035
    p24 = ounce_input / troy_ounce
    p21 = p24 * 0.875
    p18 = p24 * 0.75

    st.markdown("<br>", unsafe_allow_html=True)
    
    # عرض النتائج في بطاقات كبيرة
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

with col_side:
    # بطاقة الاستثمار والهوية
    st.markdown(f"""
        <div class='sidebar-card'>
            <h2 style='color: #ffd700;'>📈 استثمر في الذهب</h2>
            <p style='font-size: 14px; color: #ccc;'>JustMarkets تداول الذهب بروافع مالية وسبريد منخفض جداً</p>
            <a class='btn-gold' href='#'>فتح حساب تداول وكيل</a>
            <a class='btn-white' href='#'>تحميل التطبيق المباشر</a>
            <p style='margin-top: 20px; font-size: 16px; color: #ffd700;'>💬 واتساب: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

# التذييل
st.markdown("<br><p style='text-align: center; color: #555; font-size: 14px;'>تم التطوير بواسطة: عقيل فرح 👨‍💻</p>", unsafe_allow_html=True)