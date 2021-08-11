filename = 'text_files/gutenberg_text.txt'

try:
    with open(filename) as file_object:
        content = file_object.read()
except FileNotFoundError:
    pass
else:
    count = content.count('the ')
    print(count)
    
