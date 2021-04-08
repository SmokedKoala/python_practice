import struct, pprint

def f31(_data_):
    data = _data_.split(b'\x00\x57\x50\x5a\x42')[1]
    print(data)
    result = {}


    sA = struct.unpack(">8H6s2HIIIIHI", data[0: 48])
    sC = sA[8:16]
    sE = struct.unpack(">IIic", data[sA[16]-13: sA[16]])
    sD = struct.unpack(">hc", data[sC[-1] - 5 : sC[-1] - 2])
    sB1 = struct.unpack(">fB", data[sA[0] -5 : sA[0] ])
    sB2 = struct.unpack(">fB", data[sA[1] -5 : sA[1] ])
    sB3 = struct.unpack(">fB", data[sA[2] -5 : sA[2] ])
    sB4 = struct.unpack(">fB", data[sA[3] -5 : sA[3] ])
    sB5 = struct.unpack(">fB", data[sA[4] -5 : sA[4] ])
    sB6 = struct.unpack(">fB", data[sA[5] -5 : sA[5] ])
    sB7 = struct.unpack(">fB", data[sA[6] -5 : sA[6] ])

    result['A1'] = [{'B1': sB1[0], 'B2': sB1[1]}, {'B1': sB2[0], 'B2': sB2[1]}, {'B1': sB3[0], 'B2': sB3[1]}, {'B1': sB4[0], 'B2': sB4[1]}, 
        {'B1': sB5[0], 'B2': sB5[1]}, {'B1': sB6[0], 'B2': sB6[1]}, {'B1': sB7[0], 'B2': sB7[1]}]
    result['A2'] = sA[7]

    byte_list = list(struct.unpack(">" + str(sC[3]) + "c", data[sC[4] : (sC[4] + sC[3])]))
    for el in range(0,len(byte_list)):
        byte_list[el] = ord(byte_list[el])

    result['A3'] = {'C1': sC[0].decode(), 'C2': sC[1], 'C3': sC[2], 
        'C4': byte_list,
        'C5': list(struct.unpack(">" + str(sC[5]) + "d", data[   sC[6]-5 : (sC[6] + sC[5]*8)-5  ])),
        'C6': {'D1':sD[0], 'D2':ord(sD[1])}}

    result['A4'] = {
        'E1': ">" + str(sE[0]) + "H",
        # 'E1':list(struct.unpack(">" + str(sE[0]) + "H", data[sE[1] : (sE[1] + sE[0]) ])),
        'E2':sE[2],
        'E3':ord(sE[3])}

    # for i in range(-50,1):
    #     S = struct.unpack(">IIic", data[sA[16]+i-13: sA[16]+i])
        # for el in range(0,len(S)):
        #     S[el] = ord(S[el])
        # print(i," ",S)

    return result
    
    
    


dt = (b'\x00WPZB\x005\x00:\x00?\x00D\x00I\x00N\x00S\xab\x04uwsjgv\xf8-\xe6~\x00'b'\x00\x00\x02\x00\x00\x00X\x00\x00\x00\x02\x00\x00\x00Z\x00j\x00\x00\x00'b'{\xbe\xa2+\xa1n?6T\x1e\x96?\x1b\x92\x85\x88<\x85(\xd5l\xbe\x1f\xe4\x80G\xbf|'b'\xeb\xde\xfd\xbe\x8bp\xb0~\xe4D?\xa9\x19\rI\xfbw\xc0?\xc5\x12F\x1ew'b'\xef\xf0\x8b~_Q\xd3\xc1\xc2\\_V"\xb1\x1cj\x81\x8f\xe2\x00\x00\x00\x07\x00'b'\x00\x00mN\xc0\xda\xc5l')
pprint.pprint(f31(dt))
