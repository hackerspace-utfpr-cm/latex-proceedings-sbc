#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

with open('SBES 2017.csv', 'r') as csvfile:
    papers = csv.reader(csvfile, delimiter = ',', quotechar='"')
    for row in papers:
        col_number = 0
        emails = False
        author_number = 0
        for col in row:
            if not col.strip():
                break

            if col_number == 0:
                print('"' + col.strip() + '"', end = '')
            elif col_number == 1:
                print(',"' + col.strip() + '"', end = '')
            elif emails == False and '@' in col:
                emails = True
                if author_number > 0:
                    print('"', end = '')
                author_number = 0

            if col_number > 1:
                if not emails:
                    if author_number == 0:
                        print(',"', end = '')
                    
                    if (col_number - 2) % 2 == 0:
                        if author_number != 0:
                            print(';', end = '')
                        print(col.strip(), end = '')
                        author_number += 1
                    elif (col_number - 2) % 2 == 1:
                        print( ':' + col.strip(), end = '')
                else:
                    if author_number == 0:
                        print( ',"' + col.strip() + '"', end = '')
                    elif author_number == 1:
                        print( ',"' + col.strip(), end = '')
                    elif author_number > 1:
                        print( ';' + col.strip(), end = '')
                    author_number += 1

            col_number += 1
        if author_number > 1:
            print('"')
