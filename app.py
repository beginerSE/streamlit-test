# import streamlit as st
# import pandas as pd
# import numpy as np

# # データの生成
# data = pd.DataFrame({
#     'A': np.random.rand(10),
#     'B': np.random.rand(10),
#     'C': np.random.rand(10)
# })

# # Streamlitアプリのタイトル
# st.title('Streamlit データ表示デモ')

# # DataFrameを動的に表示
# st.header('動的なDataFrame表示')
# st.dataframe(data)

# # テーブルを静的に表示
# st.header('静的なテーブル表示')
# st.table(data.describe())  # dataの統計的要約を表示


# import streamlit as st

# def main():

#     st.title("Streamlit 入力フィールド サンプル")

#     # テキスト入力フィールド
#     user_name = st.text_input(
#         '名前を入力してください',
#         'ここに名前を書いてください'
#     )

#     if user_name:
#         st.write("こんにちは、", user_name, "さん！")

#     # 数値入力フィールド
#     age = st.number_input(
#         "年齢を入力してください",
#          min_value=0, 
#          max_value=100, 
#          value=25, 
#          step=1
#     )
    
#     if age:
#         st.write("あなたの年齢は", age, "歳です。")

#     # ユーザーがフォームを使って入力した情報に基づいてさらに処理を行う場合
#     # 例：年齢によってメッセージを変える
#     if age < 18:
#         st.write("あなたは未成年です。")
#     elif age >= 18:
#         st.write("あなたは成人です。")

# if __name__ == "__main__":
#     main()


# import streamlit as st

# # ボタンを使用して特定のアクションを実行
# if st.button('Click me'):
#     st.write('Thanks for clicking!')

# # チェックボックスを使用して表示内容を切り替え
# if st.checkbox('Show message'):
#     st.write('You checked the box!')

# # ラジオボタンを使用して選択肢から選ぶ
# choice = st.radio('Choose a color:', ['Red', 'Blue', 'Green'])
# st.write(f'You selected {choice}.')

# # スライダーを使用して数値を選択
# number = st.slider('Select a number:', 0, 100, 25)
# st.write(f'The selected number is {number}.')

# # ファイルアップローダーを使用してファイルをアップロード
# uploaded_file = st.file_uploader('Upload a file')
# if uploaded_file is not None:
#     # ここにファイル処理のコードを追加
#     st.write('File uploaded successfully.')


# import streamlit as st

# # スライダーを用いて年齢を選択する例
# age = st.slider(
#     'Choose your age', 
#     min_value=0, 
#     max_value=100, 
#     value=25
# )
# st.write('Your age is:', age)

# import streamlit as st

# # 範囲選択スライダーを用いて価格範囲を選択する例
# price_range = st.select_slider(
#     'Select a price range',
#     options=[
#         '$0-$20',
#         '$21-$40', 
#         '$41-$60', 
#         '$61-$80', 
#         '$81-$100'
#     ],
#     value=(
#         '$21-$40', 
#         '$61-$80'
#     )
# )
# st.write('You selected:', price_range)



# import streamlit as st

# # 年齢範囲を選択するスライダー
# age_range = st.slider(
#     'Select your age range', 
#     min_value=0, 
#     max_value=100, 
#     value=(25, 75)
# )

# # 価格範囲を選択するセレクトスライダー
# price_range = st.select_slider(
#     'Select a price range',
#     options=[
#         '$0-$20', 
#         '$21-$40', 
#         '$41-$60', 
#         '$61-$80', 
#         '$81-$100'
#     ],
#     value=(
#         '$21-$40', 
#         '$61-$80'
#     )
# )

# # 選択された年齢範囲と価格範囲の表示
# st.write('Selected age range:', age_range)
# st.write('Selected price range:', price_range)



# import streamlit as st
# from datetime import time

# # デフォルトの時間を午前9時に設定
# default_time = time(9, 0)
# selected_time = st.time_input("Select time", default_time)
# st.write("Selected Time:", selected_time)



# import streamlit as st
# import datetime

# # 初期値として今日の日付を設定
# today = datetime.date.today()
# selected_date = st.date_input("Select a date", today)
# st.write("Selected Date:", selected_date)



# import streamlit as st

# col1, col2 = st.columns(2)  # 2つのカラムを作成
# with col1:
#     st.header("カラム1")
#     st.write("ここはカラム1です。")
# with col2:
#     st.header("カラム2")
#     st.write("ここはカラム2です。")



