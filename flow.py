import os  # OS操作と環境変数取得に必要
from dotenv import load_dotenv  # .envファイルから環境変数を読み込む
from element import LibecityPage, LibecityDashboardPage  # ログイン・ダッシュボード要素操作クラスの読み込み
from chatwork import ChatworkImageSender  # チャットワーク通知クラスの読み込み
from logger import Logger  # ログを出力するライブラリの読み込み

class LibecityFlow:
    def flow():
        load_dotenv()  # .envファイルから環境変数を読み込む
        print("環境変数を読み込みました。")
        print("LibecityFlowを開始します。")
        #choromeを起動するためのインスタンスを作成
        libecity_page = LibecityPage()
        #ログを出力するためのインスタンスを作成
        logger = Logger()
        #ログインページにアクセスする
        login_url = "https://libecity.com/sighnin"
        driver = libecity_page.create_chrome()
        libecity_page.login_page(driver, login_url)
        #ログインIDの入力欄を探す
        libecity_page.login_page(driver)
        #ログインIDを入力する
        email = os.getenv("LIBECITY_EMAIL")
        #パスワード入力欄を探す
        libecity_page.type_email(driver, email)
        #パスワードを入力する
        password = os.getenv("LIBECITY_PASSWORD")
        #ログインボタンを探す
        libecity_page.type_password(driver, password)
        #ログインボタンをクリックする
        libecity_page.press_login_button(driver)
        #ログイン成功を確認する
        dashboard_page = LibecityDashboardPage(driver)
        #チャットワークで送信する
        chatwork_api_token = os.getenv("CHATWORK_API_TOKEN")
        chatwork_room_id = os.getenv("CHATWORK_ROOM_ID")
        #ブラウザを閉じる
        driver.quit()




