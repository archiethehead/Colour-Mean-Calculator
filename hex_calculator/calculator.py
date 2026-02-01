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

    R = str(hex(mean(R)))[2:]
    G = str(hex(mean(G)))[2:]
    B = str(hex(mean(B)))[2:]
    

    # Integers with trailing zeros have them removed, but there are needed for hex codes.
    # This verificaiton checks for this and ammends it if necessary.

    RGB_list = [R, G, B]
    zero = "0"

    for x in range(3):
        if len(RGB_list[x]) == 1:
            RGB_list[x] = zero + RGB_list[x]

    mean_hex = RGB_list[0] + RGB_list[1] + RGB_list[2]
    return mean_hex