# 広告データの集計スクリプト
import pandas as pd

# CSVファイルを読み込む（書き込みは行わない）
df = pd.read_csv("ad_data.csv")

# 媒体ごとにコストとコンバージョンを合計する
summary = df.groupby("媒体").agg(
    コスト合計=("コスト", "sum"),
    コンバージョン合計=("コンバージョン", "sum"),
)

# CPA（コスト合計 ÷ コンバージョン合計）を計算する
summary["CPA"] = summary["コスト合計"] / summary["コンバージョン合計"]

# 集計結果を画面に表示する
print(summary)
