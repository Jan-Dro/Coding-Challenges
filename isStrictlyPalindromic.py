def isStrictlyPalodromic(num):
        index = 2
        while index < num:
            base = bin(num)[index:]
            print(base)
            if base == int(str(base)[::-1]):
                index += 1
            return False
        return True


print(isStrictlyPalodromic(9))