# Read a file word by word
# open the text file
with open('testfile2.txt','r') as file:
    # read each line    
    for line in file:
        # read each word        
        for word in line.split():
            # display the words           
            print(word) 