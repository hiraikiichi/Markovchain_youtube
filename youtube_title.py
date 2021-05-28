from apiclient.discovery import build
import json
import datetime
from dateutil.relativedelta import relativedelta

# API情報
API_KEY = '【取得したAPI】'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

videos = [] #videoURLを格納する配列

def youtube_search(pagetoken, st, ed):
  youtube = build(
      YOUTUBE_API_SERVICE_NAME, 
      YOUTUBE_API_VERSION,
      developerKey=API_KEY
      )

  search_response = youtube.search().list(
    channelId = 'UCutJqz56653xV2wwSvut_hQ',
    part = 'snippet',
    type = 'video',
    maxResults = 50,
    publishedAfter = st, 
    publishedBefore = ed, 
    pageToken = pagetoken
  ).execute()

  print(search_response["pageInfo"]["totalResults"])

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      d = search_result["snippet"]["title"]
      videos.append(d)

  try:
    nextPagetoken =  search_response["nextPageToken"] 
    print(nextPagetoken)
    youtube_search(nextPagetoken, st, ed)
  except:
    return

dt = datetime.datetime(2013, 10, 1, 0, 0) # 動画投稿開始月を設定
for i in range(1, 97): # 97回(だいたい今月まで回す)
  youtube_search('', dt.isoformat()+'Z', (dt + relativedelta(months = 1)).isoformat()+'Z')
  dt = dt + relativedelta(months=1)

path_w = './youtube_title.txt'

with open(path_w, mode='w', encoding="utf-8") as f:
    f.write('\n'.join(videos))
