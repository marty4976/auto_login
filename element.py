from selenium import webdriver  # Seleniumのwebdriverをインポート
from selenium.webdriver.chrome.options import Options  # Chromeのオプションをインポート
from selenium.webdriver.common.by import By  # 要素検索のためのByをインポート
from selenium.webdriver.remote.webdriver import WebDriver  # WebDriver型をインポート
from selenium.webdriver.support.ui import WebDriverWait  # 明示的な待機をインポート
from selenium.webdriver.support import expected_conditions as EC  # 待機条件をインポート

class LibecityLoginPage:
    def create_chrome(self) -> WebDriver: #クラスインスタンスから呼び出すchromeドライバーを作成する関数
        options = Options()  # Chromeの設定を作成
        driver = webdriver.Chrome(options=options)  # ChromeDriverを起動するoptions
        return driver  # driverを返す

    def login_page(self, driver: WebDriver):
        url = "https://libecity.com/login"  # ログインページのURLを指定
        driver.get(url)  # 指定URLにアクセス

    # メールアドレス入力欄に対応する要素を取得
    def input_email(self, driver: WebDriver):
        wait = WebDriverWait(driver, 10)  # 最大10秒待機するwaitを作成
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//input[@placeholder="メールアドレス"]')  # メールアドレス入力欄をXPathで指定
        ))
        return element  # 要素を返す

    # パスワード入力欄に対応する要素を取得
    def input_password(self, driver: WebDriver):
        wait = WebDriverWait(driver, 10)  # 最大10秒待機するwaitを作成
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//input[@placeholder="パスワード"]')  # パスワード入力欄をXPathで指定
        ))
        return element  # 要素を返す

    # ログインボタンに対応する要素を取得
    def login_button(self, driver: WebDriver):
        wait = WebDriverWait(driver, 10)  # 最大10秒待機する
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'ログイン')]")  # ログインボタンをXPathで指定
        ))
        return element  # 要素を返す

    # メールアドレスを入力
    def type_email(self, driver: WebDriver, email: str):
        field = self.get_email_input(driver)  # メールアドレス入力欄を取得
        field.send_keys(email)  # メールアドレスを入力

    # パスワードを入力
    def type_password(self, driver: WebDriver, password: str):
        field = self.get_password_input(driver)  # パスワード入力欄を取得
        field.send_keys(password)  # パスワードを入力

    # ログインボタンをクリック
    def press_login_button(self, driver: WebDriver):
        button = self.get_login_button(driver)  # ログインボタンを取得
        driver.execute_script("arguments[0].scrollIntoView(true);", button)  # ボタンを画面内にスクロール
        button.click()  # ログインボタンをクリック

# ダッシュボード操作用クラスの定義
class LibecityDashboardPage:
    # ユーザー名表示要素を取得
    def get_username_element(self, driver: WebDriver):
        wait = WebDriverWait(driver, 10)  # 最大10秒待機するwaitを作成
        element = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".user-name")  # ユーザー名表示要素をCSSセレクタで指定
        ))
        return element  # 要素を返す

    # ログイン後のユーザー名テキストを取得
    def get_logged_in_username(self, driver: WebDriver) -> str:
        element = self.get_username_element(driver)  # ユーザー名要素を取得
        username = element.text  # ユーザー名テキストを取得
        return username  # ユーザー名を返す
