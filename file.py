list_file = ['1.txt', '2.txt', '3.txt']
list_str = []
for file in list_file:
    with open(file, encoding='utf') as text:
        line_ = 0
        for l in text:
            if l == '':
                pass
            else:
                line_ += 1
        list_str.append(line_)
print('list:', list_file, type(list_file))
print('list_str:', list_str, type(list_str))
list_file_str = list(zip(list_file, list_str))
sorted_list = sorted(list_file_str, key=lambda x: x[1])
print('sorted_list', sorted_list)
list_file, list_file_str = zip(*sorted_list)
list_file = list(list_file)
print('list_file:', list_file, type(list_file))
print('list_str:', list_str, type(list_str))
record = open('result_file.txt','a')
for file,str_ in sorted_list:
    file_name = file
    print(file_name, type(file_name))
    str_len = str(str_)
    print(str_len, type(str_len))
    record.write(file_name)
    record.write(' \n')
    record.write(str_len)
    record.write(' \n')
    with open(file, encoding='utf') as text_for_write:
        data = text_for_write.read()
        print(data)
        record.write(data)
        record.write(' \n')
record.close()