import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class AutoSearch:
    def __init__(self, t, p):
        focus_delays = 2
        click_delays = 4
        i = 0
        while i < t:
            #open browser and go to google.com
            browser = webdriver.Firefox()

            #browser.maximize_window()
            time.sleep(focus_delays)
            browser.get('http://www.google.com')

            #search a phrase
            search = browser.find_element_by_name('q')
            search.send_keys(p)
            search.send_keys(Keys.RETURN) # hit return after you enter search text

            print(p)

            hasgoogleplace = True
            try:
                #wait the page finish loading then find "More Place"
                element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_R4k")))
                element.send_keys(Keys.NULL)
                time.sleep(focus_delays)
                element.click()  # click the link
                time.sleep(click_delays)
            except TimeoutException:
                hasgoogleplace = False
                print("Has no More Places Button")

            in_map_not_found = False
            if hasgoogleplace:
                nextpage = False
                isClick = False
                while True:
                    if "NextArts" in browser.page_source:
                        try:
                            temp = WebDriverWait(browser, 10).until(
                                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "NextArts")))
                        except TimeoutException:
                            break
                        temp.send_keys(Keys.NULL)
                        time.sleep(focus_delays)
                        temp.click()
                        isClick = True
                        time.sleep(click_delays)
                        break
                    else:
                        try:
                            n = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Next")))
                        except TimeoutException:
                            in_map_not_found = True
                            print("not found in map")
                            break
                        nextpage = True
                        n.send_keys(Keys.NULL)
                        time.sleep(focus_delays)
                        n.click()
                        time.sleep(click_delays)

                if isClick:
                    try:
                        temp1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="_chp ab_button"]')))
                        temp1.click()
                        print("---found in Google map")
                    except TimeoutException:
                        print("cannot find nextarts link")
                        break

                if not in_map_not_found:
                    time.sleep(click_delays)
                    browser.back()
                    time.sleep(click_delays)
                    browser.back()
                time.sleep(click_delays)
                browser.back()
                time.sleep(click_delays)

                if nextpage:
                    browser.back()
                    time.sleep(click_delays)
            else:
                try:
                    gmap = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Website")))
                    gmap.send_keys(Keys.NULL)
                    time.sleep(focus_delays)
                    gmap.click()
                    print("---found in Google map")
                    time.sleep(click_delays)
                    browser.back()
                    time.sleep(click_delays)
                except TimeoutException:
                    print("not found in map")


            site1 = "NextArts.org"
            site2 = "Affordable Daily Large Flat Screen"

            #need to refresh the page to get page_source
            browser.refresh()
            page = 1
            # search result in organic result, click next page if cannot find
            while True:
                if site1 in browser.page_source:
                    print("found site 1")
                    try:
                        c = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, site1)))
                    except TimeoutException:
                        browser.quit()
                        break
                    c.send_keys(Keys.NULL)
                    time.sleep(focus_delays)
                    c.click()
                    print("---found in Organic at Page " + str(page))
                    time.sleep(click_delays)
                    break
                elif site2 in browser.page_source:
                    print("found site 2")
                    try:
                        c = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, site2)))
                    except TimeoutException:
                        browser.quit()
                        break
                    c.send_keys(Keys.NULL)
                    time.sleep(focus_delays)
                    c.click()
                    print("---found in Organic at Page " + str(page))
                    time.sleep(click_delays)
                    break
                else:
                    try:
                        n1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Next")))
                        page += 1

                    except TimeoutException:
                        print("not in organic")
                        browser.quit()
                        break
                    n1.send_keys(Keys.NULL)
                    time.sleep(focus_delays)
                    n1.click()
                    time.sleep(click_delays)
            browser.quit()
            print("---------------------------------------------------------------------")
            i += 1

phrases = ["wedding lighting san francisco bay area",
"Microphone rental san francisco",
"Wireless microphone rental san francisco",
"Microphone rental napa",
"Wireless microphone rental napa"
]
times = 1
for phrase in phrases:
    AutoSearch(times, phrase)


