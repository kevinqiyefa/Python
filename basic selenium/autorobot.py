import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import random


class AutoSearch:
    def __init__(self, t, p, br):
        print("<< Using " + br + " >>")
        focus_delays = 2
        click_delays = 7
        i = 0

        # optional loop for each keyword
        while i < t:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-infobars")            
            if br == "Firefox":
                browser = webdriver.Firefox()
            else:
                browser = webdriver.Chrome(chrome_options=chrome_options)
            self.open_google_and_search(p, focus_delays, browser)
            time.sleep(3)
            print("")
            if p != "NextArts":
                print("=======Search in Google Map=======")
                hasgoogleplace = self.click_more_place_button(focus_delays, click_delays, browser)

                in_map_not_found = False
                part_text = "NextArts"
                class_link = self.check_class_in_map_link(browser)

                if hasgoogleplace:
                    nextpage = False
                    is_click = False
                    while True:

                        map_class = self.check_class_in_map_link(browser)
                        find_no_ad_link = self.find_without_ad(browser, part_text, map_class)

                        if find_no_ad_link:
                            time.sleep(3)
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
                elif self.find_without_ad(browser, part_text, class_link):
                    # no moreplace button but in map result, and there are more than one result.
                    self.click_link_in_map(browser)
                    time.sleep(click_delays)
                    browser.back()
                    time.sleep(click_delays)
                    browser.back()
                    time.sleep(click_delays)
                else:
                    self.only_one_in_map(focus_delays, click_delays, browser)

            sites = ["NextArts.org | Audio, video, lighting",
                     "Affordable Daily Large Flat Screen",
                     "Drape | NextArts.org NextArts - Bay Area",
                     "Event Lighting | NextArts.org",
                     "Audio Visual Equipment Rentals - Bay Area", 
                     "Stanchions | NextArts.org NextArts"]

            # need to refresh the page to get page_source
            browser.refresh()
            time.sleep(click_delays)
            print("")
            print("=======Search in Oganic=======")
            page = 1
            print("Search in Page: " + str(page))
            # search result in organic result, click next page if cannot find
            if p != "NextArts":
                while True:

                    count_site = 0
                    foundsite = False

                    for site in sites:
                        if site in browser.page_source:
                            print("Found organic link: '" + site + "'")
                            foundsite = True
                            count_site += 1
                            if not self.click_in_organic(focus_delays, click_delays, browser, site, page):
                                print("cannot click the link")
                            time.sleep(click_delays)
                            browser.back()

                    if not foundsite and count_site == 0:
                        if (p == "lighting san francisco" or p == "lighting san francisco bay area") and page < 25:
                            page += 4
                        elif (p == "lighting company san francisco" or p == "lighting napa") and page < 6:
                            page += 5
                        # elif p == "lighting napa" and page < 10:
                        #    page += 9
                        else:
                            page += 1
                        pgs = str(page)
                        if self.search_next_page(focus_delays, click_delays, browser, pgs):
                            print("not in organic")
                            browser.quit()
                            break
                    else:
                        page += 1
                        if self.search_next_page(focus_delays, click_delays, browser, str(page)):
                            break
                        for site in sites:
                            if site in browser.page_source:
                                print("found link: '" + site + "'")
                                foundsite = True
                                count_site += 1
                                if not self.click_in_organic(focus_delays, click_delays, browser, site, page):
                                    print("cannot click the link")
                                time.sleep(click_delays)
                                browser.back()
                        break

            else:
                ending_site = ["BBB Business Profile | NextArts", "NextArts - Lighting",
                               "NextArts (San Francisco, CA):", "NextArts - San Francisco"]
                
                endlinks = my_shuffle(ending_site)
                time.sleep(focus_delays)
                
                while True:
                    found_end_site = False
                    
                    for el in endlinks:
                        if el in browser.page_source:
                            print("found ending link: '" + el + "'")
                            found_end_site = True
                            if not self.click_in_organic(focus_delays, click_delays, browser, el, page):
                                print("cannot click the link")
                            time.sleep(click_delays)
                            break
                    if found_end_site:
                        break
                    else:
                        print("No ending links in first page of organic")
                        browser.quit()
                        break


            browser.quit()
            print("")
            print("###########################################################################")
            print("")
            i += 1

    def open_google_and_search(self, ph, fd, b):
        # b.maximize_window()
        time.sleep(fd)
        b.get('http://www.google.com')

        # search a phrase
        search = b.find_element_by_name('q')
        search.send_keys(ph)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text

        print("Keywords: " + ph)

    def click_more_place_button(self, fd, cd, b):
        try:
            # wait the page finish loading then find "More Place"
            #e = WebDriverWait(b, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "_R4k")))
            e = WebDriverWait(b, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "DLOTif")))
            self.focus_and_click(e, fd, cd)
            return True
        except TimeoutException:
            print("no More Places button")
            return False

    def check_class_in_map_link(self, b):
        try:
            #temp = WebDriverWait(b, 1).until(
                #EC.presence_of_element_located((By.XPATH, "//*[contains(@class, '_iPk _Ml')]")))

            temp = WebDriverWait(b, 1).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'dbg0pd')]")))

            #return '_iPk _Ml'
            return 'dbg0pd'

        except TimeoutException:
            #return '_iPk'
            return 'dbg0pd'

    def find_without_ad(self, b, p, mc):

        #s = "//*[contains(@class, '_sEo') and .//*[contains(@class, '" + mc + "')] and .//div[contains(text(), '" + p + "')] and not(.//span[contains(@class, '_lLf')])]"

        s = "//*[contains(@class, 'cXedhc') and .//*[contains(@class, '" + mc + "')] and .//div[contains(text(), '" + p + "')] and not(.//span[contains(@class, 'gghBu')])]"

        try:
            t = WebDriverWait(b, 5).until(EC.presence_of_element_located((By.XPATH, s)))
            t.click()
            return True
        except TimeoutException:
            return False

    def click_part_text(self, fd, cd, b, pl):
        try:
            temp = WebDriverWait(b, 5).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, pl)))
        except TimeoutException:
            print("cannot find (" + pl + ") link")
            return
        self.focus_and_click(temp, fd, cd)

    def search_next_page(self, fd, cd, b, pg="Next"):
        try:
            n = WebDriverWait(b, 5).until(EC.presence_of_element_located((By.LINK_TEXT, pg)))
            print("***Clicked 'Next'***") if pg == "Next" else print(
                "___Clicked 'Next' and Searched Page: " + pg + "___")
        except TimeoutException:
            return True
        self.focus_and_click(n, fd, cd)
        return False

    def click_link_in_map(self, b):
        try:
            #tp1 = WebDriverWait(b, 5).until(
                #EC.presence_of_element_located((By.XPATH, '//*[@class="_chp ab_button"]')))
            tp1 = WebDriverWait(b, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="LJOFid ab_button"]')))
            time.sleep(5)
            tp1.click()
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Found in Google map <<<<<<<")
            return True
        except TimeoutException:
            print("cannot find nextarts link")
            return False

    def only_one_in_map(self, fd, cd, b):
        try:
            e1 = WebDriverWait(b, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_b1m kp-hc']")))
            WebDriverWait(e1, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'NextArts Audio')]")))
            click_link = WebDriverWait(e1, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Website")))
            self.focus_and_click(click_link, fd, cd)
            print("---found in Google map")
            b.back()
            time.sleep(cd)
        except TimeoutException:
            print("not found in map")

    def click_in_organic(self, fd, cd, b, site, pages):
        try:
            c = WebDriverWait(b, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, site)))
        except TimeoutException:
            b.quit()
            return False
        self.focus_and_click(c, fd, cd)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Clicked on Found link at Page " + str(pages) + "  <<<<<<<")
        return True

    def focus_and_click(self, obj, fd, cd):
        # chrome not support
        # obj.send_keys(Keys.NULL)
        time.sleep(fd)
        obj.click()  # click the link
        time.sleep(cd)



