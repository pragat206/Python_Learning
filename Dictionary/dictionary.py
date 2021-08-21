import random
from PyDictionary import PyDictionary
from plyer import notification

dictionary = PyDictionary()
word = random.choice(open("C:\\Users\\LENOVO\\learn\\words.txt").readlines())



mean = str(dictionary.meaning('Noun',word))

title = 'Words and Meaning'
message = word +':and the meaning is '+ mean

notification.notify(title= title,
                    message= message,
                    app_name = "Vocabs",
                    app_icon = None,
                    timeout= 240,
                    toast=False)