# import streamlit as st

# expander = st.expander("Click to expand")

# with expander:
#     st.write(
#         "Here is some hidden content that can be expanded or collapsed"
#         )


# import streamlit as st

# # サイドバーの設定
# with st.sidebar:
#     st.title("サイドバー")
#     user_input = st.text_input(
#         "あなたの名前を入力してください："
#     )

# # メイン画面のプレースホルダーを設定
# placeholder = st.empty()

# # ユーザーが何か入力した場合、メイン画面を更新
# if user_input:
#     with placeholder.container():
#         st.header(f"こんにちは、{user_input}さん！")
#         st.caption("Streamlit アプリへようこそ！")
#         st.write(
#             "ここにアプリの主要なコンテンツが表示されます。"
#         )
# else:
#     with placeholder.container():
#         st.write(
#             "サイドバーから名前を入力してください。"
#         )


# import streamlit as st
# import pandas as pd

# # ファイルアップロードのセクション
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
# if uploaded_file is not None:
#     # CSVファイルを読み込む
#     data = pd.read_csv(uploaded_file)
#     # データをStreamlitに表示
#     st.write("Here's the first five rows of your data:")
#     st.write(data.head())

#     # データ加工（例：すべての数値を2倍にする）
#     processed_data = data.applymap(lambda x: x*2 if type(x) is int or type(x) is float else x)
#     st.write("Here's the first five rows of the processed data:")
#     st.write(processed_data.head())

#     # 加工したデータをCSVファイルとしてダウンロード可能にする
#     csv = processed_data.to_csv(index=False)
#     st.download_button(
#         label="Download processed data as CSV",
#         data=csv,
#         file_name='processed_data.csv',
#         mime='text/csv'
#     )
# else:
#     st.write("Upload a CSV file to get started.")


# import streamlit as st

# with st.form("profile_form"):
#     st.write("Complete your profile")
#     first_name = st.text_input("First name")
#     last_name = st.text_input("Last name")
#     age = st.slider("Age", 18, 100)
#     bio = st.text_area("Bio")
#     submit = st.form_submit_button("Submit")

# if submit:
#     st.write("Profile Submitted:", first_name, last_name, age, bio)


# import streamlit as st
# import pandas as pd
# import numpy as np

# # サンプルデータの生成
# data = {
#     "ID": range(1, 11),
#     "Name": [
#         "Alice", 
#         "Bob", 
#         "Charlie", 
#         "David", 
#         "Eve", 
#         "Frank", 
#         "Grace", 
#         "Helen", 
#         "Isaac", 
#         "Julie"
#     ],
#     "Age": np.random.randint(18, 50, size=10),
#     "Status": ["Active", "Inactive"] * 5
# }
# df = pd.DataFrame(data)

# # ヘッダー
# st.header("Sample Data Filtering App")

# # ユーザー入力を受け取る
# name_input = st.text_input("Enter a name to filter:")
# status_options = st.multiselect(
#     "Select status:", 
#     options=df["Status"].unique(), 
#     default=df["Status"].unique()
# )

# # データフィルタリング
# filtered_data = df[(df["Name"].str.contains(name_input)) & (df["Status"].isin(status_options))]

# # データの表示
# st.subheader("Filtered Data")
# st.write(filtered_data)

# # ファイルダウンロード
# csv = filtered_data.to_csv(index=False).encode('utf-8')
# st.download_button(
#     "Download filtered data as CSV", 
#     csv, 
#     "filtered_data.csv", 
#     "text/csv"
# )

# # アプリのサイドバー
# st.sidebar.header("About App")
# st.sidebar.info(
#     "This is a sample data filtering app using various Streamlit components."
# )


# import streamlit as st
# import pandas as pd
# import numpy as np

# # データ生成
# data = pd.DataFrame({
#    'date': pd.date_range(start='1/1/2020', periods=100),
#    'value': np.random.randn(100).cumsum()
# })

# st.header(f"折れ線グラフのサンプル")

# # 折れ線グラフの描画
# st.line_chart(data.set_index('date'))


# import pandas as pd
# import streamlit as st

# st.header(f"棒グラフのサンプル")

