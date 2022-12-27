"""#endswith()
s="Hello welcome to python class!"
a=s.endswith('!')
print(a)"""

#find()-it return the index the firdt char index if not match it return -1
s="Hello welcome to python class for practice python programs"
a=s.find("python",23,len(s)-1)#we have given specific instructions for indexing
print(a)
a=s.rfind("python")
print(a)
