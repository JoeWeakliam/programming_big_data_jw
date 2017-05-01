"""
File to test methods from read_file_CA4
"""

import unittest

from read_file_CA4 import Commit, Change

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.commits = process_file('changes_python.log')
        #print len(self.commits)
    
    #check that 422 unique commit objects have been added to the list 
    def test_number_commits(self):
        self.assertEqual(422, len(self.commits))
    
    #test that Thomas is the author of the first commit and the last commit
    def test_setAuthor(self):
        print self.commits[0].getAuthor(), self.commits[421].getAuthor()
        self.assertEqual('Thomas', self.commits[0].getAuthor())
        self.assertEqual('Thomas', self.commits[421].getAuthor())
    
    #test that first commit was made on 13 July 2015 and last commit on 27 November 2015
    def test_setDate(self):
        print self.commits[0].getDate(), self.commits[421].getDate()
        self.assertEqual('2015-07-13', self.commits[0].getDate())
        self.assertEqual('2015-11-27', self.commits[421].getDate())
    
    #test that second commit was made on a Monday and last commit was made on a Friday
    def test_setDay(self):
        print self.commits[1].getDay(), self.commits[421].getDay() 
        self.assertEqual('Mon', self.commits[1].getDay())
        self.assertEqual('Fri', self.commits[421].getDay())
        
    #test that the length of the second commit is 20 and last commit is 4 (first line refers to 'Changed paths' and is not counted)
    def test_setChanges(self):
        print len(self.commits[1].getChanges()), len(self.commits[421].getChanges())
        self.assertEqual(20, len(self.commits[1].getChanges()) - 1) 
        self.assertEqual(4, len(self.commits[421].getChanges()) - 1)
    
    #check that the number of commits with > 20 updated files is 23 and details of first long commit are valid
    def test_processChanges(self):
        long_commits = processChanges(self.commits)
        self.assertEqual(23, len(long_commits))
        #print long_commits[1].getAuthor()
        #self.assertEqual('Thomas', long_commits[1].getAuthor())
        #self.assertEqual(12, long_commits[2].getChanges())
        
    '''def test_writeCSV(self):
         csv = writeCSV(commits)
         print len(csv)'''
        
if __name__ == '__main__':
    unittest.main()