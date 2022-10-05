# 10/5  
  ### 檔案1: `psMLtest_1005.ipynb`
  **** 可在 spark 虛擬機上 jupyter 執行計算訓練模型的時間 ****
  >1. 準備檔案 `allmusic3s_new_mltest.py`, `psMLtest_1005.ipynb` 上傳兩個檔案到 /sparkcodes -> 改權限
  >2. 登入spark主機，切換 sparksa 使用者 `su -i sparksa`
  >3. 到目錄下 `/etc/local/saprk/` or `cd $SPARK_HOME`
  >4. 開啟 spark jupter lab `./pysparklab.sh`
  >5. 執行即可。
 
  ### 檔案2: `allmusic3s_new_mltest.py`
  **** 需要訓練的檔案  _※注意!!! 與目前的格式稍有不同_ ****
  >在合併資料時，匯出.csv 指令參數增加 index=False `pandas.to_csv(xxxx.csv, indext=False)`
  >去掉第一個 index 欄位因為的一個欄位沒有名稱，再轉 `pyspark.sql.dataframe.DataFrame`會有錯誤。
  
***
## 10/4 
file: psMLtest_1004.ipynb

