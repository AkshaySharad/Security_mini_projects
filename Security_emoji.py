# Converting emojis to text - https://wellsr.com/python/convert-text-to-emojis-and-vice-versa-in-python/

emoji_dictionary = {'👍': '[thumbs_up]',
                   '❤':'[red_heart]',
                    '😞':'[happy_face]'}

# print(emoji_dictionary['❤'])


text = 'I love Python ❤ , it is brilliant 👍'
text_tokens = text.split(" ")
# print(text_tokens)

new_text = ""
for i in text_tokens:
    if i in emoji_dictionary:
        new_text +=  " " +emoji_dictionary[i]
    else:
        new_text += " " + i

# print(new_text)

#b Converting text to emojis
emoji_dictionary2 = dict([(value, key) for key, value in emoji_dictionary.items()])

# print(emoji_dictionary2)

new_text = ""
for i in text_tokens:
    if i in emoji_dictionary2:
        new_text +=  " " +emoji_dictionary2[i]
    else:
        new_text += " " + i

# print(new_text)

import emoji

text = 'I love Python :red_heart: , it is brilliant :thumbs_up:'
print(emoji.emojize(text))


# Using emot library
import emot

# Detecting emojis
emot_object = emot.core.emot()
text = "This is a brilliant movie 👌"
# print(emot_object.emoji(text))
text = "I love Python ❤️, it is brilliant 👍"
# print(emot_object.emoji(text))

# Detecting emoticons
text1 = "I love you :)"
# print(emot_object.emoticons(text1))



