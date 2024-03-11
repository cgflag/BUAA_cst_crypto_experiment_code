# 打开BMP文件并读取文件头和图像信息头
import binascii

# 打开BMP文件并读取文件头和图像信息头
with open('pic_original.bmp', 'rb') as file:
    header = file.read(54) # 读取bmp文件头部54个字节
    '''for byte in header:
        str_byte = hex(byte)[2:]
        while len(str_byte) < 2:
            str_byte = '0' + str_byte
        print('0x'+str_byte)'''
    hex_header = [hex(byte)[2:].zfill(2) for byte in header]
    out_header = ''.join(hex_header)
    content = file.read()
    #bmp_bytes = binascii.hexlify(file.read())
    #bmp_bytes = binascii.hexlify(content.encode('utf-8'))
    bmp_bytes = [hex(byte)[2:].zfill(2) for byte in content]
    out_bmp_bytes = ''.join(bmp_bytes)
with open('bmp_header.txt', 'w') as output_file1:
    # 将后面的内容每个字节转化为16进制输出
    output_file1.write(str(out_header))
with open('output.txt', 'w') as output_file2:
    output_file2.write(str(out_bmp_bytes))
