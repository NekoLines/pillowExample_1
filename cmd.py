import sys
import makeText

def main():
    if len(sys.argv) < 3:
        print("Arguments is too less for finishing jobs\nUsage: python3 cmd.py aaa bbb")
        return -1
    
    args = sys.argv[1:]
    try:
        makeText.make_text(args, "meme.png")
    except OSError:
        print("Can't found enough dependence, do you install all the needed binaries?")
    return 0

main()