#!/usr/bin/env python3

with open('./retail_transactions.csv', encoding='latin-1') as file:
    for i, line in enumerate(file):
        if i > 38170 and i < 38180:
            print(i, ' ', line)

try:
    with open('./retail_transactions.csv') as file:
        for i, line in enumerate(file):
            line = bytes(line, 'utf-8').decode('utf-8', 'ignore')
except Exception as e:
    print(e)
    print('Line:', i)