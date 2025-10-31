from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

brave_path = "/usr/bin/brave-browser"  # adjust for your system

options = Options()
options.binary_location = brave_path
# Essential options only
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
# Consider removing other args for troubleshooting

service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")
input("Press enter to close")
driver.quit()