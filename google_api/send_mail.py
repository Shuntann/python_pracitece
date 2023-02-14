from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import base64
import mimetypes
import receive_mail

def message_base64_encode(message):
    return base64.urlsafe_b64encode(message.as_bytes()).decode()

def attach_file(message,file_path,file_name):
    content_type, encoding =mimetypes.guess_type(file_path)
    main_type, sub_type = content_type.split("/",1)
    f = open(file_path, "rb")
    message_file = MIMEBase(main_type,sub_type)
    message_file.set_payload(f.read())
    message_file.add_header("Contet-Disposition", "attachment", file_name = file_name)
    encoders.encode_base64(message_file)
    f.close()
    message.attach(message_file)

    return message


def main(address):
    scopes = ["https//mail.google.com/"]
    creds = Credentials.from_authorized_user_file("token.json", scopes)
    service = build("gmail", "v1", credentials=creds)

    message = MIMEText("ご購入ありがとうございます\n只今発送の準備中です。しばらくお待ちください。")
    message["From"] = "programming.zebra@gmail.com"
    message["To"] = address
    message["Subject"] = "auto_send_mail"

    raw = {"raw": message_base64_encode(message)}
    service.users().messages().send(
        userId = "me",
        body = raw
    ).execute()


if __name__=="__main__":

    address_list = []
    address_number = int(input("送信したいメアドの数: "))
    i = 1
    while i <= address_number:
        address = str(input(f"送信アドレス({i}): "))
        address_list.append(address)
        if i == address_number:
            print(f"{len(address_list)}件送信します.") 
        i += 1
    
    for address in address_list:
        main(address)