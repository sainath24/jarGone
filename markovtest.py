import markovify

#text = "provide name email address usage"
words="produce,email"
words = words.split(',')
print(words[0])
f = open("trainmv.txt","r",encoding="utf8")
text = f.read()
model = markovify.Text(text)
str = model.make_sentence()
while words[0] not in str or words[1] not in str:
    str = model.make_sentence()
print(str)
