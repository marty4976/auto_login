from selenium import webdriver  # Seleniumのwebdriverをインポート
from selenium.webdriver.chrome.options import Options  # Chromeのオプションをインポート
from selenium.webdriver.common.by import By  # 要素検索のためのByをインポート
from selenium.webdriver.remote.webdriver import WebDriver  # WebDriver型をインポート
from selenium.webdriver.support.ui import WebDriverWait  # 明示的な待機をインポート
from selenium.webdriver.support import expected_conditions as EC  # 待機条件をインポート

class LibecityPage:
    # Chromeドライバーを作成
    def create_chrome(self) -> WebDriver:
        options = Options()  # Chromeのオプションを作成
        driver = webdriver.Chrome(options=options)  # Chromeブラウザを起動
        return driver  # WebDriverインスタンスを返す

    # ログインページにアクセス
    def login_page(self, driver: WebDriver):
        driver.get(url)  # 引数で指定したURLにアクセス

    # メールアドレス入力欄を取得
    def get_email_input(self, driver: WebDriver):
        wait = WebDriverWait(driver, 10)  # 最大10秒待機するwaitを作成
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//input[@placeholder="メールアドレス"]')  # メールアドレス欄をXPATHで指定
        ))
        return element  # 要素を返す

    # パスワード入力欄を取得
    def get_password_input(self, driver: WebDriver):
        wait = WebDriverWait(driver, 10)  # 最大10秒待機するwaitを作成
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//input[@placeholder="パスワード"]')  # パスワード欄をXPATHで指定
        ))
        return element  # 要素を返す

    # ログインボタンを取得
    def get_login_button(self, driver: WebDriver):
        wait = WebDriverWait(driver, 10)  # 最大10秒待機するwaitを作成
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'ログイン')]")  # ログインボタンをXPATHで指定
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

class LibecityDashboardPage:
    # ログイン後のユーザー名テキストを取得
    def get_logged_in_username(self, driver: WebDriver) -> str:
        wait = WebDriverWait(driver, 10)  # 最大10秒待機するwaitを作成
        element = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".user-name")  # ユーザー名表示要素をCSSセレクタで指定
        ))
        return element.text  # ユーザー名テキストを返す
