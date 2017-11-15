import os
import subprocess


RESET_CODE = 0
ALLOC_CODE = 1
ASSOC_CODE = 2

RESET_STR = "/home/shelbyt/research/gitprojects/lambda-core/bin/reset_app "
ALLOC_STR = "/home/shelbyt/research/gitprojects/lambda-core/bin/allocation_app "
ASSOC_STR = "/home/shelbyt/research/gitprojects/lambda-core/bin/association_app "

def run_bin(code, args):
    if code is RESET_CODE:
        print "reset code"
    else if code is ALLOC_CODE:
        printf "alloc code"
    else if code is ASSOC_CODE:
        printf "ass code"

def main():
    print "hello\n"
    run_bin(RESET_CODE, 10)


if __name__ == "__main__":
        main()
