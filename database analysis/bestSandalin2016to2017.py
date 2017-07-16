from operator import itemgetter
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('bestSandal-late2016-early2017.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 40)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
red = workbook.add_format({'font_color': 'red'})

# Text with formatting.
worksheet.write('A2', 'Item SKU', bold)
worksheet.write('B2', 'Total Sold Between Oct 2016 - Jan 2017', bold)

with open('ORDER_DATABASE.txt') as f:
    lines = [line.split() for line in f]
    title = lines[0]
    # lines.sort(key=lambda x: x[0])
    x = 1
    newline = []
    p = []
    while x < len(lines):
        lines[x][1:4] = [' '.join(lines[x][1:4]).strip('"')]
        if ("October" in lines[x][1] and "2016" in lines[x][1]) \
                or ("November" in lines[x][1] and "2016" in lines[x][1]) \
                or ("December" in lines[x][1] and "2016" in lines[x][1]) \
                or ("January" in lines[x][1] and "2017" in lines[x][1]):

            newline.insert(x-1, lines[x][2].split('-'))
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

#print(countp('SANDAL303'))

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