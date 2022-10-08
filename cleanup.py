

def removeSpaces(filepath, filename):
    with open(filepath) as infile, open(f'BackupOutput/{filename}_Staged.txt', 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty line. Write it to output
