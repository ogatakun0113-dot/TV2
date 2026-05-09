import streamlit as st
from datetime import datetime, timedelta, timezone

# ページ設定
st.set_page_config(page_title="緒方メディアハブ", layout="wide")

# 日本標準時 (JST) を確実に取得する設定
JST = timezone(timedelta(hours=+9), 'JST')
now_jst = datetime.now(JST)

# スタイリッシュで目に優しい「薄い色」のカスタムCSS
st.markdown("""
<style>
    /* 全体背景：薄いグレーベージュ */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* クレジットとタイトル */
    .credit { text-align: right; font-size: 14px; color: #555; margin-bottom: -10px; }
    h1 { color: #1e3a5f; font-size: 38px !important; border-bottom: 2px solid #005A9C; padding-bottom: 10px; }
    
    /* メインボタン：はっきりした青 */
    .main-btn { 
        background-color: #ffffff;
        color: #005A9C !important; 
        padding: 22px; 
        border-radius: 12px; 
        text-align: center; 
        text-decoration: none; 
        display: block; 
        font-size: 22px; 
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border: 2px solid #005A9C;
        transition: 0.3s;
    }
    .main-btn:hover { 
        background-color: #005A9C;
        color: #ffffff !important;
        text-decoration: none;
    }
    
    /* ラジオボタン：はっきりしたオレンジ */
    .radio-btn {
        color: #d35400 !important;
        border: 2px solid #d35400;
    }
    .radio-btn:hover {
        background-color: #d35400;
        color: #ffffff !important;
    }

    /* カレンダー部分 */
    .stDateInput div {
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 緒方メディアハブ")

# --- 日付選択エリア ---
st.write(f"🕒 現在の日本時間: **{now_jst.strftime('%Y/%m/%d %H:%M')}**")
# デフォルト値を「今この瞬間の日本時間の日付」に固定
selected_date = st.date_input("番組表の日付を選択", value=now_jst)

# 日付パラメータ生成
date_param = selected_date.strftime("%Y%m%d")
display_date = selected_date.strftime("%Y年%m月%d日")

st.markdown(f"### ✨ {display_date} の番組表案内")

# --- 各種番組表へのダイレクトリンク ---

col1, col2 = st.columns(2)

with col1:
    # 1. 地デジ (大阪: ggm_group_id=84)
    td_url = f"https://bangumi.org/epg/td?broad_cast_date={date_param}&ggm_group_id=84"
    st.markdown(f'<a href="{td_url}" target="_blank" class="main-btn">📡 地デジ（大阪）</a>', unsafe_allow_html=True)

    # 2. BS放送
    bs_url = f"https://bangumi.org/epg/bs?broad_cast_date={date_param}"
    st.markdown(f'<a href="{bs_url}" target="_blank" class="main-btn">🛰️ BS放送</a>', unsafe_allow_html=True)

with col2:
    # 3. CS放送
    cs_url = f"https://bangumi.org/epg/cs?broad_cast_date={date_param}"
    st.markdown(f'<a href="{cs_url}" target="_blank" class="main-btn">🎬 CS放送</a>', unsafe_allow_html=True)

    # 4. ラジオ番組表 (大阪: ggm_group_id=84)
    radio_url = f"https://bangumi.org/epg/radio?broad_cast_date={date_param}&ggm_group_id=84"
    st.markdown(f'<a href="{radio_url}" target="_blank" class="main-btn radio-btn">📻 ラジオ番組表</a>', unsafe_allow_html=True)

st.markdown("---")
st.info(f"💡 日付は自動で日本時間に更新されます。現在は **{date_param}** 用のリンクです。")

