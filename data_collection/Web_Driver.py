#File uses selenium webdriver to log into 'FollowMee.com' and download CSV for GPS and mobile speed data for the last 24 hours

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait

#Set up for web driver and setting download directory
chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = os.getcwd() +"\\chromedriver.exe"
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": "CSVs/",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

#Set up - find 'chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

#Open URL
driver.get("https://www.followmee.com/map.aspx")
driver.implicitly_wait(60) # seconds
print('found website')

#Log In
driver.find_element_by_id("ctl00_Main_Login1_UserName").send_keys("username")
driver.find_element_by_id ("ctl00_Main_Login1_Password").send_keys("password")
driver.find_element_by_id("ctl00_Main_Login1_LoginButton").click()
driver.implicitly_wait(60) # seconds
driver.get_screenshot_as_file("capture.png")
print('logged in')

#Map page and click download
driver.get("https://www.followmee.com/map.aspx")
driver.implicitly_wait(60) # seconds
download_button = driver.find_element_by_id('ctl00_Main_btnDownload')
downloadedfile = download_button.click()
driver.get_screenshot_as_file("capture2.png")
print('for download report')

#Select option 24 hours
driver.find_element_by_xpath("//select[@name = 'ctl00$Main$selPosLast']/option[text()='Last 24 Hours']").click()
driver.find_element_by_id("ctl00_Main_radCSV").click()

def enable_download_in_headless_chrome(driver, download_dir):
    # add missing support for chrome "send_command"  to selenium webdriver
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)

#Download into specified directory
enable_download_in_headless_chrome(driver, 'CSVs/')
print('download')

#Wait and close
driver.implicitly_wait(60) # seconds
driver.close()
