import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class AutoSearch:

    def __init__(self, t, p):
        focus_delays = 1
        click_delays = 3
        i = 0

        while i < t:
            browser = webdriver.Firefox()

            self.open_google_and_search(p, focus_delays, browser)

            hasgoogleplace = self.click_more_place_button(focus_delays, click_delays, browser)

            in_map_not_found = False
            if hasgoogleplace:
                nextpage = False
                is_click = False
                while True:
                    part_text = "NextArts"
                    if part_text in browser.page_source:
                        self.click_part_text(focus_delays, click_delays, browser, part_text)
                        is_click = True
                        break
                    else:
                        in_map_not_found = self.search_next_page(focus_delays, click_delays, browser)
                        if in_map_not_found:
                            print("not found in map")
                            break
                        nextpage = True

                if is_click and not self.click_link_in_map(browser):
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
                self.only_one_in_map(focus_delays,click_delays,browser)


            site1 = "NextArts.org"
            site2 = "Affordable Daily Large Flat Screen"

            #need to refresh the page to get page_source
            browser.refresh()
            page = 1
            # search result in organic result, click next page if cannot find
            while True:
                if site1 in browser.page_source:
                    print("found site 1")

                    if not self.find_in_organic(focus_delays, click_delays, browser, site1, page):
                        print("cannot click site1 link")

                    break
                elif site2 in browser.page_source:
                    print("found site 2")

                    if not self.find_in_organic(focus_delays, click_delays, browser, site2, page):
                        print("cannot click site2 link")

                    break
                else:

                    if not self.search_next_page(focus_delays, click_delays, browser):
                        page += 1
                    else:
                        print("not in organic")
                        browser.quit()
                        break

            site3 = "BBB Business Profile | NextArts"
            if p == "NextArts":
                browser.back()
                time.sleep(click_delays)
                browser.refresh()

                while True:
                    if site3 in browser.page_source:
                        print("found BBB link")

                        if not self.find_in_organic(focus_delays, click_delays, browser, site3, page):
                            print("cannot click site3 link")
                        break
                    else:
                        if self.search_next_page(focus_delays, click_delays, browser):
                            print("no BBB in organic")
                            browser.quit()
                            break

            browser.quit()
            print("---------------------------------------------------------------------")
            i += 1

    def open_google_and_search(self, ph, fd, b):
        #b.maximize_window()
        time.sleep(fd)
        b.get('http://www.google.com')

        # search a phrase
        search = b.find_element_by_name('q')
        search.send_keys(ph)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text

        print(ph)

    def click_more_place_button(self, fd, cd, b):
        try:
            # wait the page finish loading then find "More Place"
            e = WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_R4k")))
            self.focus_and_click(e, fd, cd)
            return True
        except TimeoutException:
            print("no More Places button")
            return False

    def click_part_text(self, fd, cd, b, pl):
        try:
            temp = WebDriverWait(b, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, pl)))
        except TimeoutException:
            print("cannot find (" + pl + ") link")
            return
        self.focus_and_click(temp, fd, cd)

    def search_next_page(self, fd, cd, b):
        try:
            n = WebDriverWait(b, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Next")))
        except TimeoutException:
            return True
        self.focus_and_click(n, fd, cd)
        return False

    def click_link_in_map(self, b):
        try:
            temp1 = WebDriverWait(b, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="_chp ab_button"]')))
            temp1.click()
            print("---found in Google map")
            return True
        except TimeoutException:
            print("cannot find nextarts link")
            return False

    def only_one_in_map(self, fd, cd, b):
        try:
            gmap = WebDriverWait(b, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Website")))
            self.focus_and_click(gmap, fd, cd)
            print("---found in Google map")
            b.back()
            time.sleep(cd)
        except TimeoutException:
            print("not found in map")

    def find_in_organic(self, fd, cd, b, site, pages):
        try:
            c = WebDriverWait(b, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, site)))
        except TimeoutException:
            b.quit()
            return False
        self.focus_and_click(c, fd, cd)
        print("---found in Organic at Page " + str(pages))
        return True

    def focus_and_click(self, obj, fd, cd):
        obj.send_keys(Keys.NULL)
        time.sleep(fd)
        obj.click()  # click the link
        time.sleep(cd)


phrases = ["event lighting san francisco",
            "audio equipment rental napa",
            "audio equipment rental san francisco",
            "sound system rental san francisco",
            "event lighting napa",
            "lighting napa",
            "projector rental san francisco",
            "drapery rental san francisco bay area",
            "lighting san francisco",
            "large display rental san francisco",
            "lighting company san francisco",
            "av rental company san Francisco",
            "av rental company san Francisco bay area",
            "av rental company napa",
            "av rental company wine country",
            "wedding lighting san francisco bay area",
            "wedding lighting san francisco",
            "lighting san francisco",
            "lighting san francisco bay area",
            "pipe and drape rental san Francisco",
            "drape rental san Francisco",
            "pipe and drape rental san Francisco bay area",
            "drape rental san Francisco bay area",
            "lcd projector rental san Francisco",
            "lcd projector rental san Francisco bay area",
            "projector rental san Francisco",
            "projector rental san Francisco bay area",
            "audio visual rental san Francisco",
            "audio visual rental san Francisco bay area",
            "audio equipment rental san Francisco",
            "audio equipment rental san Francisco bay area",
            "audio visual equipment rental san francisco bay area",
            "big screen tv rental san francisco",
            "lighting san francisco",
            "audio visual company san Francisco",
            "audio visual company san Francisco bay area",
            "audio visual company napa",
            "audio visual company wine country",
            "sound system rental san francisco",
            "flat screen tv rental san francisco",
            "rent flat screen tv san francisco",
            "flat screen tv rental san francisco",
            "rent big screen tv for day san francisco",
            "Microphone rental san francisco",
            "Wireless microphone rental san francisco",
            "Microphone rental napa",
            "Wireless microphone rental napa",
            "NextArts"]
times = 1
for phrase in phrases:
    AutoSearch(times, phrase)


