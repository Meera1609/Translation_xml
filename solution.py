'''
step1 : read excel sheet content and have it in the format of
        lang = {'Host': 'ホスト','Host Timechart': 'ホストタイムチャート',....}
step2: open xml sheet,go over line by line,in each line search any key of the dict lang present - >
       ,replace it by dict(lang) value,save it as file1_jp.xml
libraries may be required:
xlrd,re,
'''
import xlrd
import io
import re
book = xlrd.open_workbook("jp_lookup.xls")
sheet = book.sheet_by_index(0)
total_rows = sheet.nrows
print(total_rows)
translation={}
i = 1
for i in range(0, 5):
    sheet.cell_x = sheet.cell(i, 0).value
    sheet.cell_y = sheet.cell(i, 1).value
    translation[sheet.cell_x] = sheet.cell_y
print(translation)
#for xml file1
# with io.open('file1_jp.xml','w',encoding="utf-8") as fe:
#  with io.open('file1.xml','r+',encoding="utf-8") as f:
#   lines = f.readlines()
#   for line in lines:
#     for i in translation.keys():
#         if i in line:
#             line = line.replace(i,translation[i])
#     fe.writelines(line)


# #op1 = re.search('>.*<',line)
# #print(op1)

#for xml file2
with io.open('file2_jp.xml','w',encoding="utf-8") as fd:
 with io.open('file2.xml','r+',encoding="utf-8") as d:
  lines = d.readlines()
  for line in lines:
    for i in translation.keys():
        if i in line:
            line = line.replace(i,translation[i])
    fd.writelines(line)





