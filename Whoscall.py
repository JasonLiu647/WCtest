
from selenium import webdriver
import time


driver = webdriver.Chrome("/Users/jasonliu/Downloads/chromedriver-mac-arm64/chromedriver")
# 設定 Chrome 瀏覽器驅動程式
driver = webdriver.Chrome()

# 開啟 Pchome24h 網頁
driver.get("https://24h.pchome.com.tw/")

# 搜尋 Whoscall
driver.find_element(By.ID, "keyword").send_keys("Whoscall")
driver.find_element(By.CLASS_NAME, "btn-search").click()

# 進入 Whoscall 象卡來市話版 產品頁面
driver.find_element(By.LINK_TEXT, "Whoscall 象卡來市話版").click()

# 檢查價格是否為 1499
price = driver.find_element(By.CLASS_NAME, "p-price").text
if price != "1,499":
    raise Exception("價格不符預期")

# 截圖頁面下方紅框的 規格說明
time.sleep(2)  # 等待頁面完全載入
driver.save_screenshot("whoscall.png")

# 關閉瀏覽器
driver.close()