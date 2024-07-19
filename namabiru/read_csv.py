from xlsx2csv import Xlsx2csv
import pandas as pd
from redisss.redis_server.redisServer import redis_server_main



# xlsx 파일을 csv 파일로 변환



def get_df_data(file_path, csv_path):
    csv_way = Xlsx2csv(file_path, outputencoding="utf-8").convert(csv_path)
    # pandas로 csv 파일 읽기
    df = pd.read_csv(csv_path)[2:]
    selected = ['E2E_UID', 'Ocean_Priority', 'Trade', 'Sub_Trade', 'Service_Lane', 'Cargo_Cutoff_Time']
    # selected = ['E2E UID','Ocean Priority','Trade','Sub Trade','Service Lane','Cargo Cutoff Time']
    df = df.rename(columns={
        'E2E UID': 'E2E_UID',
        'Ocean Priority': 'Ocean_Priority',
        'Sub Trade': 'Sub_Trade',
        'Service Lane': 'Service_Lane',
        'Cargo Cutoff Time': 'Cargo_Cutoff_Time'
    })
    new_df = df[selected]


    chunk_size = 10
    for start in range(0, len(new_df),chunk_size):
        chunk = df[start:start + chunk_size]
        data = {}
        for idx, row in new_df.iterrows():
            key = row['E2E_UID']
            values = row[['Ocean_Priority','Trade', 'Sub_Trade','Service_Lane','Cargo_Cutoff_Time']]
            data[key] = values
        redis_server_main(data)
    
    
    # print(key_value_pairs.keys)
    return new_df


