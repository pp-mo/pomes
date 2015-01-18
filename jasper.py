def showline(words):
  line = ''
  for i_at, word in enumerate(words):
    if i_at == 0:
      word = word[0].upper() + word[1:]
    if i_at == len(words) - 1:
      if word[-1] == ',':
        word = word[:-1]
    else:
      word = word + ' '
    line = line + word
  print line + '!'

def song(phrase):
  words = phrase.split()
  while words:
    for _ in range(3):
      showline(words)
    print '<refrain>\n'
    words = words[:-1]

phrase = "oh, Sir Jasper, do not touch me"
song(phrase)

