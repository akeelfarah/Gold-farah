import streamlit as st
import yfinance as yf

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="جوست ماركت - تسعير الذهب", page_icon="🔱", layout="wide")

# تنسيق CSS مخصص للتكبير وتعديل الأزرار
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* لون الخلفية الداكن المطلوب */
    [data-testid="stAppViewContainer"] {
        background-color: #1a1a16;
        color: white;
    }
    
    * { direction: rtl; }
    
    .main-title { text-align: center; color: #ffd700; font-size: 45px; font-weight: bold; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #888; font-size: 18px; margin-bottom: 40px; }
    
    /* تكبير وتوسيط عنوان مدخل السعر */
    .stNumberInput label { 
        width: 100% !important; 
        text-align: center !important; 
        color: #ffd700 !important; 
        font-size: 35px !important; 
        font-weight: bold !important;
        display: block !important;
    }
    
    /* تكبير خانة إدخال السعر لتصبح ضخمة وواضحة */
    div.stNumberInput { max-width: 700px; margin: 0 auto !important; }
    input { 
        text-align: center !important; 
        font-size: 35px !important; 
        height: 70px !important;
        color: white !important; 
        background-color: #262621 !important; 
        border: 2px solid #ffd700 !important; 
        border-radius: 15px !important;
    }

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

    /* تنسيق العمود الجانبي والأزرار الثلاثة */
    .sidebar-card {
        border: 1px solid #ffd700;
        padding: 25px;
        border-radius: 15px;
        background-color: #262621;
        text-align: center;
    }
    .btn-gold {
        background-color: #ffd700; color: #000 !important; padding: 15px; border-radius: 10px;
        text-decoration: none; display: block; margin: 12px 0; font-weight: bold; font-size: 18px;
    }
    .btn-white {
        background-color: white; color: #000 !important; padding: 15px; border-radius: 10px;
        text-decoration: none; display: block; margin: 12px 0; font-weight: bold; font-size: 18px;
    }
    .btn-wa {
        background-color: #25d366; color: white !important; padding: 15px; border-radius: 10px;
        text-decoration: none; display: block; margin: 12px 0; font-weight: bold; font-size: 18px;
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
    # خانة السعر المكبرة
    ounce_input = st.number_input("أدخل سعر الأونصة العالمي ($)", value=float(live_price))
    
    troy_ounce = 31.1035
    p24 = ounce_input / troy_ounce
    p21 = p24 * 0.875
    p18 = p24 * 0.75

    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 24</div><div class='price-val'>${p24:.2f}</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 21</div><div class='price-val'>${p21:.2f}</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='price-card'><div class='gold-label'>عيار 18</div><div class='price-val'>${p18:.2f}</div></div>", unsafe_allow_html=True)

with col_side:
    # الأزرار الثلاثة بتنسيق موحد وأنيق
    st.markdown(f"""
        <div class='sidebar-card'>
            <h2 style='color: #ffd700; margin-bottom: 20px;'>📈 استثمر في الذهب</h2>
            <a class='btn-gold' href='https://one.justmarkets.link/a/4f59i0rjez'>فتح حساب تحت وكالتنا</a>
            <a class='btn-white' href='#'>تحميل تطبيق مباشر</a>
            <a class='btn-wa' href='https://wa.me/963950555563'>💬 تواصل واتساب مباشر</a>
            <p style='font-size: 12px; color: #888; margin-top: 10px;'>الوكيل المعتمد: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #555;'>تم التطوير بواسطة: عقيل فرح 👨‍💻</p>", unsafe_allow_html=True)