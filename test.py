# with open("test.txt",'r') as file:
#     print('打开文件')
#     data = file.read()
#     print(data)
#
#     print(help(file))



# class Sample:
#     def __enter__(self):
#         print("In __enter__()")
#         return "Foo"
#     def __exit__(self, type, value, trace):
#         print("In __exit__()")
#
#     def get_sample(self):
#         return Sample()
#
#     with get_sample() as sample:
#         print("sample:", sample)

# def createGenerator():
#     mylist = range(3)
#     for i in mylist:
#        yield i
#        yield i*i
# mygenerator = createGenerator() # create a generator
# print(mygenerator) # mygenerator is an object!
# for j in mygenerator:
#     print(j)
#
# print(createGenerator())


