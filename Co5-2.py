#Program to copy odd Lines of one file to another.
#Opening files for reading and writing data

input_file=open('Data1.txt')
output_file=open('WriteData.txt','w')

#Coping/reading contnts from read_file to copy_data

copy_data=input_file.readlines()
print("Actual File Content is")
print(copy_data,"\n")

for i in range(0,len(copy_data)):
    if i % 2==0:
        output_file.write(copy_data[i])
    else:
        pass

#Closing file after writing

output_file.close()

#Opening write file in read mode and printing value

output_file=open('WriteData.txt','r')
print("ODD lINES ARE:")
print(output_file.read())

#Closing Files
input_file.close()
output_file.close()

