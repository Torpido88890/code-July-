import textwrap

def wrap(string, max_width):

    for a in range(0,len(string),max_width):
       block = string[a:a+max_width]
       if len(block) == max_width:
            print(block)
       else:
            return block

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
