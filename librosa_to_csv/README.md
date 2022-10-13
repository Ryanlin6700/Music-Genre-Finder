# 10/13  優化改進 preprocessing.py  
### 檔案: `librosa_to_csv.py`
  ***** *****
  >1. 修改路徑結構 musicfile/<br>
    mp4/{file_name}/{file_name}.mp4<br> 
    wav/3s/{file_name}/{file_name}-{}-{}.wav&emsp;&emsp;csv/3s/{file_name}/{file_name}.csv<br>
    &emsp;&emsp;30s/{file_name}/{file_name}-{}.wav&emsp;&emsp;&emsp;&emsp;30s/{file_name}/{file_name}.csv 
  >2. 音檔分段改為，去頭 60s - 去尾 30s。
  >3. 選特徵：改 feature_dir 字典內容 選取需要轉出的特徵。
