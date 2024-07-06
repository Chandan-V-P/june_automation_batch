'''This file is created to practice String Methods
and created by Chandan on 27/06/2024'''

import pandas as pd
file = pd.read_csv("C:/Users/ichan/Downloads/machine-readable-business-employment-data-mar-2024-quarter.csv")
file_columns= file.columns

columns = ",".join(file_columns)
sql = f'''select {columns} from table_name;'''

print(sql)
