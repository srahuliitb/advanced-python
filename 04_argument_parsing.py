### Dummy example
# def my_function(*args, **kwargs):
#     for a in args:
#       print(a)

#     # for k in kwargs.keys():
#     #    print(f"{k}: {kwargs[k]}")
#     for k, v in kwargs.items():
#        print(f"{k}: {v}")
#     # print(kwargs)

# my_function('student', 'pgt', True, 31, firstname = 'Rahul', lastname = 'Singh')

### Realistc example 1
# import sys
# # Usage: python 04_argument_parsing.py test.txt learning\ argument\ parsing\ using\ python
# filename = sys.argv[1]
# message = sys.argv[2]

# with open(filename, 'w+') as f:
#    f.write(message)

### Realistic example 2
import sys
import getopt

# Usage: python 04_argument_parsing.py option_args_test.txt -p 8080 -h 
opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])

print(opts)