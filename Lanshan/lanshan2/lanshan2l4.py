file_path = 'input.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    while line := f.readline():
        print(line)