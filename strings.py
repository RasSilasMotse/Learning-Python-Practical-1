#advanced concepts - strings

message = ' Hello World, world is Python! '

print(message.strip())#Remove leading and trailing whitespace
print(message.lower())#Convert characters to lowercase
print(message.split(','))#split the string into a list on the comma
print(message.upper())#convert characters ton uppercase
message= "Hello world,world is Python"
print(message.replace("world" ,"earth")) #replace all occurences 
print(message.replace("world" ,"earth", 2)) #replace the first occurences
