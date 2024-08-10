

## CLASS WORK 
## DATE: MAY 27 2024



##Part 1: Creating and Using Objects

class Book:
    def __init__(self, title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return "Title:" + self.title + "," + "Author : "+ self.author +", Year :" + str(self.year) +"."
    

newbook = Book("PHYSICS", "ALBERT EINSTEIN", 2001)
secondbook = Book("MATH", "ALBERT EINSTEIN", 2005)
thirdbook = Book("CHEMISTRY ", "ALBERT EINSTEIN", 2007)
print(newbook)
print(secondbook)
print(thirdbook)

list =[newbook, secondbook,thirdbook]
# Write a function named `write_books_to_file` that takes a list of `Book` objects and a
def write_books_to_file(list):
  newwriter = open('booksdata.txt','w') 
  for item in list:
      newwriter.write(item.title + " " + item.author + " " +str(item.year) +" \n")

  newwriter.close()
  
##Part 2: Reading from and Writing to Text Files
write_books_to_file(list)
listing = []
def read_books_from_file(filename):
     readerobject = open("booksdata.txt",'r')
     for line in readerobject:
      listing.append(line)
     return(listing)


print(read_books_from_file("booksdata.txt"))




# def read_books_from_file(filename):
#      readerobject = open("booksdata.txt",'r')
#      listAux=[]
#      for line in readerobject.readlines():
#       title,author,year=line.strip().split(",")
#       listAux.append(Book(title,author,year))
#      return listAux