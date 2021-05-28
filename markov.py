import markovify

with open("./title_mecab.txt", "r", encoding="utf-8") as file:
    text = file.read()
    
# モデル作成
text_model = markovify.NewlineText(text, state_size=2, well_formed=False)


with open('./learned_data.json', 'w') as f:
    f.write(text_model.to_json())
    
with open('learned_data.json', 'r', encoding="utf-8") as f:
    text_model = markovify.Text.from_json(f.read())
    
li = []
for i in range(500): # 500タイトル作成
    li.append(text_model.make_short_sentence(140).replace(" ", ""))

with open('./out.txt', mode='w', encoding="utf-8") as f:
    f.write('\n'.join(li))
