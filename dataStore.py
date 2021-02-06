# -*- coding: utf-8 -*-
#Activity Online - an online guessing game
#Copyright (C) 2021 Peter Munk

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as
#published by the Free Software Foundation, either version 3 of the
#License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.

#You should have received a copy of the GNU Affero General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

import csv
import random
import itertools
import os

wordPath = 'wordLists/'

class DataStore:

    data = []
    wordListSet = []
    
    def __init__(self, wordListSet):
        self.wordListSet = wordListSet;
        self.reset()
    
    def isEmpty(self):
        return not self.data
    
    def getRandomElement(self):
        if not self.data:
           return "[Empty]"
        else:
            element = random.choice(self.data)
            self.data.remove(element)
            #print(element)
            return element
            
    def reset(self):
        for wordList in self.wordListSet:
            try:
                with open(wordPath+wordList+'.csv', newline='',  encoding='utf-8') as file:
                    reader = csv.reader(file)
                    unflattened = list(reader)
                    self.data.extend(list(itertools.chain(*unflattened)))
            except IOError:
                print(wordPath+wordList+'.csv does not exist')
        print(self.data)

    def getAvailableLists():
        availFiles = {}
        for file in os.listdir(wordPath):
            availFiles[file[:len(file)-4]] = len(open(wordPath+file).readlines(  ))
        return availFiles