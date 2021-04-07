import struct

def f31(_data_):
    data = _data_.split(b'\x00\x57\x50\x5a\x42')[1]
    print(data)
    result = {}


    sA = struct.unpack(">fQIhIdHHHHhIH", data[0: 46])
    sB = sA[1:6]
    sC = struct.unpack(">dI3sfdH", data[sB[1] - 3: sB[1] + 26])
    sD1 = struct.unpack(">iHIb", data[sA[6] - 3: sA[6] + 8])
    sD2 = struct.unpack(">iHIb", data[sA[7] - 3: sA[7] + 8])
    sD3 = struct.unpack(">iHIb", data[sA[8] - 3: sA[8] + 8])
    sD4 = struct.unpack(">iHIb", data[sA[9] - 3: sA[9] + 8])

    result['A1'] = sA[0]
    result['A2'] = {'B1': sB[0], 'B2': {'C1': sC[0], 'C2': sC[1], 'C3': sC[2].decode(), 'C4': sC[3], 'C5': sC[4], 'C6': sC[5]}, 'B3': sB[2], 'B4': sB[3], 'B5': sB[4]}
    result['A3'] = [{'D1': sD1[0], 'D2': list(struct.unpack(">" + str(sD1[1]) + "b", data[sD1[2] - 3: (sD1[2] + sD1[1]) - 3])), 'D3': sD1[3]},
    {'D1': sD2[0], 'D2': list(struct.unpack(">" + str(sD2[1]) + "b", data[sD2[2] - 3: (sD2[2] + sD2[1]) - 3])), 'D3': sD2[3]},
    {'D1': sD3[0], 'D2': list(struct.unpack(">" + str(sD3[1]) + "b", data[sD3[2] - 3: (sD3[2] + sD3[1]) - 3])), 'D3': sD3[3]},
    {'D1': sD4[0], 'D2': list(struct.unpack(">" + str(sD4[1]) + "b", data[sD4[2] - 3: (sD4[2] + sD4[1]) - 3])), 'D3': sD4[3]}]
    result['A4'] = sA[10]
    result['A5'] = list(struct.unpack(">" + str(sA[11]) + "h", data[sA[12] - 3: (sA[12] + sA[11] * 2) - 3]))

    return result
    
    
    


dt = (b'\x00WPZB\x005\x00:\x00?\x00D\x00I\x00N\x00S\xab\x04uwsjgv\xf8-\xe6~\x00'b'\x00\x00\x02\x00\x00\x00X\x00\x00\x00\x02\x00\x00\x00Z\x00j\x00\x00\x00'b'{\xbe\xa2+\xa1n?6T\x1e\x96?\x1b\x92\x85\x88<\x85(\xd5l\xbe\x1f\xe4\x80G\xbf|'b'\xeb\xde\xfd\xbe\x8bp\xb0~\xe4D?\xa9\x19\rI\xfbw\xc0?\xc5\x12F\x1ew'b'\xef\xf0\x8b~_Q\xd3\xc1\xc2\\_V"\xb1\x1cj\x81\x8f\xe2\x00\x00\x00\x07\x00'b'\x00\x00mN\xc0\xda\xc5l')
print(f31(dt))
#dt = (b'PXJ?\x00h\xb4\xe0\x1b\xe0R\x84\x9c?V\x00\x00\x001;\x9d\x94\xe0\x88'b'\x87?\xc8\x91f\xb1u\x1a\x88\x00P\x00]\x00j\x00w\x8c\x00\x00\x00\x00\x05\x00'b'\x82\xbf\xe5?uT\xb4\xd6j\xc3\xb2L\tpkf>\x8al{\xbf\xac\xfa\xa9\xb9gW@D2G:'b'f(\xddG\x00\x02\x00\x00\x00N\x97\xef\xc4\xbaC\xb4]\x00\x02\x00\x00\x00[\xf1'b'\x87\xcc\xa6kj\xf4\x00\x02\x00\x00\x00hp-\x8a\x85p\xb0A\x00\x02\x00\x00\x00'b'u\xc4\x98\x03\xd6\x89\x159\xe9\xd5?\xf8')
#print(f31(dt))

#o = C32()
#print(o.race())
#print(o.mask())
#print(o.mask())
#print(o.race())
#print(o.mask())
#print(o.race())
#print(o.race())
#print(o.mask())
#print(o.mask())
#print(o.move())
#print(o.mask())
#print(o.mask())

#o = C32()
#print(o.race())
#print(o.mask())
#print(o.move())
#print(o.mask())
#try:
#    print(o.move())
#except RuntimeError:
#    print('RuntimeError')
#print(o.mask())
#print(o.race())
#print(o.race())
#print(o.mask())
#print(o.mask())
#print(o.move())
#print(o.mask())
#print(o.mask())