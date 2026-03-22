import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="نظام تسعير الذهب | عقيل فرح", page_icon="💰", layout="wide")

# 2. تصميم الواجهة المتقدم (CSS)
st.markdown("""
    <style>
    /* تحسين الخلفية */
    .stApp {
        background: linear-gradient(135deg, #0d0d0b, #1a1a16, #2d2d24);
        color: white;
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
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .price-text {
        color: #ffffff;
        font-size: 48px; /* خط كبير جداً للسعر */
        font-weight: 900;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* تنسيق الأزرار */
    .main-btn {
        background: linear-gradient(90deg, #ffd700, #b8860b);
        color: black !important;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        display: block;
        margin: 10px 0;
        text-align: center;
        font-size: 18px;
    }
    
    .dev-footer {
        text-align: center;
        padding: 30px;
        color: #ffd700;
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 40px;
        border-top: 1px solid rgba(255, 215, 0, 0.1);
    }

    /* لضمان التجاوب مع الموبايل */
    @media (max-width: 768px) {
        .price-text { font-size: 36px; }
        .label-text { font-size: 20px; }
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر
st.markdown("<h1 style='text-align: center; color: #ffd700;'>🔱 نظام تسعير الذهب العالمي 🔱</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8;'>دقة عالمية في متناول يدك</p>", unsafe_allow_html=True)

# 4. منطقة العمل
col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown('<div style="background: rgba(255,255,255,0.05); padding: 30px; border-radius: 20px;">', unsafe_allow_html=True)
    ounce_price = st.number_input("أدخل سعر الأونصة ($)", min_value=0.0, value=4490.0, step=0.1)
    
    # الحسابات
    g24 = ounce_price / 31.1035
    g21 = g24 * 0.875
    g18 = g24 * 0.75
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # عرض الأسعار بخط كبير جداً
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f'<div class="price-card"><div class="label-text">عيار 24</div><div class="price-text">${g24:.2f}</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="price-card"><div class="label-text">عيار 21</div><div class="price-text">${g21:.2f}</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="price-card"><div class="label-text">عيار 18</div><div class="price-text">${g18:.2f}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style="background: rgba(0,0,0,0.3); padding: 25px; border-radius: 20px; border: 1px solid #ffd700; text-align: center;">
            <h2 style='color: #ffd700;'>📈 استثمر في الذهب</h2>
            <p>تداول الذهب برافعة مالية وسبريد منخفض جداً عبر JustMarkets</p>
            <a href="https://one.justmarkets.link/a/4f59i0rjez" class="main-btn">فتح حساب تداول وكيل</a>
            <a href="https://justmarkets.com/downloads" class="main-btn" style="background: white;">تحميل التطبيق المباشر</a>
            <hr style='border-color: rgba(255,215,0,0.2)'>
            <a href="https://wa.me/963950555563" style="color: #ffd700; text-decoration: none; font-weight: bold;">💬 واتساب: 0950555563</a>
        </div>
    """, unsafe_allow_html=True)

# 5. التوقيع النهائي
st.markdown('<div class="dev-footer">👨‍💻 تم التطوير بواسطة: عقيل فرح</div>', unsafe_allow_html=True)