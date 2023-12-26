import utils
zero_b = "00" # 1 bytes 
zero_b2 = zero_b * 2 # 2 bytes
zero_d4 = zero_b * 4 # 4 bytes
zero_b8 = zero_b * 8  # 8 bytes 
zero_b16 = zero_b * 16  # 16 bytes 
zero_b24 = zero_b * 24  # 24 bytes 
zero_b256 = zero_b * 256  # 256 bytes 
zero_b512 = zero_b * 512  # 256 bytes 

f_b = "FF"
f_b8 =  f_b * 8

bzero_b = bytes.fromhex(zero_b)
bzero_b2 = bytes.fromhex(zero_b2)
bzero_d4 = bytes.fromhex(zero_d4)
bzero_b8 = bytes.fromhex(zero_b8)
bzero_b16 = bytes.fromhex(zero_b16)
bzero_b24 = bytes.fromhex(zero_b24)
bzero_b256 = bytes.fromhex(zero_b256)
bzero_b512 = bytes.fromhex(zero_b512)



default_block_size = bytes.fromhex('00200000') # 2MB 
if __name__ == "__main__":
  print(bytes.fromhex(zero_b))
  print(bytes.fromhex(zero_b2))
  print(bytes.fromhex(zero_d4))
  print(bytes.fromhex(zero_b8))