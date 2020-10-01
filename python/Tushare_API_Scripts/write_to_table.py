def write_to_table(df, table_name, if_exists='fail'):
    import io
    import pandas as pd
    from sqlalchemy import create_engine
    db_engine = create_engine('postgresql://***:***@***:***/***')# 初始化引擎
    string_data_io = io.StringIO()
    df.to_csv(string_data_io, sep='|', index=False)
    pd_sql_engine = pd.io.sql.pandasSQL_builder(db_engine)
    table = pd.io.sql.SQLTable(table_name, pd_sql_engine, frame=df,
                               index=False, if_exists=if_exists,schema = 'goods_code')
    table.create()
    string_data_io.seek(0)
    string_data_io.readline()  # remove header
    with db_engine.connect() as connection:
        with connection.connection.cursor() as cursor:
            copy_cmd = "COPY goods_code.%s FROM STDIN HEADER DELIMITER '|' CSV" %table_name
            cursor.copy_expert(copy_cmd, string_data_io)
