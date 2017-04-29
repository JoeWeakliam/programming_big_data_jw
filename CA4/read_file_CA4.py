"""
Program to read in the changes log file
"""

import xlwt
from tempfile import TemporaryFile

changes_file = 'changes_python.log'
data = [line.strip() for line in open(changes_file, 'r')]

#create a class of commit objects
class Commit(object):
    
    #none values allow you  to create commit objects with no parameters 
    def __init__(self, author = None, date = None, day = None, comment_line_count = None, changes = None):
        self.author = author
        self.date = date
        self.day = day
        self.comment_line_count = comment_line_count
        self.changes = changes
            
    #define the set and get methods relevant to 'my interesting facts'
    def setAuthor(self, author):
        self.author = author
    
    def getAuthor(self):
        return self.author
    
    def setDate(self, date):
        self.date = date
    
    def getDate(self):
        return self.date
    
    def setDay(self, day):
        self.day = day
    
    def getDay(self):
        return self.day
    
    def setChanges(self, changes):
        self.changes = changes
    
    def getChanges(self):
        return self.changes

#class Author extends Commit
'''class Author(Commit):
    
    def __init__(self, num_authors = None, max_author = None, min_author = None, num_commits = None):
        self.num_authors = num_authors
        self.max_author = max_author
        self.min_author = min_author
        self.num_commits = num_commits
    
    def setNumAuthors(self, number):
        self.num_authors = number
    
    def getNumAuthors(self):
        return self.num_authors
    
    def setMaxAuthor(self, name):
        self.max_author = name
    
    def getMaxAuthor(self):
        return self.max_author
    
    def setMinAuthor(self, name):
        self.min_author = name
    
    def getMinAuthor(self):
        return self.min_author
    
    def getNumCommits(self):
        return self.num_commits'''

#process list of authors to count number of commit comments by author
def processAuthors(authors):
    #create a list of unique authors
    unique_authors = []
    #create variables to record max and min number of commits and the most and least productive authors
    max_commits = 0
    min_commits = 0
    max_author = None
    min_author = None
    #for each author in the list of commit objects
    for author in authors:
        if author not in unique_authors:
            unique_authors.append(author) #add to list of unique authors
    #unique_authors.sort()
    #count number of occurrences of each unique author
    for unique_author in unique_authors:
        #print unique_author, authors.count(unique_author)
        #if number of commits of current author is greater than max_author
        if max_commits == 0 or max_commits < authors.count(unique_author):
            max_commits = authors.count(unique_author)
            max_author = unique_author
            #print max_author, authors.count(unique_author)
        #if number of commits of current author is less than min_author
        if min_commits == 0 or min_commits > authors.count(unique_author):
            min_commits = authors.count(unique_author)
            min_author = unique_author
            #print min_author, authors.count(unique_author)
    print 'Max {} commits made by {}'.format(max_commits, max_author)
    print 'Min {} commits made by {}'.format(min_commits, min_author)
            
#process list of dates to count number of commit comments made on each distinct date
def processDates(dates):
    #create a list of unique dates
    unique_dates = []
    max_commits = 0
    min_commits = 0
    max_date = None
    min_date = None
    #for each date associated with each commit object
    for date in dates:
        if date not in unique_dates:
            unique_dates.append(date) #add to list of unique dates
    #count number of occurrences of each unique date
    for unique_date in unique_dates:
        #print unique_date, dates.count(unique_date)
        #if number of commits made on the current date is greater than max_date
        if max_commits == 0 or max_commits < dates.count(unique_date):
            max_commits = dates.count(unique_date)
            max_date = unique_date
        #if number of commits of current date is less than min_date
        if min_commits == 0 or min_commits > dates.count(unique_date):
            min_commits = dates.count(unique_date)
            min_date = unique_date
    print 'Max {} commits made on {}'.format(max_commits, max_date)
    print 'Min {} commits made on {}'.format(min_commits, min_date)

#process list of days to count number of commit comments made on each day of the week
def processDays(days):
    #create a list of unique days
    unique_days = []
    max_commits = 0
    min_commits = 0
    max_day = None
    min_day = None
    #for each day linked to each commit object
    for day in days:
        if day not in unique_days:
            unique_days.append(day) #add to list of unique days
    #count number of occurrences of each unique day
    for unique_day in unique_days:
        #print unique_day, days.count(unique_day)
        #if number of commits made on the current day is greater than max_day
        if max_commits == 0 or max_commits < days.count(unique_day):
            max_commits = days.count(unique_day)
            max_day = unique_day
        #if number of commits of current day is less than min_author_commits
        if min_commits == 0 or min_commits > days.count(unique_day):
            min_commits = days.count(unique_day)
            min_day = unique_day
    print 'Max {} commits made on {}'.format(max_commits, max_day)
    print 'Min {} commits made on {}'.format(min_commits, min_day)

#process list of changes/authors to record number of commits involving more than 10 files being updated
def processChanges(changes, authors):
    index = 0
    num_files_updated = 10
    large_commits = {}
    #largest_commit = None
    #commit_author = None
    for change in changes:
        if len(change) > num_files_updated:
            large_commits = {'change' : 'hello'}
            #print change, authors[index]
            index += 1
    #print large_commits.

#write to excel file to generate plots using R         
def writeExcel(commits):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('Commits')

    #supersecretdata = [34,123,4,1234,12,34,12,41,234,123,4,123,1,45123,5,43,61,3,56]
    #for i, e in enumerate(supersecretdata):
        #sheet1.write(i,1,e)
        
    for index, commit in enumerate(commits):
        sheet1.write(index, 1, str(commit.getAuthor()))
        
    name = "Commits.csv"
    book.save(name)
    book.save(TemporaryFile())     

       
commits = [] #store commit objects in a list
sep = 72*'-' #separator of 72 hyphens
current_commit = None
index = 0 

#search for separator, read line for revision, author, date, comment line count
#read file changes, read comment
#get next commit
while True:
    try:
        #parse each of the commits and put them into a list of commit objects
        current_commit = Commit()
        details = data[index + 1].split('|')
        #call setAuthor() method
        current_commit.setAuthor(details[1].strip())
        #call setDate() method - Note we are only interested in the yyyy-mm-dd substring here
        current_commit.setDate(details[2].strip().split(' ')[0])
        #call setDay() method - Note we need to access the relevant substring to get the specific day
        current_commit.setDay(details[2].strip().split(' ')[3][1:4])
        #delete this as not relevant to my analysis
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        #call setChanges() method - Note data[0:5] returns data from line 0 up to line 4
        current_commit.setChanges(data[index+2:data.index('',index+1)]) 
        index = data.index(sep, index + 1) #index function searches ahead to find next separator and assigns new value to index variable
        commits.append(current_commit) #add current commit object to list of commits
    except IndexError:
        break

#print len(commits)
print commits[0].getAuthor()
print commits[0].getDate()
print commits[0].getDay()
print commits[0].getChanges()

#reorder the list in chronological order
commits.reverse()

#create a list of authors, dates, days and changes to allow statistical analysis to be run on each attribute
authors = []
dates = []
days = []
changes = []

#process list of commit objects and add key attributes to new lists
for index, commit in enumerate(commits):
    #first access commit author
    #print(commit.getAuthor())
    authors.append(commit.getAuthor())
    dates.append(commit.getDate())
    days.append(commit.getDay())
    changes.append(commit.getChanges())
#call relevant methods to process attribute lists
processAuthors(authors)
processDates(dates)
processDays(days)
processChanges(changes, authors)
writeExcel(commits)


        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    