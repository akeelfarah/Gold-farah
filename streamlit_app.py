import streamlit as st
import streamlit.components.v1 as components
import os

# 1. إثبات الملكية (Meta Tag)
verify_tag = '<meta name="google-adsense-account" content="ca-pub-6456486381436649">'

# 2. جسر برمي لملف ads.txt الصغير
if "ads" in st.query_params:
    if os.path.exists("ads.txt"):
        with open("ads.txt", "r") as f:
            st.text(f.read())
        st.stop()

st.set_page_config(page_title="جوست ماركت", layout="wide")

# حقن الكود في رأس الصفحة
components.html(f"<html><head>{verify_tag}</head></html>", height=0)

# محتوى الموقع البسيط للتجربة
st.title("🔱 نظام تسعير الذهب العالمي")
st.write("الموقع قيد المراجعة من قبل AdSense...")