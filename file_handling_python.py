'''x will create new file if alredy exists it will throe an error like --FileExistsError'''

# f1=open('file1.text','x')
# f1=open('file2.text','x')
# f1=open('range.py','x') #FileExistsError
# f2= open('file2.py','w')
# f2.write('w--> write command use to create and write the content \n#if file already exists it will delete the content and add the new content in it')
# f2.close()

# f2=open('file2.py','a')
# f2.write('\n#a--> used to append(add) the content to the existed file \n# if file file not existed it create the file add the content to it ')
# f2.close()

# f2=open('file2.py','a')
# f2.write('#x--> is used to create the new file if file name already exists  it will throw an error\n#r--> only if file exists, it  read the content in the file else it will throw an error--filenotfound')
# f2.close()
# f3=open('range.py','r')
# print(f3.read())

'''to get path of the file import os and use getcwd-current working directory '''
# import os
# print(os.getcwd())#PS C:\Users\JOSH\Documents\desktop\goutham> 

'''to check the file exists or not it gives in True or False'''
# import os
# print(os.path.exists('file1.text'))#True

'''to delete existed files'''
#import os
# os.remove('file1.text')
# os.remove('file2.py')

'''it will print total content of the file in terminal window it is also print programm '''
# f4=open("file2.text",'r')
# f4=open('number_system.py','r')
# print(f4.read())

'''using readline we can print the required characters'''
# print(f4.readline(4))# a=
# print(f4.readline(10))# a=0.7 sd

'''to print total content in the form of list use readlines'''
# f5=open('file2.text','r')
# print(f5.readlines())
#output is content in file2.text file in the form of list
