from turtle import down
from flask import Flask, render_template, request, url_for
from flask_moment import Moment
from pathlib import Path
import uuid
# import sys 
import pandas as pd
import recognition.videodownload_w as download
import recognition.librosa_to_csv_w as librosa_to_csv
import recognition.recommend_songlist_userA_w as recommend
import recognition.load_model_w as model

# 需先在music-main/static/musicfile/下建立mp4、wav兩個資料夾 
app = Flask(__name__)
moment = Moment(app)

UPLOAD_FOLDER = Path(__file__).resolve().parent/'static/musicfile/mp4'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# get: 使用者輸入url
# post: 獲取url、下載、分析
@app.route('/', methods=['GET', 'POST'])
def get_url():
    # 使用者輸入url
    if request.method == "GET":
        return render_template('file.html', page_header="UPLOAD MUSIC")
    elif request.method == "POST":
        # 獲取url
        text = request.form['url']
        filename = str(uuid.uuid4())
        print(filename)
        # 下載mp4
        download.download(text,filename)

        # preprocessing
        librosa_to_csv.Video_to_csv(filename)

        # analysis
        result_df = model.predict_ans(filename)
        df = pd.DataFrame(result_df)
        result_list = df.values.tolist()
        
        #simlar song list
        result = recommend.find_similar_songs(filename)
        print(result)

        return result_list


if __name__ == "__main__":
    app.run(debug=True)
