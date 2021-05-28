import MeCab

with open('./youtube_title.txt', mode='rt', encoding='utf-8') as f:
    read_data = list(f)

m = MeCab.Tagger('-Owakati')
f = open('./title_mecab.txt', 'w', encoding="utf-8")

for line in read_data:
    if '&amp;' in line or '&#39;' in line or '&quot;' in line:
        line = line.replace('&amp;', '&').replace('&#39;', "'").replace('&quot;', '"')
    splited_line = m.parse(line)
    f.write(str(splited_line))
f.close()
