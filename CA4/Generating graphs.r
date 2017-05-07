#Locate the correct working directory
setwd("C:/Users/bankhawk_9/Desktop/DRCA4")

#read in the Commits file
data <- read.csv('Commits.csv', header=TRUE, sep = ",")

#replace values from authors column to make Authors graph more readable
data$Author <- factor(gsub("/OU=Domain Control Validated/CN=svn.company.net", "Domain Control Validated", data$Author))

#plot the 3 graphs and set the graph and axes titles 
plot(data[1], type="l", main = paste("Number of commits by", colnames(data)[1]), xlab = "Author name", ylab = "Number commits")

plot(data[2], type="l", main = paste("Number of commits by", colnames(data)[2]), xlab = "Date", ylab = "Number commits")

plot(data[3], type="l", main = paste("Number of commits by", colnames(data)[3]), xlab = "Day", ylab = "Number commits")