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

    # 1. 切换 iframe
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "g_iframe")))

    # 2. 等待歌曲模块加载出来
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "m-song-module")))

    # 3. 页面 HTML 解析
    soup = BeautifulSoup(driver.page_source, "lxml")

    ul = soup.find("ul", id="m-song-module")
    if not ul:
        print("❌ 依然没找到 m-song-module，可能页面结构变了")
    else:
        lis = ul.find_all("li")
        print("li count:", len(lis))

    for li in lis:
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