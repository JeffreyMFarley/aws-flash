import sys
import os
import json
import random
import textwrap
from collections import Counter
if sys.version < '3':
    _input = raw_input
else:
    _input = input

# -----------------------------------------------------------------------------

def wrapped_out(i, s):
    lead = '{0}. '.format(i)
    wrapper = textwrap.TextWrapper(initial_indent=lead,
                                   subsequent_indent=' ' * len(lead))
    s = wrapper.fill(s)
    print(s)

def ask(i, q):
    os.system('cls' if os.name == 'nt' else 'clear')

    wrapped_out(i, q['text'])
    print('\n')

    for k in sorted(q['options']):
        wrapped_out(k, q['options'][k])
    print('\n')

    a = _input('> ').upper().translate({ord(' '): None, ord(','): None})
    return [x for x in a]

def check(q, a):
    compare = Counter(q['answers']) == Counter(a)
    return 10 if compare else 0

def reveal(q, a, s):
    print('Correct' if s else 'Incorrect')
    if not s:
        print(', '.join(sorted(q['answers'])))
    _input("'Enter' to continue")

# -----------------------------------------------------------------------------

def run():
    with open('questions.json') as f:
        questions = json.load(f)

    exam = random.sample(questions, 20)
    for i, question in enumerate(exam):
        answer = ask(i + 1, question)
        score = check(question, answer)
        reveal(question, answer, score)

if __name__ == '__main__':
    run()
