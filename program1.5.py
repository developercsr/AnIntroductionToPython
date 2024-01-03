"""There are 6 BitWiseOperators 
& : | : ~ : ^ : << : >> 
"""
def main():
    print(2&4)
    print(2|4)
    print(~4)#Result Comes in 2"s Compliments Form
    print(2^4)
    print(2<<4)#RIGH SIDE no.of bits will shifted to left side
    print(2>>4)#left side no.of bits will be shifted to right side
    #These will never be in rotating Order
if __name__ == "__main__":
    main()