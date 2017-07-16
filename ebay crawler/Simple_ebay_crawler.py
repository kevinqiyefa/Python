import xlsxwriter
import requests
from bs4 import BeautifulSoup



def scrape(max_pages):
    page = 1

    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('web_scrape.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 100)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Text with formatting.
    worksheet.write('A1', 'Ebay Item TD', bold)
    worksheet.write('B1', 'Item Price', bold)
    worksheet.write('C1', 'Item Title', bold)



    while page <= max_pages:
        url = "http://www.ebay.com/sch/i.html?_odkw=BOOT&_nkw=boot" #change url for future multiple page search
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        page += 1

        cl = 0
        rw = 1
        for item in soup.findAll("div", {"class": "mimg itmcd img"}):
            item_id = item.get("iid")
            item_title = item.select(".vip")[0].string
            item_price = item.select(".bold")[0].string

            # only print the item that has Buy It Now price
            if not item.select(".bid"):
                worksheet.write(rw, cl, item_id)
                cl += 1
                print(item_id)
                if not item.select(".prRange"):
                    worksheet.write(rw, cl, item_price.strip())
                    cl += 1
                    print(item_price.strip())
                else:
                    price_range = ""
                    for x in item.select(".bold")[0].contents:
                        price_range += str(x).replace('<span>', '').replace('</span>', '').strip()+ " "
                    worksheet.write(rw, cl, price_range)
                    print(price_range)
                    cl += 1
                worksheet.write(rw, cl, item_title)
                print(item_title)
                print()
                cl = 0
                rw += 1

    workbook.close()
scrape(1)



