
def save_file(boy, girl, count):
    
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_gile = 'girl_' + str(count) + '.txt'
        
    boy_file = open(file_name, 'w')
    girl_file = open(file_name, 'w')
        
    boy_file.writeline(boy)
    girl_file.writeline(girl)    
    
    boy_file.close()
    girl_file.close()

def split_file(file_name):  
    f = open('record.txt')
    
    boy = []
    girl = []
    count = 1
    
    for each_line in f:
        if each_line[:6] != '=====':
            (role, line_spoken) = each_line.split(':', 1)
            if role == 'A':
                boy.append(line_spoken)
            elif role == 'B':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)
            
            boy = []
            girl = []
            count += 1
    
    save_file(boy, girl, count)
    
    f.close()
    
split_file('record.txt')