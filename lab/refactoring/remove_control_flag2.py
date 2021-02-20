# by Kami Bigdely
# Remove control flag
# Reference: https://stackoverflow.com/a/10140333/81306
# This code snippet reads up to the end of the file
  
n = 16
file = 'foobar.file'

def readfile(file, n):
    with open(file, 'rb') as fp:
        chunk = fp.read(n)
        if chunk == '': # end of file, stop running.
            return
        print(chunk)
        # process(chunk)

readfile(file, n)