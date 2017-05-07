"""
File to test methods from read_file_CA4
"""

import unittest, csv

from read_file_CA4 import Commit, Change, processFile, processChanges, processList

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.commits = processFile('changes_python.log')
            
    #check that 422 unique commit objects have been added to the list 
    def test_number_commits(self):
        self.assertEqual(422, len(self.commits))
    
    #test that Thomas is the author of the first commit and the last commit
    def test_setAuthor(self):
        #print self.commits[0].getAuthor(), self.commits[421].getAuthor()
        self.assertEqual('Thomas', self.commits[0].getAuthor())
        self.assertEqual('Thomas', self.commits[421].getAuthor())
    
    #test that first commit was made on 13 July 2015 and last commit on 27 November 2015
    def test_setDate(self):
        #print self.commits[0].getDate(), self.commits[421].getDate()
        self.assertEqual('2015-07-13', self.commits[0].getDate())
        self.assertEqual('2015-11-27', self.commits[421].getDate())
    
    #test that second commit was made on a Monday and last commit was made on a Friday
    def test_setDay(self):
        #print self.commits[1].getDay(), self.commits[421].getDay() 
        self.assertEqual('Mon', self.commits[1].getDay())
        self.assertEqual('Fri', self.commits[421].getDay())
        
    #test that the length of the second commit is 20 and last commit is 4 (first line refers to 'Changed paths' and is not counted)
    def test_setChanges(self):
        #print len(self.commits[1].getChanges()), len(self.commits[421].getChanges())
        self.assertEqual(20, len(self.commits[1].getChanges()) - 1) 
        self.assertEqual(4, len(self.commits[421].getChanges()) - 1)
    
    #check that the max/min number of commits for sample list is 4 (11) and 1 (2), and the max/min values are 11, 2
    def test_processList(self):
        test_list = [11, 6, 2, 5, 11, 11, 6, 25, 25, 11, 78, 3, 3, 5]
        processList(test_list)
        self.assertEqual(11, processList(test_list)[0]) #11 has most commits, i.e. max_value
        self.assertEqual(4, processList(test_list)[1]) #max of 4 commits associated with 11
        self.assertEqual(2, processList(test_list)[2]) #2 has least commits, i.e. min_value
        self.assertEqual(1, processList(test_list)[3]) #min of 1 commit associated with 2
    
    #check that the number of commits with > 30 updated files is 12 and details of first long commit are valid
    def test_processChanges(self):
        long_commits = processChanges(self.commits)
        self.assertEqual(12, len(long_commits))
        
    #test that the column names in the CSV file are correct         
    def test_writeCSV(self):
         with open('Commits.csv') as csvfile:
             readCSV = csv.reader(csvfile, delimiter = ',')
             for column in readCSV:
                 self.assertEqual('Author', column[0])
                 print column[0]
                 self.assertEqual('Date', column[1])
                 print column[1]
                 self.assertEqual('Day', column[2])
                 print column[2]
                 self.assertEqual('Changes length', column[3])
                 print column[3]
                 break
                         
if __name__ == '__main__':
    unittest.main()