# aqssignment
#Author : Gbolahan Adebowale 


## a function to read the file and sort them out 
def bookreader(openbook):
    # Open and read the file
    with open(openbook, 'r') as readerobject:
        book = readerobject.read().lower().replace(',', '').replace('.', '').replace('-', '').replace("'", '').strip().split()
    
    # Count word frequencies
    wc = {}
    for i in book:
        if i in wc:
            wc[i] += 1
        else:
            wc[i] = 1
    
    # Print word counts
    for word, count in wc.items():
        print(f'{word} {count}')
    
    return wc

#### second function to write the book with the word count
def bookwriter(writebook, word_counts):
    # Sort words by frequency (from most to least frequent)
    wordsorter = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Write the sorted words and their counts to a file
    with open(writebook, "w") as writerobject:
        for word, count in wordsorter:
            writerobject.write(f'{word} {count}\n')

# 
word_counts = bookreader('Assignment1/sample.txt')  # Read and count words this take the file path as the argument

##function that takes the 2 arugument the file and the word counter
bookwriter('Assignment/result.txt', word_counts)  # Write the sorted word counts to a file

# Output the sorted word counts to the terminal
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    print(f'{word} {count}')

   
