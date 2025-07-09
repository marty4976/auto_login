
import os  # OS 操作用（環境変数取得など）
from dotenv import load_dotenv  # .env ファイル読み込み用
from selenium.webdriver.common.by import By  # 要素検索方法指定用
from selenium.webdriver.support.ui import WebDriverWait  # 明示的待機用
from selenium.webdriver.support import expected_conditions as EC  # 待機条件指定用
from element import LibecityPage  # ページ操作をまとめたクラス
from logger import Logger  # ログ出力用

class LibecityFlow:
    def flow(self):
        load_dotenv()  # .env を読み込んで環境変数に反映

        libecity_page = LibecityPage()  # ページ操作ヘルパーを生成
        logger = Logger()  # ログ出力インスタンスを生成

        # Chrome を起動してログイン画面へ遷移
        login_url = "https://libecity.com/signin"
        driver = libecity_page.create_chrome()  # ヘッドレス Chrome を生成
        libecity_page.open_login_page(driver, login_url)  # URL を開く

        # 環境変数からメールアドレスとパスワードを取得
        email = os.getenv("LIBECITY_EMAIL")
        password = os.getenv("LIBECITY_PASSWORD")
        if not email or not password:  # 取得できなければ終了
            driver.quit()
            return None

        # フォームへの入力処理
        if not libecity_page.type_email(driver, email):  # メールアドレス入力
            driver.quit()
            return None
        if not libecity_page.type_password(driver, password):  # パスワード入力＆Enter送信
            driver.quit()
            return None

        # ログイン後のユーザー名を取得して存在を確認
        try:
            user_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="cw-menu"]/div[1]/div[1]/div[1]')  # ユーザー名要素の XPATH
                )
            )
            username = user_elem.text  # テキスト（ユーザー名）を取得
        except Exception:
            username = None  # 取得に失敗したら None

        driver.quit()  # ブラウザを閉じる
        return username  # 成功時はユーザー名、失敗時は None を返す
