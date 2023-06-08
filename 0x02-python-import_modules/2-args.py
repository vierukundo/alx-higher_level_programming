#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments_num = len(sys.argv)
    if arguments_num <= 1:
        print('{} arguments.'.format(0))
    elif arguments_num == 2:
        print('{} argument:'.format(1))
        print('{}: {}'.format(1, (sys.argv)[1]))
    elif arguments_num > 2:
        print('{} arguments:'.format(arguments_num - 1))
        for i in range(1, arguments_num):
            print('{}: {}'.format(i, (sys.argv)[i]))
