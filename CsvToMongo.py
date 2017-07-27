import pandas as pd
import json
import pymongo
class MongoDB:
  #连接到MongoDB数据库中
  def LinkDB(self,DBName):
      client = pymongo.MongoClient('192.168.47.128', 27017)
      db=client.DBName
      return db
  #使用DataFrame数据格式在MongoDB中创建相应的数据表
  def CreateDataTable(self,dbname,tableName,dataframe):
      db=self.LinkDB(dbname)
      db.tableName.insert(json.loads(dataframe.T.to_json()).values())
  #从MongoDB数据库中读取数据并转换为DataFrame格式
  def getData(self,dbname,tablename):
      db=self.LinkDB(dbname)
      da=pd.DataFrame.from_dict(db.tableName.find()[1],orient="index")
      for i in  db.tableName.find():
         da.append(pd.DataFrame.from_dict(i,orient="index"))
         da=pd.concat([da, pd.DataFrame.from_dict(i,orient="index")], axis=1)
      da.drop_duplicates
      print(da.T)