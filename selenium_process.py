# selenium_process.py
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


# ---- logger ----
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


class ChromeDriverManager:
    """ChromeDriver を管理するクラス"""

    @staticmethod
    def chrome_option(size: str = "1200,900") -> Options:
        """ウィンドウサイズを設定した Chrome オプションを返す"""
        opts = Options()
        opts.add_argument(f"--window-size={size}")
        return opts

    @staticmethod
    def chrome_process(options: Options | None = None) -> webdriver.Chrome:
        """ChromeDriver を生成して返す"""
        try:
            opts = options or ChromeDriverManager.chrome_option()
            driver = webdriver.Chrome(options=opts)  # Selenium Manager がパス解決
            logger.info("ChromeDriver を起動しました。")
            return driver
        except WebDriverException as e:
            logger.error(f"ChromeDriver の起動に失敗: {e}")
            raise
        except Exception as e:
            logger.error(f"想定外のエラー: {e}")
            raise


if __name__ == "__main__":
    TEST_URL = "https://libecity.com/"
    driver = None
    try:
        driver = ChromeDriverManager.chrome_process()
        driver.get(TEST_URL)
        logger.info(f"遷移先: {driver.current_url}")
        time.sleep(5)  # ページ確認用
        logger.info(f"タイトル: {driver.title}")
    finally:
        if driver:
            driver.quit()
            logger.info("ChromeDriver を終了しました。")
