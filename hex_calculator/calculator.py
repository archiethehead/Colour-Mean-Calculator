def mean(numbers: list[int]) -> int:

    return round(sum(numbers) / len(numbers))

def hex_to_RGB(hex_codes: list[int]) -> list[int]:

    R = []
    G = []
    B = []

    try:
        for code in hex_codes:
            R.append(int(code[:2], 16))
            G.append(int(code[2:4], 16))
            B.append(int(code[4:6], 16))
        
        return R, G, B
    
    except:
        raise ValueError

def hex_mean(hex_codes: list[int]) -> str:

    R, G, B = hex_to_RGB(hex_codes)

    R = str(hex(mean(R)))
    G = str(hex(mean(G)))
    B = str(hex(mean(B)))

    mean_hex = R[2:] + G[2:] + B[2:]
    return mean_hex