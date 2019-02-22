#!/usr/bin/env python3

import os, lxml.etree

os.chdir('xml_docs/')

insider_count = 0
total_count = 0
error_count = 0

for i in os.listdir():
    try:
        print(i)

        if i.endswith('jpg'):
            os.remove(i)
            continue

        tree = lxml.etree.parse(i)
        root = tree.getroot().tag
        
        if root == 'ownershipDocument':
            insider_count += 1
        else:
            os.remove(i)
        total_count += 1
    except:
        error_count += 1

print()
print('Insider count:\t\t', insider_count)
print('Total count:\t\t', total_count)
print('Files deleted:\t\t', total_count - insider_count)
print('\nErrors:\t\t', error_count)

os.chdir('..')