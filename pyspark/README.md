# 10/13 更新
  ### 檔案1: `psMLtest_1005.ipynb` 
  ***** 可在 spark 虛擬機上 jupyter 執行計算訓練模型的時間 *****<br>
  ✨更新讀檔 hadoop HA路徑指令。
  >參考 10/5 步驟。
  
  ### 檔案2: `allmusic3s_new.csv`  
  ***** 只能使用這個.csv 訓練（或著已經去掉 index 的.csv） *****<br>
  ✨補載點。<br>
  >1. 上傳至hadoop 檔案系統<br>
  google 雲端載點： https://drive.google.com/file/d/1tUKuAGcezCkBqxkFaZC1vvC9fQpBB7KE/view?usp=sharing
  
  ### 檔案3: `allmusic3s_new_mltest.py` 
  ***** .py 的程式 *****<br>
  ✨更新讀檔 hadoop HA路徑指令。<br>
  ✨spark-submit local mode 測試OK。<br>
  
  >1. 在相同目錄下執行 `spark_submit allmusic3s_new_mltest.py`
  >2. 反註解 => 內容 `spark.csv(/tmp/allmusic3s_new.csv)` 使用hadoop HA
  >2. 反註解最後幾個註解，可選擇不同模型再測試。
  
  ***
<br>

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
 
  ### 檔案2: `allmusic3s_new.csv` 檔案太大沒有上傳github
  ***** 需要訓練的檔案  _※注意!!! 與目前的格式稍有不同_ *****
  >在合併資料時，匯出.csv 指令需要參數增加 index=False `pandas.to_csv(xxxx.csv, indext=False)`
  >來去掉第一個 index 欄位就沒問題，因為的一個欄位沒有名稱，再轉 `pyspark.sql.dataframe.DataFrame`會有錯誤。
  
  ### 檔案3: `allmusic3s_new_mltest.py` 
  ***** .py 的程式 *****
  > 目前只可以開 spark jupter lab `./pysparklab.sh` 在終端機執行 (待研究...)
  > 指令 `python3 allmusic3s_new_mltest.py` 即可執行。
***

# 10/4 
_psMLtest_1004.ipynb_ 測試過程

