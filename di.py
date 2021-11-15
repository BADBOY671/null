import dis
import marshal
f = open("file.pyc","rb")
f.seek(8) #assuming there are magic numbers at the beginning
code = marshal.load(f)
dis.dis(code)
