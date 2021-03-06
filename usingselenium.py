import os
import contextlib
import selenium.webdriver as webdriver
import csv
import time

url = "https://www.quora.com/Arpit-Jain-11/followers"
download_dir = '/tmp'
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.dir", download_dir)

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)



with contextlib.closing(webdriver.Firefox(firefox_profile=fp)) as driver:
    driver.get(url)
    driver.execute_script("onDownload(2);")
    csvfile = os.path.join(download_dir, 'download.csv')

    time.sleep(10)
    with open(csvfile, 'rb') as f:
        for line in csv.reader(f, delimiter=','):
            print(line)
