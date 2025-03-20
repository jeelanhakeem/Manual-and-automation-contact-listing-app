import re

text="Hi Good Afternoon and  I am Jeelu and  i have completed B.tech"
x=re.search("\\s",text)
print("The first white-space character is located in position:",x.start())
