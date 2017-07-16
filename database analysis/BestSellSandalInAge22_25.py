import csv
from operator import itemgetter
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('bestSandalinGroupAge22_25.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 40)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
red = workbook.add_format({'font_color': 'red'})

# Text with formatting.
worksheet.write('A2', 'Item SKU', bold)
worksheet.write('B2', 'Total Sold In Group Age 22-25', bold)

with open('ORDER_DATABASE.txt') as f:
    c = csv.reader(f, delimiter='\t', skipinitialspace=True)

    x = 0
    newline = []
    p = []
    lines = []
    lines = [row for row in c]

while x < len(lines):
    # print(lines[x][8])
    if ("1992" in lines[x][8] or "1993" in lines[x][8]) \
            or ("1994" in lines[x][8] or "1995" in lines[x][8]):
        newline.insert(x, lines[x][2].split('-'))
        p.append(lines[x][3])
    x += 1

y = 0
while y < len(newline):
    newline[y].append(p[y])
    y += 1


def countp(i):
    name = i
    total = 0
    l = 0
    while l < len(newline):
        if name in newline[l]:
            total += int(newline[l][2])
        l += 1
    return total

nl = []
cp = []
a = 0

while a < len(newline):
    b = 0
    if not [newline[a][0]] in nl:
        nl.insert(a, [newline[a][0]])
        cp.insert(a, countp(newline[a][0]))

    a += 1


k = 0
while k < len(nl):
    nl[k].append(cp[k])
    k += 1

r = sorted(nl, key=itemgetter(1), reverse=True)
m = 0
while m < len(r):
    if m == 0:
        worksheet.write(m + 2, 0, str(r[m][0].strip("'")), red)
        worksheet.write(m + 2, 1, r[m][1], red)
    else:
        worksheet.write(m + 2, 0, str(r[m][0].strip("'")))
        worksheet.write(m + 2, 1, r[m][1])
    m += 1


workbook.close()