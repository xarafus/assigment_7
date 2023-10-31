senders = []
line_count = 0
file_path = r'C:\Users\user\Downloads\mbox.txt'
with open(file_path, 'r') as file:
    for line in file:
        if line.startswith("From "):
            sender = line.split()[1]
            print(sender)
            senders.append(sender)
            line_count += 1
print(f"Total {line_count} lines were printed.")
