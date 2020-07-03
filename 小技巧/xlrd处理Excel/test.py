# encoding = utf-8
__author__ = "mcabana.com"


import xlrd

excel_file = "test.xlsx"

# 打开一个工作簿
workbook = xlrd.open_workbook(excel_file)

# 打开工作表
worksheet = workbook.sheet_by_name('class 1')

# 接收关键字查询
name = input('Ple enter student name: ')
subject = input('Ple enter subject: ')

# 确定数据区域有效, 行数  列数
rows = worksheet.nrows  # 获取的是有效数据
cols = worksheet.ncols


# 获取学生列表, 科目列表。按行读取, 按列读取
names = worksheet.col_values(0)     # 学生姓名, 整列的数据, ---》列表
subjects = worksheet.row_values(0)  # 考试科目, 整行的数据, ---》列表


# 开始查询, 输入 姓名,科目
# 查询姓名所在的行号
if name in names:
    name_row = [names.index(name), ]
else:
    name_row = list(range(rows))

# 查询科目所在地列号
if subject in subjects:
    subject_col = [subjects.index(subject)]
else:
    subject_col = list(range(cols))

# 提取值
for row in name_row:
    for col in subject_col:
        value = worksheet.cell(row, col).value
        print(name, subject, value)