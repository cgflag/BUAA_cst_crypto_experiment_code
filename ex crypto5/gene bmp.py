import struct

# 打开 BMP 文件（假设文件名为 image.bmp）
'''with open('image.bmp', 'rb') as bmp_file:
    # 读取 BMP 文件头（前 54 个字节）
    bmp_header = bmp_file.read(54)

    # 解析 BMP 文件头信息
    width, height = struct.unpack("<ii", bmp_header[18:26])  # 从字节 18 到 25 取出宽度和高度
    bpp = struct.unpack("<h", bmp_header[28:30])[0]  # 从字节 28 到 29 取出每像素位数

    # 读取 BMP 文件中剩余的像素数据
    bmp_data = bmp_file.read()'''
'''with open('bmp_header.txt', 'rb') as bmp_file:
    header = bmp_file.read(54)
    width, height = struct.unpack("<ii", header[18:26])  # 从字节 18 到 25 取出宽度和高度
    bpp = struct.unpack("<h", header[28:30])[0]  # 从字节 28 到 29 取出每像素位数



with open("output_ECB.txt", 'rb') as file:
    bmp_data = file.read()
# 将像素数据写入新的 BMP 文件中
with open('restored_ECB.bmp', 'wb') as bmp_file:
    # 写入 BMP 文件头
    bmp_file.write(header)

    # 写入像素数据
    bmp_file.write(bmp_data)'''


'''def write_bmp_file(file_path, width, height, color_depth, pixel_data):
    # 计算文件大小
    file_size = 54 + len(pixel_data)
    # 构造文件头
    file_header = struct.pack('<cciiii', b'B', b'M', file_size, 0, 54, 40)
    # 构造信息头
    info_header = struct.pack('<iiiHHiiiiii', 40, width, height, 1, color_depth, 0, len(pixel_data), 0, 0, 0, 0)
    # 写入文件头和信息头
    with open(file_path, 'wb') as f:
        f.write(file_header)
        f.write(info_header)
        # 写入像素数据
        f.write(pixel_data)

if __name__ == '__main__':
    width = 100
    height = 100
    color_depth = 24
    pixel_data = b'\xff\x00\x00' * (width * height)
    file_path = 'test.bmp'
    write_bmp_file(file_path, width, height, color_depth, pixel_data)'''
from PIL import Image
import binascii
import struct

# 读取十六进制字节串（假设字节串保存在 image_hex.txt 文件中）
with open('bmp_header.txt', 'r') as f:
    hex_data = f.read()
#with open('output.txt', 'r') as f:
#with open('output_ECB.txt', 'r') as f:
with open('output_CBC.txt', 'r') as f:
    hex_data += f.read()

bmp_data = bytes.fromhex(hex_data)

# 解析BMP文件头
header = struct.unpack('<2sI4H2I2L', bmp_data[:30])
width = header[6]
height = header[7]
pixel_offset = header[9]

# 创建一个PIL（Python Imaging Library）的Image对象，并设置其大小和模式
img = Image.new('RGB', (width, height), color='white')

# 写入BMP文件头
img_file = open('output.bmp', 'wb')
img_file.write(bmp_data[:pixel_offset])

# 将字节串写入图像文件
img.putdata([(bmp_data[i+2], bmp_data[i+1], bmp_data[i]) for i in range(pixel_offset, len(bmp_data), 3)])

# 保存图像文件
img.save(img_file, 'BMP')

# 关闭文件流
img_file.close()