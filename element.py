from selenium import webdriver  # Selenium の WebDriver 操作用
from selenium.webdriver.common.by import By  # 要素検索方法（ID, XPATH など）の定義
from selenium.webdriver.support.ui import WebDriverWait  # 明示的に待機を行うためのクラス
from selenium.webdriver.support import expected_conditions as EC  # 待機条件（要素が存在する、クリック可能など）
from selenium.webdriver.common.keys import Keys  # キーボード操作（Enter など）用

class LibecityPage:
    def create_chrome(self):
        options = webdriver.ChromeOptions()          # Chrome の起動オプションを設定するためのオブジェクトを生成
        return webdriver.Chrome(options=options)     # ヘッドレスなどオプションを指定して Chrome ブラウザを起動

    def open_login_page(self, driver, url: str) -> bool:
        try:
            driver.get(url)                          # 指定された URL をブラウザで開く
            return True                              # 成功したら True を返す
        except Exception:
            return False                             # 何か問題が起きたら False を返す

    def type_email(self, driver, email: str) -> bool:
        try:
            # メールアドレス入力欄がクリック可能になるまで、最大 10 秒間待つ
            email_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(           # 要素が画面上に表示され、かつクリック可能になるまで
                    (By.XPATH, '//*[@id="contents_wrap"]/main/div[1]/section/div[1]/p[2]/input')
                )
            )
            email_field.send_keys(email)             # メールアドレスを入力
            return True                              # 入力に成功したら True を返す
        except Exception:
            return False                             # 取得や入力時にエラーが起きたら False

    def type_password(self, driver, password: str) -> bool:
        try:
            # パスワード入力欄がクリック可能になるまで、最大 10 秒間待つ
            password_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="contents_wrap"]/main/div[1]/section/div[2]/p[2]/input[1]')
                )
            )
            password_field.send_keys(password)       # パスワードを入力
            password_field.send_keys(Keys.RETURN)    # Enter キーを送信してフォームを submit
            return True                              # 送信に成功したら True を返す
        except Exception:
            return False                             # 取得や送信時にエラーが起きたら False

    def wait_for_login(self, driver, timeout: int = 10) -> str | None:
        try:
            # ログイン後のユーザー名表示要素が現れるまで、最大 timeout 秒間待つ
            user_name_element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(       # 要素が DOM 上に存在するまで
                    (By.XPATH, '//*[@id="cw-menu"]/div[1]/div[1]/div[1]')
                )
            )
            return user_name_element.text           # 成功したら要素のテキスト（ユーザー名）を返す
        except Exception:
            return None                              # 見つからない場合やタイムアウト時は None を返す
