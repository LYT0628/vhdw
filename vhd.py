import garbage.constant as constant
from enum import Enum

class Feature(Enum):
  NoFeature = b'\x00\x00\x00\x00'
  Temporary = b'\x00\x00\x00\x01'
  Reserved = b'\x00\x00\x00\x02'

class OS(Enum):
  WIN = b'Wi2k'
  MAC = b'Mac'

class DiskType(Enum):
  None_ = b'\x00\x00\x00\x00'
  Fixed = b'\x00\x00\x00\x02'
  Dynamic = b'\x00\x00\x00\x03'
  Differencing = b'\x00\x00\x00\x04'

def newVHD(type="dynamic"):
  pass


def newVHD(vhd_path: str):

  f = open(vhd_path, 'rb')

  f.seek(-512,2)
  footer_area = f.read(512)

  # footer_area = content[-512:]
  footer = Footer(cookie=footer_area[0:8],
                  features=footer_area[8:8+4],
                  file_format_version=footer_area[12:12+4],
                  data_offset=footer_area[16:16+8],
                  timestamp=footer_area[24:24+4],
                  creator_app=footer_area[28:28+4],
                  creator_version=footer_area[32:32+4],
                  creator_hostOS=footer_area[36:36+4],
                  original_size=footer_area[40:40+8],
                  current_size=footer_area[48:48+8],
                  cylinder=footer_area[56:56+2],
                  heads=footer_area[58:59],
                  sectors=footer_area[59:60],
                  disk_type=footer_area[60:64],
                  checksum=footer_area[64:68],
                  uuid_=footer_area[68:68+16],
                  saved_state=footer_area[84:85],
                  reserved=footer_area[85:85+427])

  
  if footer.diskType() == DiskType.Fixed:
    f.close()
    return FixedVHD(vhd_path=vhd_path, footer=footer)
  
  if footer.diskType() == DiskType.Dynamic:
    f.seek(512,0)
    header_area = f.read(1024)
      
    # block_allocation_table_area = content[512+1024:-511]

    header = Header(cookie=header_area[0:8],
                    data_offset=header_area[8:16],
                    table_offset=header_area[16:24],
                    header_version=header_area[24:28],
                    max_table_entry=header_area[28:32],
                    block_size=header_area[32:36],
                    checksum=header_area[36:40],
                    parent_uuid=header_area[40:56],
                    parent_timestamp=header_area[56:60],
                    reserved1=header_area[60:64],
                    parent_unicode_name=header_area[64:64+512],
                    parent_locator_entry1=header_area[576:576+24],
                    parent_locator_entry2=header_area[576+24:576+24*2],
                    parent_locator_entry3=header_area[576+24*2:576+24*3],
                    parent_locator_entry4=header_area[576+24*3:576+24*4],
                    parent_locator_entry5=header_area[576+24*4:576+24*5],
                    parent_locator_entry6=header_area[576+24*5:576+24*6],
                    parent_locator_entry7=header_area[576+24*6:576+24*7],
                    parent_locator_entry8=header_area[576+24*7:576+24*8],
                    reserved2=header_area[-256:])
    f.close()
    return DynamicVHD(header=header,footer=footer, vhd_path=vhd_path)
  
  raise NotImplementedError("The type of VHD is not supported now.")



