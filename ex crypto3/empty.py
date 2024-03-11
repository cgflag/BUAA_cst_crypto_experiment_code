#print('{:#x}'.format(1454423413))
#weak = ['0x0101010101010101', '0xFEFEFEFEFEFEFEFE', '0xE0E0E0E0F1F1F1F1', '0x1F1F1F1F0E0E0E0E', '0x0000000000000000'
#        ,'0xFFFFFFFFFFFFFFFF','0xE1E1E1E1F0F0F0F0',  '0x1E1E1E1E0F0F0F0F']
'''weak = ['0x0101010101010101', '0x1F1F1F1F0E0E0E0E', '0xE0E0E0E0F1F1F1F1', '0xFEFEFEFEFEFEFEFE', '0x0000000000000000', '0xFFFFFFFFFFFFFFFF', '0xE1E1E1E1F0F0F0F0', '0x1E1E1E1E0F0F0F0F']
for i in range(0, len(weak)):
    print(weak[i])
semi_weak = ["0x011F011F010E010E", '0x1F011F010E010E01', '0x01E001E001F101F1', '0xE001E001F101F101',
             '0x01FE01FE01FE01FE', '0xFE01FE01FE01FE01', '0x1FE01FE00EF10EF1', '0xE01FE01FF10EF10E',
             '0x1FFE1FFE0EFE0EFE', '0xFE1FFE1FFE0EFE0E', '0xE0FEE0FEF1FEF1FE', '0xFEE0FEE0FEF1FEF1',
             '0x001E001E000F000F', '0x1E001E000F000F00', '0x00E100E100F000F0', '0xE100E100F000F000',
             '0x00FF00FF00FF00FF', '0xFF00FF00FF00FF00', '0x1EE11EE10FF00FF0', '0xE11EE11EF00FF00F',
             '0x1EFF1EFF0FFF0FFF', '0xFF1EFF1EFF0FFF0F', '0xE1FFE1FFF0FFF0FF', '0xFFE1FFE1FFF0FFF0']
#一个点不小心弄错了
for i in range(0, 12):
    print(semi_weak[2*i]+' '+semi_weak[2*i+1])
'''


def compress(self, path):
    filename, file_extension = os.path.splitext(path)
    output_path = filename + ".bin"

    with open(path, 'r+') as file, open(output_path, 'wb') as output:
        text = file.read().rstrip()

        if len(text) == 0:
            print("File is empty")
            return

        frequency = self.make_frequency_dict(text)
        heap = self.make_heap(frequency)
        self.make_codes(heap)

        encoded_text = self.get_encoded_text(text)
        padded_encoded_text = self.pad_encoded_text(encoded_text)

        b = self.get_byte_array(padded_encoded_text)
        output.write(bytes(b))

    print("Compressed")
    return output_path


def decompress(self, input_path):
    filename, file_extension = os.path.splitext(input_path)
    output_path = filename + "_decompressed.txt"

    with open(input_path, 'rb') as file, open(output_path, 'w') as output:
        bit_string = ""

        byte = file.read(1)
        while len(byte) > 0:
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)
            decoded_text = self.decode_text(encoded_text)

            output.write(decoded_text)

        print("Decompressed")
        return output_path
