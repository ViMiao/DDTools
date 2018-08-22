
import os, sys


def mainjssRead(mainjssPath):
    print('Path Type is:' + str(type(mainjssPath)))
    
    mainjssOut = open(mainjssPath)
    
    try:
        for line in mainjssOut:
            print(line)
    finally:
        mainjssOut.close()

def dataExtracrion(CalPath):
    #提取计算数据并输出
    resultPath = os.path.join(CalPath, '设计结果\\')
    mainjssPath = os.path.join(resultPath, 'mainjss.txt')
    print(mainjssPath)
    mainjssRead(mainjssPath)


def projectCalPathJudgment(theNewPath):
    #文件路径判断，如果是文件夹路径则直接输出文件夹路径；如果是文件路径则去除文件名后直接输出文件路径
    if os.path.isfile(theNewPath):
        theNewPath = os.path.dirname(os.path.abspath(theNewPath))
        return(theNewPath+"\\")
    elif os.path.isdir(theNewPath):
        return(theNewPath)
    else:
        print("文件夹或文件路径错误，请重新输入！")
        return False

def main():
    
    filePath = 'D:\\Cal-Temp\\Analysis-博物馆-上部计算-1.7.1.0\\'
    print('filePath type is: ' + str(type(filePath)))
    # f = open(filePath)
    # for txt in f.readlines():
    #     print(txt)
    # f.close()
    
    # while True:
    #     projectCalPath = input("请拖拽或输入计算文件夹或文件路径：>>")
    #     projectCalPath = projectCalPathJudgment(projectCalPath)
    #     if projectCalPath == "exit":
    #         break
    #     elif projectCalPath:
    #         dataExtracrion(projectCalPath)
    # exit
    dataExtracrion(filePath)
        
            
if __name__=="__main__":
    main()
