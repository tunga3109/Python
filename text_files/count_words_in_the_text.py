def count(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f'Sorry {filename} does not exist!')   

    else:
        words = content.split()
        num_words = len(words)
        print(f'The file {filename} has about {num_words} words.')

filename = ['text_files/alice.txt','text_files/text.txt','text_files/asd.txt']
for name in filename:
    count(name)

