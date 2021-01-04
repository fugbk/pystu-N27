# encoding = utf-8
__author__ = "Ang Li"


# encoding = utf-8
__author__ = "Ang Li"


import xlrd

wb_cmdb = xlrd.open_workbook('cmdb.xlsx')
wb_ip = xlrd.open_workbook('未在cmdb存活的服务器.xlsx')


ip_table = wb_ip.sheet_by_index(0)

# print(ip_table.nrows)    # 所有的行数

ip_list = set() # 所有的要检查的ip
for row in range(1, ip_table.nrows):
    ip_list.add(ip_table.cell_value(row, 0).strip())


wlj_table = wb_cmdb.sheet_by_index(0)

ress = list()


wlj_table_nows = wlj_table.nrows

for ip in ip_list:
    for row in range(1, wlj_table_nows):
        if ip == wlj_table.cell_value(row, 1).strip():
            a = [ip, 'DSJ', wlj_table.cell_value(row, 5), f'{wlj_table.cell_value(1, 0)}内网IP']
        elif ip == wlj_table.cell_value(row, 2).strip():
            a = [ip, 'DSJ', wlj_table.cell_value(row, 5), f'{wlj_table.cell_value(1, 0)}外网IP，对应内网为{wlj_table.cell_value(row, 1).strip()}']
        elif ip == wlj_table.cell_value(row, 3).strip():
            a = [ip, 'DSJ', wlj_table.cell_value(row, 5), f'{wlj_table.cell_value(1, 0)}虚拟IP，对应内网为{wlj_table.cell_value(row, 1).strip()}']
        elif ip == wlj_table.cell_value(row, 4).strip():
            a = [ip, 'DSJ', wlj_table.cell_value(row, 5), f'{wlj_table.cell_value(1, 0)}idrac IP，对应内网为{wlj_table.cell_value(row, 1).strip()}']
        else:
            a = None
        if a:
            print(a)





