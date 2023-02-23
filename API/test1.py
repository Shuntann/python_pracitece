from googleapiclient.discovery import build

apiKey = "AIzaSyCdaS1JZZ3IArBYwQShFZ4tjQx_YzrOqZQ"

youtube = build("youtube","v3",  developerKey=apiKey)


request = youtube.channels().list(
    part = "statistics",

    id="UC5Kgc_HNzx4GJ-w4QMeeKiQ"
)

response = request.execute()

print(response)