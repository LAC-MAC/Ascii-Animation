import os, subprocess, re

files = os.listdir('/Users/lachlanmackay/Desktop/animate/test/')

files.remove(".DS_Store")
#files.sort(key=lambda f: int(re.sub('/Users/lachlanmackay/Desktop/animate/jm', '', f)))
files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))



        
print(files)




for i in range(0, len(files)):
    bashCommand = "jp2a " + str(files[i])
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, cwd="/Users/lachlanmackay/Desktop/animate/test/")
    output, error = process.communicate()

    print(str(output, "utf-8"))

    filename = "rrAscii/asciiFrame" + str(i) + ".txt"
    text_file = open(filename, "w")
    n = text_file.write(str(output, "utf-8"))
    text_file.close()