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