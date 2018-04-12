import string
abs = string.ascii_lowercase

def strToBin():
    plainText = ''
    with open('strText', 'r') as f:
        for line in f:
            plainText += line
    with open('binTextResult', 'a') as f:
        f.write(''.join((''.join(('0' * (6 - len(format(abs.index(c), 'b'))), format(abs.index(c), 'b'))) if c in abs else c) for c in plainText))
    return 'Complete !'

def binToStr():
    binText = res = ''; i = 0
    with open('binTextResult', 'r') as f:
        for line in f:
            binText += line
    while i < len(binText):
        res += (abs[int(binText[i:i+6], 2)] if binText[i] in '01' else binText[i])
        if binText[i] not in '01': i -=5
        i += 6
    with open('strTextResult', 'a') as f:
        f.write(res)
    return 'Complete !'

strToBin()
