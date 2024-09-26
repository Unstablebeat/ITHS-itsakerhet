file = open("log.txt", 'r')
line = file.readline()
search_string = "Failed login attempt"
result = []
while line:
    if search_string in line:
        result.append(line.strip())
    line = file.readline()

for index, attempt in enumerate(result):
    print(index, attempt)

