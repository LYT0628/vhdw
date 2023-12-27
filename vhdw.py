import argparse
import sys
import os.path as op  

import vhd




def do_write(src, dest, lba):
  if not op.exists(src):
    raise ValueError("source file cannot not exist!!!")
  if not op.exists(dest):
    ans = input("warning: dest file is not exits. want to create ?[y/n]")
    if ans is 'n':
        exit(0)

  img = vhd.newVHD(dest)
  content = None
  with open (src, 'rb') as f:
    content = f.read()

  img.write(src=content, lba=lba)
  print(img.footer.cookie)

def parse_args():
    parser = argparse.ArgumentParser(
        prog="Vhdw",
        description="Vhdw is command line tool to write binary content to VHD format file.",
        epilog="Good luck."
  )

    parser.add_argument('-s', '--src', help="the source file will be written to vhd file")
    parser.add_argument('-d', '--dest', help="dest vhd file will be written")
    parser.add_argument('-n', '--number', default=0, 
                        help=' the beginning logic sector number(LBA) of dest location') 

    args = parser.parse_args()
    return args

if __name__ == "__main__":
  args = parse_args()
  
  do_write(src=args.src, 
           dest=args.dest,
           lba=args.number)
  
