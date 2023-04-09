# file_obj=open('test.txt','rt',encoding='utf-8')
# file_obj2=open('test2.txt','wt',encoding='utf-8')
# file_obj2.write(file_obj.read())

# #close file

# file_obj.close()
# file_obj2.close()


#模拟登录
# user=input('Enter your name:')
# pwd=input('Enter your password:')
# data='{}:{}----\n'.format(user,pwd)
# file_obj3=open('infos/user.txt','at',encoding='utf-8')
# file_obj3.write(data)
# file_obj3.close()

#read and write
#r和w的光标在开头，a的光标在结尾
# file_obj=open('test.txt','rt+',encoding='utf-8')
# contentpre=file_obj.read()
# print(contentpre)
# file_obj.write('\n this is a new line')
# file_obj.close()

#flush()方法是强制刷新缓冲区，把缓冲区的内容写入文件

#with语句是自动关闭文件

with open('test.txt','rt',encoding='utf-8') as file_obj,open('test2.txt','wt',encoding='utf-8') as file_obj2:
    content=file_obj.read()
    print(content)
