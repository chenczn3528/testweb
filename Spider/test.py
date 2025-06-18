from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
# driver.get("https://www.baidu.com")
# print(driver.title)
# driver.quit()



album_url = f"https://music.163.com/album?id=59888486&limit=1000"

driver.set_page_load_timeout(30)  # 最多等 30 秒加载页面
try:
    driver.get(album_url)
except Exception as e:
    print("页面加载失败:", e, flush=True)


try:
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "g_iframe")))
except Exception as e:
    print("iframe 加载失败:", e, flush=True)


soup = BeautifulSoup(driver.page_source, "html.parser")
albums = []

for li in soup.select("ul#m-song-module li"):
    print("li.text:", li.text)
    print("li", li)
    a_tag = li.select_one("a.msk")
    if not a_tag:
        continue
    href = a_tag.get("href", "")
    album_id = href.split("id=")[-1] if "id=" in href else None

    title = li.select_one("p.dec a.tit")
    if title:
        album_title = title.text.strip()
    else:
        album_title = li.select_one("div.u-cover")["title"] if li.select_one("div.u-cover") else "未知专辑"

    if album_id:
        albums.append((album_id, album_title))
        print(album_id, album_title)

driver.quit()