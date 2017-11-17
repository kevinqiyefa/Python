import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class AutoSearch:
    def __init__(self, t, p):
        focus_delays = 3
        click_delays = 5
        i = 0
        while i < t:
            #open browser and go to google.com
            browser = webdriver.Firefox()

            browser.maximize_window()
            time.sleep(focus_delays)
            browser.get('http://www.google.com')

            #search a phrase
            search = browser.find_element_by_name('q')
            search.send_keys(p)
            search.send_keys(Keys.RETURN) # hit return after you enter search text

            try:
                #wait the page finish loading then find "More Place"
                element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_R4k")))
                element.send_keys(Keys.NULL)
                time.sleep(focus_delays)
            except TimeoutException:
                browser.quit()
                break
            element.click() #click the link

            time.sleep(click_delays)
            nextpage = False
            while True:
                if "NextArts Audio Visual" in browser.page_source:
                    try:
                        temp = WebDriverWait(browser, 10).until(
                            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "NextArts Audio")))
                        temp.send_keys(Keys.NULL)
                        time.sleep(focus_delays)
                    except TimeoutException:
                        browser.quit()
                        break
                    temp.click()
                    time.sleep(click_delays)
                    break
                else:
                    try:
                        n = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Next")))
                    except TimeoutException:
                        browser.quit()
                        break
                    nextpage = True
                    n.send_keys(Keys.NULL)
                    time.sleep(focus_delays)
                    n.click()
                    time.sleep(click_delays)

            try:
                temp1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="_chp ab_button"]')))
            except TimeoutException:
                browser.quit()
                break
            temp1.click()
            time.sleep(click_delays)
            browser.back() #go back to the privious page
            time.sleep(click_delays)
            browser.back()
            time.sleep(click_delays)
            browser.back()
            time.sleep(click_delays)

            if nextpage:
                browser.back()
                time.sleep(10)

            result = "NextArts.org | Audio, video, lighting, party rentals - Bay Area (415) 970 ..."

            # search result in organic result, click next page if cannot find
            while True:
                if result in browser.page_source:
                    try:
                        c = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, result)))
                    except TimeoutException:
                        browser.quit()
                        break
                    c.send_keys(Keys.NULL)
                    time.sleep(focus_delays)
                    c.click()
                    time.sleep(click_delays)
                    break
                else:
                    try:
                        n1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Next")))
                    except TimeoutException:
                        browser.quit()
                        break
                    n1.send_keys(Keys.NULL)
                    time.sleep(focus_delays)
                    n1.click()
                    time.sleep(click_delays)
            browser.quit()
            i += 1

phrases = ["audio visual rental san francisco",
           "event lighting san francisco"]
times = 1
for phrase in phrases:
    AutoSearch(times, phrase)