# # データ生成
# data = pd.DataFrame({
#    'category': ['A', 'B', 'C'],
#    'value': [10, 20, 30]
# })

# # 棒グラフの描画
# st.bar_chart(data.set_index('category'))

# import streamlit as st
# import pandas as pd
# import numpy as np


# st.title('散布図のサンプル（Vega-Lite使用）')

# # データ生成
# data_size = 200
# data = pd.DataFrame({
#    'X軸': np.random.randn(data_size),
#    'Y軸': np.random.randn(data_size)
# })

# # Vega-Liteを使った散布図の作成
# scatter_chart = {
#    'mark': {'type': 'point', 'filled': True},
#    'encoding': {
#       'x': {'field': 'X軸', 'type': 'quantitative'},
#       'y': {'field': 'Y軸', 'type': 'quantitative'}
#    },
# }

# st.vega_lite_chart(data, scatter_chart)


# import streamlit as st
# import pandas as pd
# import numpy as np
# # データ生成
# data = pd.Series(np.random.randn(1000))

# st.title('ヒストグラムのサンプル')
# # ヒストグラムの描画
# st.hist_chart(data)


# import streamlit as st
# import pandas as pd
# import numpy as np


# st.title('ヒストグラムのサンプル')

# # データ生成
# data_size = 1000
# data = pd.Series(np.random.randn(data_size))

# # データのビニング
# hist_values = np.histogram(data, bins=20)[0]
# bin_edges = np.histogram(data, bins=20)[1]
# bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# # ヒストグラム用のデータフレームを作成
# hist_df = pd.DataFrame({
#     'bin_centers': bin_centers,
#     'counts': hist_values
# })

# # ヒストグラムの描画
# st.bar_chart(hist_df.set_index('bin_centers'))


# import streamlit as st
# import pandas as pd
# import numpy as np

# # データの生成
# @st.cache_data
# def create_data(size=365):
#     """ 1年分のランダムデータを生成 """
#     dates = pd.date_range(start='1/1/2020', periods=size)
#     values = np.random.randn(size).cumsum()  # 累積和を取ることでトレンドを模擬
#     return pd.DataFrame({'Date': dates, 'Value': values})

# def main():
#     st.title('Interactive Line Chart with Slider')

#     data = create_data()

#     # スライダーの設定
#     days_to_show = st.slider(
#         'Select range of days to display:', 
#         min_value=30, 
#         max_value=365, 
#         value=180, 
#         step=10
#     )

#     # データのフィルタリング
#     filtered_data = data.head(days_to_show)

#     # 折れ線グラフの表示
#     st.line_chart(filtered_data.set_index('Date'))

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import requests
# import time
# from datetime import datetime

# API_URL = "https://api.coin.z.com/public/v1/ticker?symbol=BTC_JPY"

# def get_bitcoin_price():
#     response = requests.get(API_URL)
#     if response.status_code == 200:
#         data = response.json()
#         return data['data'][0]['last'], 'online'
#     else:
#         return None, 'error'

# def main():
#     st.title('ビットコイン価格トラッカー')

#     # 初期価格とステータスの取得
#     price, status = get_bitcoin_price()
#     price_location = st.empty()
#     time_location = st.empty()
#     status_location = st.empty()

#     # ステータスに応じて異なる色でテキストを表示
#     if status == 'online':
#         price_location.write(f'現在のビットコイン価格: ¥{price}')
#         status_location.markdown(
#          f'<span style="color:green">オンライン</span>', unsafe_allow_html=True
#       )
#     else:
#         status_location.markdown(
#          f'<span style="color:red">APIエラー</span>', unsafe_allow_html=True
#       )

#     time_location.write(
#       f'最終更新時刻: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
#    )

#     # 指定された間隔で価格とステータスを更新
#     interval = st.sidebar.slider(
#       '更新間隔（秒）:', 
#       min_value=1, 
#       max_value=600, 
#       value=3
#    )
#     while True:
#         time.sleep(interval)
#         new_price, new_status = get_bitcoin_price()
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         if new_status == 'online':
#             price_location.write(f'現在のビットコイン価格: ¥{new_price}')
#             status_location.markdown(
#                f'<span style="color:green">オンライン</span>', 
#                unsafe_allow_html=True
#             )
#         else:
#             status_location.markdown(
#                f'<span style="color:red">APIエラー</span>', 
#                unsafe_allow_html=True
#             )

