import vhd

test_vhd = "/home/lyt0628/dev/CODE/vhdw/test.vhd"
orange_vhd = "/home/lyt0628/dev/CODE/vhdw/ORANGE.vhd"
def main():
  img = vhd.newVHD(orange_vhd)
  print(int.from_bytes(img.header.table_offset,'big'))
  print(img.footer.cookie)

if __name__ == "__main__":
  main()