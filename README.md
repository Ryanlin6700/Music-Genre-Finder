## librosa_reference
>音檔匯入特徵函數測試，繪製頻譜、播放音檔等參考 jupyter notebook 呈現。
>
## model test
>機器學習模型試跑，用 `allmusic3s.csv` 資料集。

## pyspark
>1. 用 pysark 測試 sparkML 模型訓練速度測試，需要安裝spark jupter lab 上測試執行速度已叢集為準。<br>
>2. `allmusic3s_new_mltest.py` 需要再測試，在ubuntu執行讀取資料及路徑需要修改。

## recommend_songlist
>相似歌單推薦程式，用 `finalcsv3s.csv`資料集與 userupload csv 資料合併轉換，推薦資料集最相似 top5 的歌名、url。<br>
>✨ _需配合 videodownload 和 preprocessing 兩支.py程式執行。_
