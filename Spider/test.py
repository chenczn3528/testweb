from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)
driver.set_page_load_timeout(60)

try:
    driver.get("https://music.163.com/album?id=59888486&limit=1000")

    # 显式等待 iframe 出现
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe#g_iframe"))
    )

    iframe = driver.find_element(By.CSS_SELECTOR, "iframe#g_iframe")
    driver.switch_to.frame(iframe)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    # print(soup.prettify())
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

except Exception as e:
    print("iframe 加载失败:", e, flush=True)

finally:
    driver.quit()

# soup = BeautifulSoup(driver.page_source, "html.parser")
# albums = []
#
# for li in soup.select("ul#m-song-module li"):
#     print("li.text:", li.text)
#     print("li", li)
#     a_tag = li.select_one("a.msk")
#     if not a_tag:
#         continue
#     href = a_tag.get("href", "")
#     album_id = href.split("id=")[-1] if "id=" in href else None
#
#     title = li.select_one("p.dec a.tit")
#     if title:
#         album_title = title.text.strip()
#     else:
#         album_title = li.select_one("div.u-cover")["title"] if li.select_one("div.u-cover") else "未知专辑"
#
#     if album_id:
#         albums.append((album_id, album_title))
#         print(album_id, album_title)
#
# driver.quit()