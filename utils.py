



def calculate_CHS():
  pass

def calculate_checksum():
  pass

def calculate_timestamp():
  pass

def fill_lz(hex_str: str, size: int):
  if len(str) == size:
     return hex_str
  if len(str) > size:
    return str[-size:]
  tmp_str = hex_str
  while(len(tmp_str) < size):
    tmp_str = "0"+tmp_str
  return tmp_str


if __name__ == "__main__":
  str = "ffff"
  print(fill_lz(hex_str=str, size=8))
  str = "000000ff"
  print(fill_lz(hex_str=str,size=6))