#         time_location.write(f'最終更新時刻: {current_time}')
#         print(
#             f'現在のビットコイン価格: ¥{new_price if new_price else "N/A"} - 更新時刻: {current_time} - ステータス: {new_status}'
#         )

# if __name__ == '__main__':
#     main()



# import streamlit as st
# import pandas as pd
# import numpy as np
# from datetime import datetime

# # サンプルデータの生成
# def create_sample_data():
#     date_range = pd.date_range(start='2020-01-01', end='2020-12-31', freq='D')
#     temperature_data = np.random.normal(loc=15, scale=5, size=(len(date_range),))
#     return pd.DataFrame({
#         'date': date_range,
#         'temperature': temperature_data
#     })

# # データの読み込み
# data = create_sample_data()

# # タイトル
# st.title('日付範囲に基づく気温データの視覚化')

# # ユーザー入力の取得
# # min_valueとmax_valueをdatetime.date型に変換
# start_date, end_date = st.slider(
#     "日付範囲を選択:",
#     min_value=data['date'].min().date(),
#     max_value=data['date'].max().date(),
#     value=(data['date'].min().date(), data['date'].max().date()),
#     format='YYYY-MM-DD'
# )

# # データのフィルタリング
# filtered_data = data[(data['date'].dt.date >= start_date) & (data['date'].dt.date <= end_date)]

# # グラフのプロット
# st.line_chart(filtered_data.rename(columns={'date': 'index'}).set_index('index'))



# import streamlit as st
# import requests
# import time
# from datetime import datetime
# import pandas as pd
# import plotly.express as px


# API_URL = "https://api.coin.z.com/public/v1/ticker?symbol=BTC_JPY"

# def get_bitcoin_price():
#     response = requests.get(API_URL)
#     if response.status_code == 200:
#         data = response.json()
#         return data['data'][0]['last'], 'online'
#     else:
#         return None, 'error'


# # DataFrameを初期化します。このDataFrameは価格とタイムスタンプを格納します。
# price_data = pd.DataFrame(columns=['Timestamp', 'Price'])

# def main():
#     st.title('ビットコイン価格トラッカー')

#     # 初期価格とステータスの取得
#     price, status = get_bitcoin_price()
#     price_location = st.empty()
#     time_location = st.empty()
#     status_location = st.empty()
#     graph_location = st.empty()

#     if status == 'online':
#         price_location.write(f'現在のビットコイン価格: ¥{price}')
#         status_location.markdown(f'<span style="color:green">オンライン</span>', unsafe_allow_html=True)
#         # 初期データポイントを追加
#         price_data.loc[len(price_data)] = [datetime.now(), price]
#     else:
#         status_location.markdown(f'<span style="color:red">APIエラー</span>', unsafe_allow_html=True)

#     time_location.write(f'最終更新時刻: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

#     # グラフを初期化して表示
#     fig = px.line(price_data, x='Timestamp', y='Price', title='ビットコイン価格トレンド')
#     graph_location.plotly_chart(fig)

#     # 指定された間隔で価格とステータスを更新
#     interval = st.sidebar.slider('更新間隔（秒）:', min_value=1, max_value=600, value=30)
#     while True:
#         time.sleep(interval)
#         new_price, new_status = get_bitcoin_price()
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         if new_status == 'online':
#             price_location.write(f'現在のビットコイン価格: ¥{new_price}')
#             status_location.markdown(f'<span style="color:green">オンライン</span>', unsafe_allow_html=True)
#             # 新しいデータポイントを追加
#             price_data.loc[len(price_data)] = [datetime.now(), new_price]
#         else:
#             status_location.markdown(f'<span style="color:red">APIエラー</span>', unsafe_allow_html=True)

#         time_location.write(f'最終更新時刻: {current_time}')
#         print(f'現在のビットコイン価格: ¥{new_price if new_price else "N/A"} - 更新時刻: {current_time} - ステータス: {new_status}')

#         # グラフを更新
#         fig = px.line(price_data, x='Timestamp', y='Price', title='ビットコイン価格トレンド')
#         graph_location.plotly_chart(fig)

# if __name__ == '__main__':
#     main()


import streamlit as st
import numpy as np
from joblib import load

# 保存された決定木モデルをロード
model = load(r"C:\Users\pc\Downloads\decision_tree_model.joblib")



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

