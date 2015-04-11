#!/usr/bin/evn python 

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\ "
def remove_punctuation(s):
    s_sans_punc=""
    for letter in s:
       if letter not in punctuation:
           s_sans_punc += letter
    return s_sans_punc

s = "Well, I never did!, said Alice."
print remove_punctuation(s)
