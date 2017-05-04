"""
Program to read in and process the changes log file into a list of 'commit' objects 
"""
#import packages to allow creation of and export to CSV file
import xlwt
from tempfile import TemporaryFile

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

#class Change extends Commit and inherits all the class methods 
class Change(Commit):
    
    #none values allow you  to create change objects with no parameters 
    def __init__(self, author = None, num_changes = None):
        self.author = author
        self.num_changes = num_changes

#generic method to process list of attibutes to count the number of commits linked to a specific attribute value, e.g. date 
def processList(input_list):
    #create a list of unique values
    unique_values = []
    #create variables to record the max and min number of commits by attribute value and the highest and lowest attribute values
    max_commits = 0
    min_commits = 0
    max_value = None
    min_value = None
    #for each value in the list of commit objects
    for value in input_list:
        if value not in unique_values:
            unique_values.append(value) #add to list of unique values
    #count number of occurrences of each unique value
    #print unique_values
    for unique_value in unique_values:
        #if number of commits of current attribute value is greater than max_value
        if max_commits == 0 or max_commits < input_list.count(unique_value):
            max_commits = input_list.count(unique_value)
            max_value = unique_value
        #if number of commits of current attribute value is less than min_value
        if min_commits == 0 or min_commits > input_list.count(unique_value):
            min_commits = input_list.count(unique_value)
            min_value = unique_value
    #want to return multiple values
    #print max_value, max_commits, min_value, min_commits
    return max_value, max_commits, min_value, min_commits
         
#process list of changes/authors to record details about commits involving more than 20 files being updated
def processChanges(commits):
    index = 0
    num_files_updated = 30 #set min number of changed files that we are interested in 
    large_commits = [] #create a list of change objects where num_files_updated > 30
    while index < len(commits):
        if len(commits[index].getChanges()) > num_files_updated:
            change = Change() #create a new change object and set its attributes
            #print 'new'
            change.setAuthor = commits[index].getAuthor()
            change.setChanges = commits[index].getChanges()
            large_commits.append(change) #add to list of large commits
        index += 1 #increment value of index outside of 'if' clause
    return large_commits

#write to CSV file to generate plots using R         
def writeCSV(commits):
    book = xlwt.Workbook() #create the workbook and active sheet
    sheet1 = book.add_sheet('Commits')
    index = 0
    #set the column names
    sheet1.write(index, 0, 'Author')
    sheet1.write(index, 1, 'Date')
    sheet1.write(index, 2, 'Day')
    sheet1.write(index, 3, 'Changes length')
    #populate the rows with attribute values from commit objects
    for index, commit in enumerate(commits):
        sheet1.write(index + 1, 0, str(commit.getAuthor()))
        sheet1.write(index + 1, 1, str(commit.getDate()))
        sheet1.write(index + 1, 2, str(commit.getDay()))
        sheet1.write(index + 1, 3, len(commit.getChanges())) #causes exception: String longer than 32767 characters
    #name and save the file
    name = "Commits.csv"
    book.save(name)
    book.save(TemporaryFile())
    return book

#read in and process the relevant log file detailing commit activity
def processFile(file_name):
    changes_file = file_name
    data = [line.strip() for line in open(changes_file, 'r')]
    #initialise key variables for processing log file       
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

    commits.reverse() #sort the commit objects in chronological order 
    return commits

#populate the lists of attribute objects that we want to analyse for interesting statistics 
def populate_lists(commits):
    #create a list of authors, dates, days and changes to allow statistical analysis to be run on each attribute
    authors = []
    dates = []
    days = []
    #process list of commit objects and add key attributes to new lists
    for index, commit in enumerate(interesting_commits):
        #add attributes of each commit object to corresponding list 
        authors.append(commit.getAuthor())
        dates.append(commit.getDate())
        days.append(commit.getDay())
            
    #call processList method to process attribute lists and generate interesting stats
    print 'The following interesting statistics were generated from the data:'
    author_stats = processList(authors)
    print 'Max {} commits made by {}'.format(author_stats[1], author_stats[0])
    print 'Min {} commits made by {}'.format(author_stats[3], author_stats[2])
    date_stats = processList(dates)
    print 'Max {} commits made on {}'.format(date_stats[1], date_stats[0])
    print 'Min {} commits made on {}'.format(date_stats[3], date_stats[2])
    day_stats = processList(days)
    print 'Max {} commits made on {}'.format(day_stats[1], day_stats[0])
    print 'Min {} commits made on {}'.format(day_stats[3], day_stats[2])
    change_stats = processChanges(commits)
    print 'Number of commits with > 30 updated files: {}'.format(len(change_stats))
    
#run the program to generate the results 
if __name__ == '__main__':
    interesting_commits = processFile('changes_python.log') 
    populate_lists(interesting_commits)
    writeCSV(interesting_commits) #generate the CSV file        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    