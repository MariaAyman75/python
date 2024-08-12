def read(filepath, option):
    
    try:
        file = open(filepath, 'r')
        if option == 'all':
            return file.read()
        elif option.isdigit():
            return file.read(int(option))
        elif option == 'line':
            return file.readline()
        elif option == 'lines':
            return file.readlines()
        else:
            return "Invalid option"
    except FileNotFoundError:
        return "File not found"

def write(filepath, content):
   
    if not isinstance(content, (str, list)):
        return "Invalid content type"
    
    try:
        file = open(filepath, 'w')
        if isinstance(content, str):
            file.write(content)
        elif isinstance(content, list):
            file.writelines(content)
    except Exception as e:
        return f"An error occurred: {e}"
    

def append(filepath, newcontent):
    
    if not isinstance(newcontent, (str, list)):
        return "Invalid content type"
    
    try:
        file = open(filepath, 'a')
        if isinstance(newcontent, str):
            file.write(newcontent)
        elif isinstance(newcontent, list):
            file.writelines(newcontent)
    except Exception as e:
        return f"An error occurred: {e}"
   
