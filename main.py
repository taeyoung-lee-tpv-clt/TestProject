# from concurrent import futures
# from common.logging import logger
from namabiru.read_csv import get_df_data

file_path = './pricing.xlsx'
csv_path = './pricing.csv'

def serve():
    get_df_data(file_path,csv_path)

if __name__ == "__main__":
    print("Redis Server Start!")
    serve()
