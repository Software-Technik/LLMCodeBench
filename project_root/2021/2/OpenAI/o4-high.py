import sys
def main():
    h1=d1=h2=d2=aim=0
    with open(sys.argv[1]) as f:
        for line in f:
            parts=line.split()
            if not parts: continue
            cmd,val=parts[0],int(parts[1])
            if cmd=='forward':
                h1+=val; h2+=val; d2+=aim*val
            elif cmd=='down':
                d1+=val; aim+=val
            elif cmd=='up':
                d1-=val; aim-=val
            else:
                raise ValueError('Invalid command')
    sys.stdout.write(f"{h1*d1} {h2*d2}")
if __name__=='__main__':
    main()