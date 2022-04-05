poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)

# The file was opened in read mode but we wanted to write to it so had to change the mode to w.
