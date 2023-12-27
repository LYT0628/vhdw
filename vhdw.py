import vhd

test_vhd = "/home/lyt0628/dev/CODE/vhdw/test.vhd"
orange_vhd = "/home/lyt0628/dev/CODE/vhdw/ORANGE.vhd"
FIX_vhd =  "/home/lyt0628/VirtualBox VMs/FIX_VHD2/FIX_VHD2.vhd"

bin_path = "/home/lyt0628/dev/CODE/vhdw/hello2.bin"
FIX_TEST = "/home/lyt0628/dev/CODE/vhdw/FIX_VHD2.vhd"
def main():
  img = vhd.newVHD(FIX_TEST)
  content = None
  with open (bin_path, 'rb') as f:
    content = f.read()

  img.write(src=content,lba=0)
  print(img.footer.cookie)

if __name__ == "__main__":
  main()