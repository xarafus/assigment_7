find_words = []
file_path = r'C:\Users\user\Downloads\romeo.txt'
with open(file_path, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word not in find_words:
                find_words.append(word)
find_words.sort()
print(find_words)
