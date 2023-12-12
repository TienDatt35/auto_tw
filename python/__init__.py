import time
import sys
sys.path.append("..")
from GPMLoginAPI import GPMLoginAPI
from selenium import webdriver
# python3 -m pip install --upgrade pip
# python3 -m pip
# pip install selenium
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options

# from UndetectChromeDriver import UndetectChromeDriver

apiUrl = 'http://127.0.0.1:15103/'
proxy = ["tin://suVbG4k7ZDJY7j6P79DajdGwvB9TQrkq:True","tin://5uqvUMfBYDu69Qo90MM4jweoLhSGY1J9:True","tin://oEH4MiLXGG73Ut97i7lBfIaiL0wyVaMZ:True","tin://zLIznEOlACSeDhT50Sywvf5iAVjKbJGM:True","tin://9JI8YDa1dKWH969inL71j1caA7KQulsk:True"]

def GetPro():
    api = GPMLoginAPI(apiUrl) # Alert: copy url api on GPM Login App

    #  Print list off profiles in GPMLogin -------------------------
    print('PROFILES ----------------------------')
    profiles = api.GetProfiles()
    if(profiles != None):
        for profile in profiles:
            id = profile['id']
            name = profile['name']
            print(f"Id: {id} | Name: {name}")

    # print('UPDATE PROXY------------------')
    # api.UpdateProxy(profiles[2], proxy[1])

    # print('START PROFILE ------------------')
    # startedResult = api.Start(profiles[2])
    # # startedResult = api.Start('e20e14ee-b825-4d36-8eb3-ccea61562aa4')
    # time.sleep(3)
    # chrome_options = Options()
    # chrome_options.add_argument("--lang=en-US")
    # chrome_options.add_experimental_option("debuggerAddress", startedResult["selenium_remote_debug_address"])

    # chrome_options.arguments.extend(["--no-default-browser-check", "--no-first-run"])

    # driver_path = startedResult["selenium_driver_location"]
    # # driver_path = "C:\\Users\\LEGION\\AppData\\Local\\Programs\\GPMLogin\\gpm_browser\\gpm_browser_chromium_core_107\\gpmdriver.exe"
    # print('driver_path: ', driver_path)
    # ser = service.Service(driver_path)
    # # driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    # driver = webdriver.Chrome(service=ser, options=chrome_options)
    # driver.get("https://whoer.net/")
    # input('Enter to close browser...')
    # driver.close()
    # driver.quit()

if __name__ == '__main__':
    GetPro()