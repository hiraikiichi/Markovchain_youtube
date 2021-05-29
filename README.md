# 東海オンエアの動画タイトルを自動生成してみた

## :pencil2: 詳しい内容(Qiita)

#### [東海オンエアの動画タイトルを自動生成してみた](https://qiita.com/kii95/items/64afaa389e064c9834d0)

## :computer: 開発環境

- Python 3.7.4
- Anaconda 4.8.5
- mecab-python-windows 0.996.3
- markovify 0.9.0
- google-api-python-client 2.6.0

## フォルダ詳細

- youtube_title.py # 特定のチャンネルの動画全タイトルを取得します
- title_mecab.py # タイトルを形態素解析します
- markov.py # マルコフ連鎖でタイトルを生成します 
