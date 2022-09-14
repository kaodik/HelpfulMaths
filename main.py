inp1= input()
def print_hi(inp1):
    s = inp1.split('+')
    s.sort()
    s ='+'.join(s)
    print(s)
if __name__ == '__main__':
    print_hi(inp1)