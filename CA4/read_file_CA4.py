"""
Created on Wed Apr 26 18:34:55 2017

@author: bankhawk_9
"""

#C:\Users\bankhawk_9\Desktop\DRCA4
changes_file = 'changes_python.log'

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]
print len(data)

sep = 72*'-' #separator of 72 hyphens

#commit class
class Commit(object):
    
    #nones allow you  to create commit objects with no parameters 
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

a_commit = Commit('r1551925', 'Thomas', '2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', 1, None, 'Renamed folder to the correct name')
print a_commit.revision
print a_commit.author
print a_commit.comment

commits = [] #store commit objects in a list
current_commit = None
index = 0 

#search for separator
#read line for revision, author, date, comment line count
#read file changes
#read comment
#get next commit
while True:
    try:
        #parse each of the commits and put them in a list
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = details[0].strip()
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)] #data[0:5] returns data from line 0 up to line 4
        index = data.index(sep, index + 1) #index function searches ahead to find the next separator and assigns new value to index variable
        current_commit.comment = data[index-current_commit.comment_line_count:index] #determines length of comment
        commits.append(current_commit) 
        
    except IndexError:
        break

#print len(commits)
#print commits[0].author
print commits[0].comment
print commits[0].changes


commits.reverse() #reorder the list in chronological order

#for index, commit in 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    