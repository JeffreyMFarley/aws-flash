import re
import json
import codecs

# -----------------------------------------------------------------------------

def acquire():
    with codecs.open('raw.txt', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            if s:
                yield s

def extract_pair(match, table):
    a = match.group(1).upper()
    b = match.group(2).strip().translate(table)
    return (a, b)

def buildPunctuationReplace():
    table = {0xa6 : u'|',
             0xb4 : u'\'',
             0xb6 : u'*',
             0xd7 : u'x',

            0x2022 : u'*',   # bullet
            0x2023 : u'*',   
            0x2024 : u'.',   
            0x2027 : u'*',
            0x2032 : u"'",
            0x2035 : u"'",
            0x2039 : u'<',
            0x203a : u'>',
            0x2043 : u'-',
            0x2044 : u'/',
            0x204e : u'*',
            0x2053 : u'~',
            0x205f : u' ',
            0x2192 : u'>'    # rightwards arrow
            }
    table.update({c :u' ' for c in range(0x2000, 0x200a)})
    table.update({c :u'-' for c in range(0x2010, 0x2015)})
    table.update({c :u"'" for c in range(0x2018, 0x201b)})
    table.update({c :u'"' for c in range(0x201c, 0x201f)})

    return table

# -----------------------------------------------------------------------------

def run():
    sm = [
        re.compile('([0-9]+)\.\s(.*)'),
        re.compile('([a-fA-F])\.?\s(.*)'),
        re.compile('([a-fA-F])+')
    ]
   
    table = buildPunctuationReplace()

    state = 0
    accum = {}
    num = 1

    for l in acquire():
        m = sm[state].match(l)
        if not m:
            m = sm[2].match(l)
            if m:
                accum['answers'] = [c for c in l.strip()]
                yield accum
            else:
                print('Lost State around {0}'.format(num))
            state = 0
            accum = {}

        elif state == 0:
            num, accum['text'] = extract_pair(m, table)
            accum['options'] = {}
            state = state + 1       

        elif state == 1:
            on, t = extract_pair(m, table)
            accum['options'].update({on: t})

if __name__ == '__main__':
    questions = [q for q in run()]
    with open('questions.json', 'w') as f:
        json.dump(questions, f, sort_keys=True)

