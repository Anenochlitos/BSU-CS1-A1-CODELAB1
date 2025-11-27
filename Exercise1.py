word1 = 'Coding' 
word2 = 'is'
word3 = 'cool'

'''I'm creating variables'''

sentence = (word1 + " " + word2 + " " + \
     word3)  #This is a comment for the line continuation item

sentence2 = (f'{word1} {word2} {word3}') #I'm using an f-string to not have to use the + operator 
print(sentence2)
print(sentence)

'''I printed the output twice to showcase that different methods can achieve the same result'''
