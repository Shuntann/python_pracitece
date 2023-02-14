from google.oauth2.credentials import credentials
from googleapiclient.discovery import build
import json
import base64

from httplib2 import Credentials

def get_header(headers, name):
    for header in headers:
        if header["name"].lower() == name:
            return header["value"]

def base64_decode(data):
    return base64.urlsafe_b64decode(data).decode()

def base64_decode_file(data):
    return base64.urlsafe_b64decode(data.encode("UTF-8"))

def get_body(body):
    if body["size"] > 0:
        return base64_decode(body["data"])

def get_parts_body(body):
    if (body["size"] > 0 and "data" in body.keys() and "mimeType" in body.keys() and body ["mimeType"] == "text/plain"):
        return base64_decode(body["data"])

def get_parts(parts):
    for part in parts:
        if part["mimeType"]=="text/plain":
            b = base64_decode(part["body"]["data"])
            if b is not None:
                return b
        
        if "body" in part.keys():
            b= get_parts_body(part["body"]["data"])
            if b is not None:

def get_attachment_id(parts):
    for part in parts:
        print(part["mimeType"])


def main(address):
    scopes =["https://mail.google.com/"]
    creds = Credentials.from_authorized_user_file("token.json", scopes)
    service = build("gmail", "v1", credentials = creds)

    messages = service.users().messages().list(
        userId="me",
        q = address
    ).execute().get("messages")

    for message in messages:
        print("=" *10)
        m_data = service.users().message().get(
            userId="me",
            id = message["id"]
        ).execute()

        #ヘッダー情報習得
        headers = m_data["payload"]["headers"]
        
        #日付
        date_data = get_header(headers,"data")
        print(f"日付: {date_data}")

        from_data = get_header(headers, "from")
        print(f"差出人: {from_data}")

        to_data = get_header(headers, "to")
        print(f"宛先: {to_data}")

        sub_data = get_header(headers, "subject")
        print(f"差出人: {sub_data}")

        body = m_data["payload"]["body"]
        body_data = get_body(body)

        if "parts" in m_data["payload"].keys():
            parts = m_data["payload"]["parts"]
            parts_data = get_parts(parts)

            attachment_id, extension = get_attachment_id(parts)

        


if __name__ == "__main__":
    address = str(input("受信メアド: "))


    main(address)