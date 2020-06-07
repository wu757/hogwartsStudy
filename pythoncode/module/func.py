def have_parameter(para):
    print(f"输出参数: {para}")

def no_parameter():
    print("无参数")

def have_return(value):
    print("这函数有返回值: ")
    return value

def no_retrun():
    print("无return时默认返回：None")

if __name__ == '__main__':
    no_parameter()