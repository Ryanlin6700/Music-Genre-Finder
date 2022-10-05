# 10/5  
  ### 檔案1: `psMLtest_1005.ipynb`
  ***** 可在 spark 虛擬機上 jupyter 執行計算訓練模型的時間 *****
  >1. 準備檔案 `allmusic3s_new.csv`, `psMLtest_1005.ipynb` 上傳兩個檔案到 /sparkcodes -> 改權限
  >2. 登入spark主機，切換 sparksa 使用者 `su -i sparksa`
  >3. 到目錄下 `/etc/local/saprk/` or `cd $SPARK_HOME`
  >4. 開啟 spark jupter lab `./pysparklab.sh`
  >5. 執行即可。
  >※內容可以選擇執行叢集或單幾版運算，另外要使用 Hdfs 要先上傳`allmusic3s_new.csv` 到Hadoop 分散式系統
  >在補上load file `hdfs://bdse120.example.com/tmp`程式碼
 
  ### 檔案2: `allmusic3s_new.csv`
  ***** 需要訓練的檔案  _※注意!!! 與目前的格式稍有不同_ *****
  >在合併資料時，匯出.csv 指令參數增加 index=False `pandas.to_csv(xxxx.csv, indext=False)`
  >去掉第一個 index 欄位，因為的一個欄位沒有名稱，再轉 `pyspark.sql.dataframe.DataFrame`會有錯誤。
  
  ### 檔案3: `allmusic3s_new_mltest.py` 檔案太大沒有上傳github
  ***** .py 的程式 *****
  > 目前只可以開 spark jupter lab `./pysparklab.sh` 在終端機執行 (待研究...)
  > 指令 `python3 allmusic3s_new_mltest.py` 即可執行。
  <br>
  <br>
  
***

# 10/4 
_psMLtest_1004.ipynb_ 測試過程

