import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="نظام تسعير الذهب | عقيل فرح", layout="wide")

# 2. تصميم الواجهة وإخفاء العناصر غير المرغوبة (أيقونة الدعم والقائمة)
st.markdown("""
    <style>
    /* إخفاء القائمة وأيقونة الدعم والFooter */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* تحسين الخلفية */
    .stApp {
        background: linear-gradient(135deg, #0d0d0b, #1a1a16, #2d2d24);
        color: white;
    }
    
    /* تكبير عنوان إدخال السعر */
    .stNumberInput label {
        font-size: 28px !important;
        font-weight: bold !important;
        color: #ffd700 !important;
        display: block;
        text-align: center;
        margin-bottom: 15px;
    }

    /* تصميم البطاقات السعرية */
    .price-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        text-align: center;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    .label-text {
        color: #ffd700;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .price-text {
        font-size: 2.5rem;
        font-weight: 800;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# عنوان الموقع
st.markdown("<h1 style='text-align: center; color: #ffd700;'>🔱 نظام تسعير الذهب العالمي 🔱</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8;'>دقة عالمية في متناول يدك</p>", unsafe_allow_html=True)

st.write("---")

# منطقة الحسابات
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### لوحة الحساب ⚙️")
    # تم تكبير الخط الخاص بهذا العنوان عبر CSS أعلاه
    gold_price_oz = st.number_input("($) أدخل سعر الأونصة العالمي الحالي", min_value=0.0, value=2290.0, step=1.0)
    
    # حسابات العيارات (الأونصة = 31.1035 جرام)
    price_per_gram_24 = gold_price_oz / 31.1035
    price_per_gram_21 = price_per_gram_24 * (21/24)
    price_per_gram_18 = price_per_gram_24 * (18/24)

    st.write(" ")
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.markdown(f"<div class='price-card'><div class='label-text'>عيار 24</div><div class='price-text'>${price_per_gram_24:.2f}</div></div>", unsafe_allow_html=True)
    with res_col2:
        st.markdown(f"<div class='price-card'><div class='label-text'>عيار 21</div><div class='price-text'>${price_per_gram_21:.2f}</div></div>", unsafe_allow_html=True)
    with res_col3:
        st.markdown(f"<div class='price-card'><div class='label-text'>عيار 18</div><div class='price-text'>${price_per_gram_18:.2f}</div></div>", unsafe_allow_html=True)

with col2:
    # صندوق الإعلان لشركة JustMarkets
    st.markdown("""
        <div style="background: rgba(255, 215, 0, 0.05); padding: 30px; border-radius: 20px; border: 2px dashed #ffd700; text-align: center;">
            <h2 style="color: #ffd700;">📊 استثمر في الذهب</h2>
            <p style="font-size: 14px;">تداول الذهب برافعة مالية وسبريد منخفض جداً عبر <b>JustMarkets</b></p>
            <a href='https://justmarkets.com' style='display: inline-block; background: #ffd700; color: black; padding: 12px 25px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 10px;'>فتح حساب تداول وكيل</a>
            <br><br>
            <a href='#' style='display: inline-block; background: white; color: black; padding: 10px 20px; border-radius: 10px; text-decoration: none; font-size: 14px;'>تحميل التطبيق مباشر</a>
            <p style="margin-top: 20px; font-size: 13px;">💬 تواصل معي واتساب: 0950555563</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='text-align: center; font-size: 0.8rem; opacity: 0.6;'>👨‍💻 تم التطوير بواسطة: عقيل فرح</p>", unsafe_allow_html=True)