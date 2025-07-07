import sys
def main():
    h1=d1=h2=d2=aim=0
    with open(sys.argv[1]) as f:
        for line in f:
            cmd, val = line.split()
            v = int(val)
            if cmd[0]=='f':
                h1+=v; h2+=v; d2+=aim*v
            elif cmd[0]=='d':
                d1+=v; aim+=v
            elif cmd[0]=='u':
                d1-=v; aim-=v
            else:
                raise ValueError('Invalid command')
    sys.stdout.write(f"{h1*d1} {h2*d2}")
if __name__=="__main__":
    main()