class Footer:
  def __init__(self) -> None:
    self.cookie = b'conectix'
    self.futures = constant.bzero_b4
    self.file_format_version = constant.bzero_b4 
    self.data_offset = constant.bzero_b8 
    self.timestamp = constant.bzero_b4 
    self.creator_app = constant.bzero_b4 
    self.creator_version = constant.bzero_b4 
    self.creator_hostOS = constant.bzero_b4 
    self.original_size =constant.bzero_b8 

  def __init__(self,features,file_format_version, 
                    data_offset, timestamp,
                    creator_app, creator_version, creator_hostOS,
                    original_size, current_size ,
                    cylinder,heads, sectors,
                    disk_type, checksum,uuid_,
                    saved_state ,cookie=b'conectix', reserved = 0) -> None:
    self.cookie = cookie
    self.futures = features
    self.file_format_version = file_format_version
    self.data_offset = data_offset
    self.timestamp = timestamp
    self.creator_app = creator_app
    self.creator_version = creator_version
    self.creator_hostOS = creator_hostOS
    self.original_size = original_size
    self.current_size = current_size
    self.cylinder = cylinder
    self.heads = heads
    self.sectors = sectors
    self.disk_type = disk_type
    self.checksum = checksum
    self.uuid = uuid_ 
    self.saved_state = saved_state
    self.reserved = reserved

  def diskType(self):
    if self.disk_type is None:
      raise ValueError
    return DiskType(self.disk_type)


class FixedVHD:
  def __init__(self, vhd_path: str, footer: Footer) -> None:
    self._vhd_path = vhd_path # 需要时再打开， data=content[0:-512]
    self.footer:Footer = footer

class Header:
  def __init__(self) -> None:
    self.footer = None 
    self.cookie = b'cxsparse'
    self.data_offset = constant.f_b8
    self.table_offset = constant.bzero_b8
    self.header_version = constant.bzero_b4
    self.max_table_entry = constant.bzero_b4
    self.block_size = constant.bzero_b4
    self.checksum = constant.bzero_b4
    self.parent_uuid = constant.bzero_b16 
    self.parent_timestamp = constant.bzero_b4 
    self.reserved1 = constant.bzero_b4 
    self.parent_unicode_name = constant.bzero_b512
    self.parent_locator_entry1 = constant.bzero_b24
    self.parent_locator_entry2 = constant.bzero_b24
    self.parent_locator_entry3 = constant.bzero_b24
    self.parent_locator_entry4 = constant.bzero_b24
    self.parent_locator_entry5 = constant.bzero_b24
    self.parent_locator_entry6 = constant.bzero_b24
    self.parent_locator_entry7 = constant.bzero_b24
    self.parent_locator_entry8 = constant.bzero_b24
    self.reserved2 = constant.bzero_b256    

  def __init__(self,data_offset = None, table_offset = None,
                    header_version = None, max_table_entry = None,
                    block_size = None, checksum = None, 
                    parent_uuid = None, parent_timestamp = None,
                    reserved1 = None, parent_unicode_name = None,
                    parent_locator_entry1 = None,
                    parent_locator_entry2 = None,
                    parent_locator_entry3 = None,
                    parent_locator_entry4 = None,
                    parent_locator_entry5 = None,
                    parent_locator_entry6 = None,
                    parent_locator_entry7 = None,
                    parent_locator_entry8 = None,
                    reserved2 = None,
                    cookie=b'cxsparse') -> None:
    self.cookie = cookie
    self.data_offset = data_offset
    self.table_offset = table_offset
    self.header_version = header_version
    self.max_table_entry = max_table_entry
    self.block_size = block_size
    self.checksum = checksum
    self.parent_uuid = parent_uuid
    self.parent_timestamp = parent_timestamp
    self.reserved1 = reserved1
    self.parent_unicode_name = parent_unicode_name
    self.parent_locator_entry1 = parent_locator_entry1
    self.parent_locator_entry2 = parent_locator_entry2
    self.parent_locator_entry3 = parent_locator_entry3
    self.parent_locator_entry4 = parent_locator_entry4
    self.parent_locator_entry5 = parent_locator_entry5
    self.parent_locator_entry6 = parent_locator_entry6
    self.parent_locator_entry7 = parent_locator_entry7
    self.parent_locator_entry8 = parent_locator_entry8
    self.reserved2 = reserved2



class DynamicVHD:
  def __init__(self) -> None:
    self.header = None 
    self.footer = None
    self.block_allocation_table =None
    self.blocks = []


  def __init__(self ,  header: Header, footer: Footer, 
                      vhd_path: str) -> None:
    self.header = header 
    self.footer = footer
