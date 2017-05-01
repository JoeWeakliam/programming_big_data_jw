
# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

print(len(commits))

commits.reverse()

for index, commit in enumerate(commits):
    print(commit.get_commit_comment())
