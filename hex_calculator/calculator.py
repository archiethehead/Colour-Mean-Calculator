def mean(numbers: list[int]) -> int:

    """Returns the mean of the given list of nums.
    
        Args:
           numbers(list[int]): Each R, G, or B value in the form of an integer.
    
        Returns:
            int: The mean of every integer.
    
        Raises:
            ZeroDivisionError: When the list doesn't contain any elements.
    
        Examples:
            >>> mean(1,2)
            2
        """

    try:
        return abs(round(sum(numbers) / len(numbers)))
    
    except:
        raise ZeroDivisionError

def find_complementary(hex_code: str) -> str:

    """Returns the mathematical complementary of a given hex code.
    
        Args:
           hex_code(str): Each R, G, or B value in the form of a string.
    
        Returns:
            str: The complementary of the given hex code in the form of a string.
    
        Raises:
            N/A
    
        Examples:
            >>> find_complementary(F192AB)
            0e6d54
        """

    R, G, B = hex_to_RGB([hex_code])
    R = 255 - R[0]
    G = 255 - G[0]
    B = 255 - B[0]

    return stringify_hex(R, G, B)

def hex_to_RGB(hex_codes: list[str]) -> list[int]:

    """Returns the constituent RGB values of a hex colour code in the form of three string lists.
    
        Args:
           hex_codes(list[str]): Each hex-code entered by the user in the form of a string.
    
        Returns:
            list[int]: R, G, and B in the form of integer lists.
    
        Raises:
            ValueError: When any of the given list values isn't a string.
    
        Examples:
            >>> hex_to_RGB(['004b9d','202f55'])
            [0, 32], [75, 47], [157, 85]
        """

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

def stringify_hex(R: int, G: int, B: int) -> str:
    
    """Returns a given set of RGB values as a single string.
    
        Args:
           R(int)
           G(int)
           B(int)
    
        Returns:
            str: The RGB values as a complete hex string
    
        Raises:
            N/A
    
        Examples:
            >>> find_complementary(0x0, 0xFF, 0XFF)
            00FFFF
        """

    # Integers with trailing zeros have them removed, but there are needed for hex codes.
    # This verificaiton checks for this and ammends it if necessary.

    R = str(hex((R)))[2:]
    G = str(hex((G)))[2:]
    B = str(hex((B)))[2:]
    
    RGB_list = [R, G, B]
    zero = "0"

    for x in range(3):
        if len(RGB_list[x]) == 1:
            RGB_list[x] = zero + RGB_list[x]

    mean_hex = RGB_list[0] + RGB_list[1] + RGB_list[2]

    return mean_hex

def hex_mean(hex_codes: list[str]) -> str:

    """Returns the mean vaulue of a given array of hex colour codes as a string.
    
        Args:
           hex_codes(list[str]): Each hex colour code in the form of a string.
    
        Returns:
            str: The mean value of every hex code in the form of a string.
    
        Raises:
            TypeError: When hex_codes isn't a list.
    
        Examples:
            >>> calculator.hex_mean(
            ["004b9d",
            "202f55",
            "13c2f0",
            "003882",
            "2472ce",
            "0d2b60",
            "123576"])

            '115393'
        """

    try:
        if len(hex_codes) == 0:
            return "000000"
    
    except:
        raise TypeError

    R, G, B = hex_to_RGB(hex_codes)

    R, G, B = mean(R), mean(G), mean(B)

    mean_hex = stringify_hex(R, G, B)

    return mean_hex