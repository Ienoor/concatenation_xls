import glob
import pandas as pd

# Путь к папке с файлами
files_xls = glob.glob(r'*.xls')

df = pd.DataFrame()

for f in files_xls:
    data = pd.read_excel(f, 'Лист1')
    df = df.append(data)


# Путь к папке с результатом файлами
df.to_excel(r'')
