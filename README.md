下載整個Datasets到本地端，或是在kaggle Code執行
https://www.kaggle.com/competitions/smartphone-decimeter-2022<br>
1. 導入必要的模組

<pre><code>import plotly.express as px
import glob
import datetime
import os
import pandas as pd</code></pre>

2. 設定起始日期

<pre><code>start_date = datetime.datetime(2021, 10, 29)</code></pre>

3. 定義資料夾路徑模式

<pre><code>folder_pattern = "/kaggle/input/smartphone-decimeter-2022/train/20**MTV-1"</code></pre>

4. 獲取所有匹配的資料夾

<pre><code>folders = glob.glob(folder_pattern)</code></pre>
<br>
5. 過濾出日期大於等於 2021-10-29 的資料夾

<pre><code>filtered_folders = []
for folder in folders:
    folder_name = os.path.basename(folder)
    folder_date_str = folder_name[:10]
    folder_date = datetime.datetime.strptime(folder_date_str, "%Y-%m-%d")
    
    if folder_date >= start_date:
        filtered_folders.append(folder)</code></pre>
<br>
6. 獲取篩選後資料夾中的 ground_truth.csv 文件

<pre><code>file_ground_truth_folders=[]
for folder in filtered_folders:
    for file in glob.glob(f"{folder}/**/ground_truth.csv", recursive=True):
        if os.path.isfile(file):
            file_ground_truth_folders.append(file)</code></pre>
<br>
7. 繪製地圖

<pre><code>for k in range(0, len(file_ground_truth_folders)):
    fig = px.scatter_mapbox(pd.read_csv(file_ground_truth_folders[k]),
                            lat="LatitudeDegrees",
                            lon="LongitudeDegrees")
    fig.update_layout(mapbox_style='open-street-map')</code></pre>
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(title_text="GPS trafic")
    fig.show()
<br>

![map](https://github.com/user-attachments/assets/df7ab21e-3a43-46c5-8c2a-2adbd1121b11)
