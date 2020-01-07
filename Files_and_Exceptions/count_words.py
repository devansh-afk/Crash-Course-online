def count_words(filename):
    """Counts the number of words ini a text file"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'The file {filename} does not exist')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has {num_words} number of words')


count_words('text_files/alice.txt')
count_words('alice2.txt')
FileNames = ['alice2.txt', 'random.txt', 'text_files/alice.txt']
for i in FileNames:
    count_words(i)
