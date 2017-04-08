import os
import re

if __name__ == '__main__':
    root = os.getcwd()

    for subdir, dirs, files in os.walk(root):
        for file in files:
            if file.endswith('.md'):
                f = open(os.path.join(subdir, file), 'r')
                file_content = f.read()

                category = subdir[subdir.rfind('/') + 1:]

                repl = '''---
title: ''' + file[:-3] + '''
date: 2017-04-08
categories: ''' + category+ '''
tags: ''' + category + '''
---'''
                file_content = re.sub('(?s)^#.*<!-- MDTOC.*?<!-- /MDTOC -->', repl, file_content)

                f.close()
                f = open(os.path.join(subdir, file), 'w')
                f.write(file_content)
                f.close()


