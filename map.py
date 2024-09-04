#%%
import plotly.express as px
import glob
import datetime
import os
import pandas as pd
# 設定起始日期
start_date = datetime.datetime(2021, 10, 29)

# 資料夾路徑模式
folder_pattern = "E:\\python\\論文程式\\SINS\\smartphone-decimeter-2022\\train\\20**MTV-1"
# 獲取所有匹配的資料夾
folders = glob.glob(folder_pattern)

# 過濾出日期大於等於2020-05-25的資料夾
filtered_folders = []
file_ground_truth_folders=[]
file_device_gnss_folders=[]
file_device_imu_folders=[]
for folder in folders:
    # 從資料夾名稱中提取日期
    folder_name = os.path.basename(folder)
    folder_date_str = folder_name[:10]  # 提取日期部分，假設資料夾格式為 YYYY-MM-DD...
    folder_date = datetime.datetime.strptime(folder_date_str, "%Y-%m-%d")
    
    # 比較日期
    if folder_date >= start_date:
        filtered_folders.append(folder)

# 打印符合條件的資料夾
for folder in filtered_folders:
    for file in glob.glob(f"{folder}/**/ground_truth.csv", recursive=True):
    # 檢查是否為檔案，因為 glob 也會返回目錄
        if os.path.isfile(file):
            file_ground_truth_folders.append(file)
    for file in glob.glob(f"{folder}/**/device_imu.csv", recursive=True):
    # 檢查是否為檔案，因為 glob 也會返回目錄
        if os.path.isfile(file):
            file_device_imu_folders.append(file)
    for file in glob.glob(f"{folder}/**/device_gnss.csv", recursive=True):
    # 檢查是否為檔案，因為 glob 也會返回目錄
        if os.path.isfile(file):
            file_device_gnss_folders.append(file)

len(file_ground_truth_folders)
for k in range(0, len(file_ground_truth_folders)):
    print(file_ground_truth_folders[k])
    fig = px.scatter_mapbox(pd.read_csv(file_ground_truth_folders[k]),

                            # Here, plotly gets, (x,y) coordinates
                            lat="LatitudeDegrees",
                            lon="LongitudeDegrees",
                                # labels="tripId",
                                # Here, plotly detects color of series


                            )
    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(title_text="GPS trafic")
    fig.show()

# %%
