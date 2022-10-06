# 10/6  相似歌單推薦
  ### 檔案1: `recommend_songlist.py`
  ***** 輸入 “風格+編號“ 可以推薦相識歌單 （內建資料集）*****
  >1. 準備檔案 `allmusic3s.csv` 放到與程式碼同一個資料夾。
  >2. 終端機輸入指令 `python recommend_songlist.py allmusic3s.csv songname`  songname _ex: jazz5、pop30... 每個風格50首。_
  >3. 推薦表單。
 
  ### 檔案2: `recommend_songlist_2.py` 
  ***** 接續 url 模型，配合使用 *****
  >`url` youtube 連結。*不可從清單中複製連結會報錯！！！*
  >`file_name` 自定義。*執行三個檔案必須要一致*
  >1. 指令`python videodownload.py url file_name`    
  >2. 指令`python preprocessing.py file_name`     
  >3. 指令`python recommend_songlist_2.py file_name` 
  >4. 推薦表單。
  
  ### 檔案3: `allmusic3s.csv` 
  ***** 3秒資料集 *****
  >google 雲端連結
  https://drive.google.com/file/d/1K5ozXFQb5sxmN9hgr1ZkKlgxeZ1VjlfL/view?usp=sharing
  <br>
  <br>
  
***
