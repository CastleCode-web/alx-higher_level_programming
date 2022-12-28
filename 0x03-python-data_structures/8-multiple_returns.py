#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return len(sentence), None
    else:
        return len(sentence), sentence[0]


#MyCode
'''#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0]
    if len(sentence) == 0:
        return (a, None)
    else:
        return (a, b)
'''
