import struct
import os
 
# 拼音表偏移，
startPy = 0x1540
 
# 汉语词组表偏移
startChinese = 0x2628

GTable = []

def byte2str(data):
    pos = 0
    str = ''
    while pos < len(data):
        c = chr(struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0])
        if c != chr(0):
            str += c
        pos += 2
    return str

def getChinese(data):
    pos = 0
    while pos < len(data):
        same = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
        pos += 2
        py_table_len = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
        pos += 2
        pos += py_table_len
        for i in range(same):
            c_len = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
            pos += 2
            word = byte2str(data[pos: pos + c_len])
            pos += c_len
            ext_len = struct.unpack('H', bytes([data[pos], data[pos + 1]]))[0]
            pos += 2
            if len(word)==4:
                GTable.append((word))
            pos += ext_len
 
def scel2txt(file_name):
    print('-' * 60)
    with open(file_name, 'rb') as f:
        data = f.read()
    print("词库名：", byte2str(data[0x130:0x338])) # .encode('GB18030')
    print("词库类型：", byte2str(data[0x338:0x540]))
    print("描述信息：", byte2str(data[0x540:0xd40]))
    print("词库示例：", byte2str(data[0xd40:startPy]))
    getChinese(data[startChinese:])
 
if __name__ == '__main__':
    scel2txt('生活常用成语大全.scel')
    f = open('成语.txt', 'w',encoding='UTF-8-SIG')
    cnt=0
    for word in GTable:
        f.write(str(cnt)+','+word+'\n')
        cnt+=1
    f.close()