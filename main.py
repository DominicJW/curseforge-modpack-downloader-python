from selenium import webdriver
import time
import os
import json


chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory':"./mods_down",
'download.prompt_for_download':False,
'download.extensions_to_open':"application/java-archive",
'safebrowsing.enabled':True}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--safebrowsing-disable-download-protection")
chrome_options.add_argument("safebrowsing-disable-extension-blacklist")
##See https://stackoverflow.com/a/59841109


driver = webdriver.Chrome(chrome_options)


with open("manifest.json", "r") as json_file:
    manifest = json.load(json_file)
    
for j in manifest["files"]:
    url = f"https://www.curseforge.com/api/v1/mods/{j['projectID']}/files/{j['fileID']}/download"
    driver.get(url)
    time.sleep(1)


##Finish downloading any stragglers
while True:
    if any(filename.endswith(".crdownload") for filename in os.listdir("../../Downloads")):
        time.sleep(1)
    else:
        break

# Close the browser
driver.quit()
