import os  # OS操作と環境変数取得に必要
from dotenv import load_dotenv  # .envファイルから環境変数を読み込む
from element import LibecityLoginPage  # ログイン・ダッシュボード要素操作クラスの読み込み
from chatwork import ChatworkImageSender  # チャットワーク通知クラスの読み込み
from logger import Logger  # ログを出力するライブラリの読み込み

class Flow:
    # .env からログインIDとパスワードを取得する
    def load_env(self):
        load_dotenv()  # .envファイルを読み込む
        email = os.getenv("LIVECITY_EMAIL")  # メールアドレスを取得
        password = os.getenv("LIVECITY_PASSWORD")  # パスワードを取得
        return email, password  # 2つの値を返す

    # ChromeDriver を起動する
    def create_chrome(self):
        login_page = LibecityLoginPage()  # ログインページ操作クラスのインスタンス化
        driver = login_page.create_driver()  # ドライバ生成メソッドの呼び出し
        return driver  # ドライバを返す

    # ログインページにアクセスする
    def access_login_page(self, driver):
        login_page = LibecityLoginPage()  # インスタンス化
        login_page.go_to_login(driver)  # ログインページに遷移

    # ログインIDの入力欄を探して入力する
    def input_email(self, driver, email):
        login_page = LibecityLoginPage()  # インスタンス化
        login_page.type_email(driver, email)  # メールアドレスを入力

    # パスワードの入力欄を探して入力する
    def input_password(self, driver, password):
        login_page = LibecityLoginPage()  # インスタンス化
        login_page.type_password(driver, password)  # パスワードを入力

    # ログインボタンを探してクリックする
    def click_login_button(self, driver):
        login_page = LibecityLoginPage()  # インスタンス化
        login_page.press_login_button(driver)  # ログインボタンをクリック

    # ログイン成功を URL で確認する
    def check_login(self, driver):
        result = "dashboard" in driver.current_url or "home" in driver.current_url  # 成功条件をチェック
        return result  # 判定結果を返す

    # ログイン後のユーザー名を取得する
    def get_username(self, driver):
        dashboard_page = LibecityDashboardPage()  # インスタンス化
        username = dashboard_page.get_logged_in_username(driver)  # ユーザー名を取得
        return username  # 取得したユーザー名を返す

    # チャットワークにメッセージを送信する
    def send_chatwork(self, message, logger):
        chatwork = ChatworkImageSender(  # チャットワーククラスを初期化
            api_token=os.getenv("CHATWORK_API_TOKEN"),  # APIトークンを.envから取得
            room_id=os.getenv("CHATWORK_ROOM_ID"),  # ルームIDを.envから取得
            logger=logger  # ロガーを渡す
        )
        result = chatwork.send_message(message)  # メッセージを送信
        print(f"Chatwork送信: {result}")  # 結果を表示

    # メインの処理をまとめて実行する
    def all_run(self):
        email, password = self.load_credentials()  # .envからID・パスワードを取得
        if not email or not password:  # どちらかが未設定の場合
            print("環境変数が設定されていません")  # エラー表示
            return  # 処理を終了

        logger = Logger()  # ロガーを生成
        driver = self.create_driver()  # Chromeドライバを起動

        try:
            self.access_login_page(driver)  # ログインページに移動
            self.input_email(driver, email)  # メールアドレスを入力
            self.input_password(driver, password)  # パスワードを入力
            self.click_login_button(driver)  # ログインボタンをクリック

            is_logged_in = self.check_login_success(driver)  # ログイン判定
            if is_logged_in:
                username = self.get_username(driver)  # ユーザー名を取得
                msg = f"✅ リベシティにログイン成功：{username}"  # 成功メッセージを作成
            else:
                msg = "⚠️ ログイン失敗：URLに dashboard または home が含まれていません"  # 失敗メッセージ
            print(msg)  # 結果を出力
            self.send_to_chatwork(msg, logger)  # チャットワークに通知

        except Exception as e:
            error_msg = f"❌ エラー発生：{str(e)}"  # 例外内容を文字列化
            print(error_msg)  # エラー表示
            self.send_to_chatwork(error_msg, logger)  # チャットワークにエラー通知

        finally:
            driver.quit()  # ブラウザを閉じる
            print("ブラウザを閉じました")  # 終了メッセージ


