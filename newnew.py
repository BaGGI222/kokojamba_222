# class MyFile():
#     def __init__(self, filename, mode, encoding):
#         self.filename = filename
#         self.mode = mode
#         self.encoding = encoding
        

#         def __enter__(self):
#             self.file = open(self.filename, self.mode, self.encoding)
#             return self.file
        
#         def __exit__(self, exc_type, exc_val, exc_tb):
#             self.file.close()


# with MyFile('1.txt', 'nameis', encoding = 'utf-8') as file:
#     content = file.read()  
#     print(content)

class iterator: 
    def __init__(self, start): 
        self.start = start 
 
    def __iter__(self): 
        return self 
 
    def __next__(self): 
        self.start += 1 
        return self.start - 1
    
one_iterator = iterator(0)
for i in one_iterator:
    print(i)
    