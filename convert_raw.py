import os
import sys
import re

# -----------------------------------------------------------------------------

def acquire():
    with open('raw.txt') as f:
        for line in f:
            s = line.strip()
            if s:
                yield s

def extract_pair(match):
    a = match.group(1).upper()
    b = match.group(2).strip()
    return (a, b)

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    sm = [
        re.compile('([0-9]+)\.\s(.*)'),
        re.compile('([a-fA-F])\.?\s(.*)'),
        re.compile('([a-fA-F])+')
    ]

    state = 0
    errs = {}
    question = {}

    for l in acquire():
        m = sm[state].match(l)
        if not m:
            m = sm[2].match(l)
            if m:
                question['answers'] = [c for c in l.strip()]
                print(question)
                question = {}
            else:
                print('Lost State')
                errs[question['number']] = l
            state = 0

        elif state == 0:
            question['number'], question['text'] = extract_pair(m)
            question['options'] = []
            state = state + 1       

        elif state == 1:
            on, otext = extract_pair(m)
            question['options'].append({on: otext})

    print(errs)
