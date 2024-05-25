import streamlit as st
import numpy as np
from joblib import load

# 保存された決定木モデルをロード
model = load("decision_tree_model.joblib")

# タイトルの設定
st.title('決定木モデル予測アプリ')

# ユーザー入力を受け取る
st.subheader('特徴量を入力してください')

# 特徴量の入力
feature1 = st.number_input('特徴量 1')
feature2 = st.number_input('特徴量 2')
feature3 = st.number_input('特徴量 3')
feature4 = st.number_input('特徴量 4')

# 予測ボタン
if st.button('予測'):
    # 入力特徴量をnumpy配列に変換
    features = np.array([[feature1, feature2, feature3, feature4]])
    
    # 予測の実行
    prediction = model.predict(features)
    
    # 予測結果の表示
    st.write('予測結果:', prediction)

