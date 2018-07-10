#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import glob
import os

class Paper():
    def __init__(self):
        self.name = ""
        self.number = 0
        self.track = ""
        self.authors = []

class Author():
    def __init__(self):
        self.name = ""
        self.affiliation = ""
        self.email = ""

with open('SBES 2017.csv', 'r') as csvfile:
    papers = []
    papers_data = csv.reader(csvfile, delimiter = ',', quotechar='"')
    for row in papers_data:
        paper = Paper()
        papers.append(paper)
        col_number = 0

        for col in row:
            if col_number == 0:
                paper.number = int(col.strip())
            elif col_number == 1:
                paper.track = col.strip()
            elif col_number == 2:
                paper.name = col.strip()
            elif (col_number % 2) == 1:
                if ('@' in col):
                    break
                current_author = Author()
                current_author.name = col.strip()
                paper.authors.append(current_author)
            elif (col_number % 2) == 0:
                current_author.affiliation = col.strip()
            col_number += 1

    for paper in papers:
        paper_directory = ""
        paper_filename = ""
        author_number = 0
        print('\procpaper[')
        print('\ttitle={' + paper.name + '},')
        print('\tauthor={', end = '')
        for author in paper.authors:
            if (author_number > 0):
                print(', ', end = '')
            print(author.name, end = '')
            author_number += 1
        print('},')

        print('\tindex={', end = '')
        for author in paper.authors:
            print('\index{' + author.name + '}', end = '')
        print('}]', end = '')
        print('{', end = '')
        if paper.track == 'Research':
            paper_directory = os.path.join('papers', 'research')
        elif paper.track == 'Education':
            paper_directory = os.path.join('papers', 'education')
        else:
            paper_directory = os.path.join('papers', 'insightful-ideas')
        for filename in sorted(glob.glob(os.path.join(paper_directory, str(paper.number) + '*.pdf'))):
            paper_filename = filename[:-len('.pdf')]
        print(paper_filename + '}') 
        print()




