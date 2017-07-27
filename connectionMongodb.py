from CsvToMongo import MongoDB
import pandas as pd
da=MongoDB()
dataframe = pd.read_csv(r'F:\项目\大数据\数据\路面机械数据\1.csv', encoding='gbk')
da.CreateDataTable("test","test",dataframe)
print('succeed')
# da.getData("test","test")

