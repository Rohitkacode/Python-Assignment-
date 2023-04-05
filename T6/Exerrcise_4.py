
input_string = 'Consultadd Training' 

def gen(string):
    rs = string[::-1]
    yield rs 


result = "".join([i for i in gen(input_string)])  
print(result)