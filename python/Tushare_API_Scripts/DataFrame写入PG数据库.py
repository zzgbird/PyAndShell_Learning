# DataFrame写入PG数据库

# 提前创建df数据集并安装psycopg2模块
pip install psycopg2

# 1. 使用pandas的to_sql导入
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:ican00@127.0.0.1:5432/stockam')
 
start = datetime.datetime.now() 


pd.io.sql.to_sql(df, 'stock_basic', engine,index= False, schema='ods',if_exists='append')

# fail 如果表存在，啥也不做
# replace 如果表存在，删了表，再建立一个新表，把数据插入
# append 如果表存在，把数据插入，如果表不存在创建一个表！！

end = datetime.datetime.now()
 
print('time cost:',(end - start))


# 2.使用copy_from导入 这种方式直接用了psycopg2模块中的copy_from方法，写入速度最快。
# dataframe类型转换为IO缓冲区中的str类型
# 需要先建表并指定插入列名
import psycopg2
from io import StringIO

df = pro.query('namechange',)

output = StringIO()
df.to_csv(output, sep='\t', index=False, header=False)
output1 = output.getvalue()

#conn = pgconnection()
conn = psycopg2.connect(database="stockam", user="postgres", password="ican00", host="127.0.0.1", port="5432") 

cur = conn.cursor()
# columns=['label1', 'label2']
cur.copy_from(StringIO(output1),'ods.namechange',)
 
conn.commit()

cur.close()
conn.close()


# 3. executemany()方法批量输入数据到数据库
import psycopg2
    
conn = psycopg2.connect(host=***, port=***, database=***, user=***, password=***)
cur = conn.cursor()
sql =  "insert into " + table_name + " values(%s, %s, %s)"
cur.executemany(sql, data)
conn.commit()
conn.close()


# 强大的copy_from()，是postgresSQ的内置函数
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import StringIO
from io import BytesIO
 
data1 = pd.DataFrame(data)
# dataframe类型转换为IO缓冲区中的str类型
output = BytesIO()
data1.to_csv(output, sep='\t', index=False, header=False)
output1 = output.getvalue()
   
conn = psycopg2.connect(host=***, user=***, password=***, database=***)
cur = conn.cursor()
cur.copy_from(StringIO.StringIO(output1), table_name1, null='',columns=columns)
conn.commit()
cur.close()
conn.close()
print('done')
这儿需要特别记录下，copy_from