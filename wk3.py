newriter = open("mydata.txt", 'w')

newriter.write("hey,\n i am witing")
newriter.writelines(['new', 'list', 'test'])

newriter.close()

readerobject = open('mydata.txt', 'r')

# Part 3: Putting It All Together