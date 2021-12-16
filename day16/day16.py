#!/usr/bin/env python3


from math import prod


bitmap = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


class Packet:

    def __init__(self, version, type_id, value):
        self.version = version
        self.type_id = type_id
        self.__value = value

    def __str__(self):
        return f'Version: {self.version} - Type: {self.type_id} - Value: {self.value}'

    @property
    def value(self):
        return int(self.__value, 2)
    

class Operator(Packet):

    def __init__(self, version, type_id, subpackets):
        super().__init__(version, type_id, None)
        self.subpackets = subpackets

    @property
    def value(self):
        if self.type_id == '000':
            return sum(p.value for p in self.subpackets)
        elif self.type_id == '001':
            return prod(p.value for p in self.subpackets)
        elif self.type_id == '010':
            return min(p.value for p in self.subpackets)
        elif self.type_id == '011':
            return max(p.value for p in self.subpackets)
        elif self.type_id == '101':
            assert len(self.subpackets) == 2
            return self.subpackets[0].value > self.subpackets[1].value
        elif self.type_id == '110':
            assert len(self.subpackets) == 2
            return self.subpackets[0].value < self.subpackets[1].value
        elif self.type_id == '111':
            assert len(self.subpackets) == 2
            return self.subpackets[0].value == self.subpackets[1].value


def read_packet(bits, index, packets):
    if bits[index:].count('0') == len(bits[index:]):
        return index + len(bits[index:])
    version = bits[index:index+3]
    type_id = bits[index+3:index+6]
    index += 6
    if int(type_id, 2) == 4:
        value = ''
        while True:
            group = bits[index:index+5]
            value += group[1:]
            index += 5
            if group[0] == '0':
                break
        packets.append(Packet(version, type_id, value))
    else:
        subpackets = []
        length_type_id = bits[index]
        if length_type_id == '0':
            length_of_subpackets = int(bits[index+1:index+16], 2)
            index += 16
            i = index
            while index < i + length_of_subpackets:
                index = read_packet(bits, index, subpackets)
        elif length_type_id == '1':
            nr_of_subpackets = int(bits[index+1:index+12], 2)
            index += 12
            for i in range(nr_of_subpackets):
                index = read_packet(bits, index, subpackets)
        packets.append(Operator(version, type_id, subpackets))
    return index


def sum_versions(packets):
    v = 0
    for packet in packets:
        v += int(packet.version, 2)
        if packet.type_id != '100':
            v += sum_versions(packet.subpackets)
    return v


def run():
    with open('input.txt') as fh:
        bits = ''.join(bitmap[h] for h in fh.read())

    packets = []
    i = 0
    while i < len(bits):
        i = read_packet(bits, i, packets)

    print(sum_versions(packets))  # first answer
    print(packets[0].value)  # second answer


if __name__ == '__main__':
    run()
