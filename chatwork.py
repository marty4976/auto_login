import requests
from typing import Optional
from logger import Logger

class ChatworkImageSender:
    def __init__(self, *, api_token: str, room_id: str, logger: Logger) -> None:
        self.api_token = api_token
        self.room_id = room_id
        self.logger = logger
        self.base_url = "https://api.chatwork.com/v2"

    def upload_file(self, *, file_path: str, message: Optional[str] = None) -> Optional[str]:
        url = f"{self.base_url}/rooms/{self.room_id}/files"
        headers = {
            "X-ChatWorkToken": self.api_token,
        }

        try:
            with open(file_path, "rb") as f:
                files = {"file": (file_path, f)}
                data = {"message": message} if message else {}
                response = requests.post(url, headers=headers, files=files, data=data)

            if response.status_code == 200:
                self.logger.info(message="ファイル送信に成功しました。")
                return response.json().get("file_id")
            else:
                self.logger.error(message=f"送信失敗：{response.status_code} - {response.text}")
                return None
        except Exception as e:
            self.logger.error(message=f"ファイル送信中にエラーが発生しました: {e}")
            return None
        
    def send_message(self, message: str) -> bool:
        url = f"{self.base_url}/rooms/{self.room_id}/messages"
        headers = {
            "X-ChatWorkToken": self.api_token,
        }
        data = {"body": message}
        try:
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                self.logger.info("メッセージ送信に成功しました。")
                return True
            else:
                self.logger.error(f"メッセージ送信失敗：{response.status_code} - {response.text}")
                return False
        except Exception as e:
            self.logger.error(f"メッセージ送信中にエラーが発生しました: {e}")
            return False