# encoding = utf-8
__author__ = "Ang Li"


import xlrd
import re

wb_cmdb = xlrd.open_workbook('cmdb.xlsx')
wb_ip = xlrd.open_workbook('未在cmdb存活的服务器.xlsx')

# wb_cmdb = xlrd.open_workbook('cmdb - 副本.xlsx')
# wb_ip = xlrd.open_workbook('未在cmdb存活的服务器-test.xlsx')


ip_table = wb_ip.sheet_by_index(0)

# print(ip_table.nrows)    # 所有的行数

ip_list = [] # 所有的要检查的ip
for row in range(1, ip_table.nrows):
    ip_list.append(ip_table.cell_value(row, 0).strip())



print("已获取需要检索的IP。")


def slect_ip(ip):
    for x in range(0, 9):
        # sheet中共有多少行, 下面循环这些行,每行对比
        wlj_table = wb_cmdb.sheet_by_index(x)
        wlj_table_nows = wlj_table.nrows

        a = ""
        # 循环当前sheet的所有行
        for row in range(1, wlj_table_nows):    # row是行号

            # 循环当前行的所有类型的IP, i是列号
            for i in range(1, 5):
                # 获取cmdb单元格中的IP,可能是ip,外网ip,虚拟ip,idrac ip
                ip_now = wlj_table.cell_value(row, i).strip()
                # 先匹配这个单元格是否对上
                if ip == ip_now:
                    app_type = wlj_table.cell_value(row, 5).strip()
                    # ip类型,虚拟ip还是idrac ip登
                    ip_type = wlj_table.cell_value(1, 0) + wlj_table.cell_value(0, i).strip()
                    # ip, dsj, 应用系统, 为什么没在cmdb
                    a = [ip, 'DSJ', app_type, ip_type]
                    return a
                else:
                    # 如果匹配不上,检查是否有特殊字符,如果有
                    if re.search("(/)|(,)", ip_now):    # 如果对比的ip中没有特殊字符 10.159.3.3/10.159.3.4
                        if ip in re.split("(/)|(,)", ip_now):   # 用特殊字符将ip分成列表, 10.159.3.2/3 这种没有效果,多是虚拟ip

                            # 如果这个ip, 在这个列表里
                            # ip类型,虚拟ip还是idrac ip登
                            ip_type = wlj_table.cell_value(1, 0) + wlj_table.cell_value(0, i).strip()
                            app_type = wlj_table.cell_value(row, 5).strip()
                            # ip, dsj, 应用系统, 为什么没在cmdb
                            a = [ip, 'DSJ', app_type, ip_type]
                            return a
    if len(a) == 0:
        with open('not_in__wlj', 'a', encoding='utf-8') as f:
            f.write(ip)
            f.write('\n')
        return None



# 检测到的
count = 0
not_in = 0

with open('re.csv', 'a', encoding='utf-8') as c:
    for ip in ip_list:
        strs = ""
        print("开始检查~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ", ip)
        wlj_rs = slect_ip(ip)
        if wlj_rs:
            count += 1
            for w in wlj_rs:
                strs += w + ','
            c.write(strs)
            c.write('\n')
        else:
            not_in += 1

print("共检查了IP {} 个, 其中".format(len(ip_list)))
print("\t共检测到IP {} 个".format(count), "未检测到IP {}".format(not_in))