def my_shuffle(array):
    random.shuffle(array)
    return array

browswers = ["Firefox", "Chrome"]

keywords = ["event lighting San Francisco",
            "audio equipment rental Napa",
            "audio equipment rental San Francisco",
            "sound system rental San Francisco",
            "event lighting Napa",
            "lighting Napa",
            "projector rental San Francisco",
            "drapery rental San Francisco bay area",
            "lighting San Francisco",
            "large display rental San Francisco",
            "lighting company San Francisco",
            "av rental company San Francisco",
            "av rental company San Francisco bay area",
            "av rental company Napa",
            "av rental company wine country",
            "wedding lighting San Francisco bay area",
            "wedding lighting San Francisco",
            "lighting San Francisco",
            "lighting San Francisco bay area",
            "pipe and drape rental San Francisco",
            "drape rental San Francisco",
            "pipe and drape rental San Francisco bay area",
            "drape rental San Francisco bay area",
            "lcd projector rental San Francisco",
            "lcd projector rental San Francisco bay area",
            "projector rental San Francisco",
            "projector rental San Francisco bay area",
            "audio visual rental San Francisco",
            "audio visual rental San Francisco bay area",
            "audio equipment rental San Francisco",
            "audio equipment rental San Francisco bay area",
            "audio visual equipment rental San Francisco bay area",
            "big screen tv rental San Francisco",
            "audio visual company San Francisco",
            "audio visual company San Francisco bay area",
            "audio visual company Napa",
            "audio visual company wine country",
            "sound system rental San Francisco",
            "flat screen tv rental San Francisco",
            "rent flat screen tv San Francisco",
            "rent big screen tv for day San Francisco",
            "Microphone rental San Francisco",
            "Wireless microphone rental San Francisco",
            "Microphone rental Napa",
            "Wireless microphone rental Napa",
            "Red carpet rental San Francisco",
            "Red carpet rental Napa"]

ending_keyword = "NextArts"

times = 1
print("---------------------------------------------------------------------")
print("------------------------------Start----------------------------------")
print("---------------------------------------------------------------------")
print("###########################################################################")

new_keywords = my_shuffle(keywords)

for kw in new_keywords:
    AutoSearch(times, kw, random.choice(browswers))
AutoSearch(times, ending_keyword, random.choice(browswers))

print("---------------------------------------------------------------------")
print("------------------------------END------------------------------------")
print("---------------------------------------------------------------------")


