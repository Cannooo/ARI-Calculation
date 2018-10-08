import re
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
spunctuation = '''()-[]{};:'"\,<>/@#$%^&*_~'''

text = input("Enter your text: ")
no_punct=""
for char in text:
    if char not in punctuation:
        no_punct = no_punct+char

sno_punct=""
for char in text:
    if char not in spunctuation:
        sno_punct = sno_punct+char

        
characters = (len(no_punct))-no_punct.count(' ')
print (characters, "characters")
words = len(re.findall(r'\w+', no_punct))
print (words, "words")
sentences = (len(sno_punct))-sno_punct.count(' ')-(characters)
print(sentences, "sentences")

ARI1 = (characters/words)

ARI2 = (words/sentences)

FullARI = 4.71 * ARI1 + 0.5 * ARI2 -21.43

print((round(FullARI)), "is the reading age of this text")


