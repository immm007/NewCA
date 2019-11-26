import os
import pandas as pd


def generate(year, batch):
    data_path = 'D:\\NewCA\\{0}.xls'.format(year)
    folder_path = 'D:\\NewCA\\CA\\{0}\{1}'.format(year, batch)
    df = pd.read_excel(data_path)
    df = df.set_index('验收编号',drop=False)
    years = []
    numbers = []
    for name in os.listdir(folder_path):
        year = int(name[5:9])
        number = int(name[10:-6])
        years.append(year)
        numbers.append(number)
    drop_nums = []
    for num in df.index:
        if num not in numbers:
            drop_nums.append(num)
    df = df.drop(index = drop_nums)
    drop_nums = []
    for i in range(len(years)):
        num = numbers[i]
        year = years[i]
        result = df.loc[num]
        if type(result) == type(df):
            result = result.set_index('验收年份')
            for y in result.index:
                if y != year:
                    drop_nums.append(result.loc[y]['序号'])
    df = df.set_index('序号')
    df = df.drop(index = drop_nums)   
    return df

df1 = generate('2016','2019.11')
df2 = generate('2017','2019.11')