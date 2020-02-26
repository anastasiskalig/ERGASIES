with open('file.txt','r') as f:
  for line in f:
    for word in line.split():
      if len(word) > 3:
        print (word[1:] +word[0]+ "ay")

        
