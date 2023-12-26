# vhdw

vhdw is a tool to write img info vhd format file.



## VHDW格式笔记



- 类型
	- Fixed
	- Dynamic
    - Differencing

### Fixed 
- 创建即分配了所有大小，比如虚拟硬盘大小为2GB， 则它在主机中文件大小也应当分配有2GB的数据区域。
- 数据区域之后有一个尾部， FIxed VHD硬盘的大小就等于 数据区域大小 + 尾部区域大小。

### Dynamic 
- 动态VHD由三部分组成，头部，数据区域，和尾部，三者大小之和即VHD文件大小
- 动态VHD数据区域以块分配，写入多少数据，就分配足以装下数据的块
- 动态VHD格式
	- 头部：
		- 512字节：尾部的赋值
		- 1024字节: 动态硬盘头
		- BAT, 块分配表
		- 数据块数组...
		- 512字节： 尾部

### Disserencing
差分VHD

- 不同的硬盘映像

### 尾部格式
共： 512字节
| Hard disk footer fields  |Size (bytes) |  Diescription |
|Cookie                    |8            |  大小写敏感，用于给给硬盘发明者（conectix）做标识 |
|Features                   |4          | 标识特性支持， 0x0标识没有特别功能，0x1表示硬盘是暂时存放的，随时会被删掉，0x2 表示保留，硬盘所有bits都设为0
| File Format Version       |4          | 版本由两部分组成，主版本和次版本，0x00010000, 当版本不向下兼容时更新版本号
|Data Offset               |8           | 数据偏移，动态硬盘和差分使用，表示 数据区域偏移， fixedVHD 永远设置为0xFFFFFFFF
|Time Stamp                 |      4 | 时间戳 ，储存创建时间（秒）  This is the number of seconds since January 1, 2000 12:00:00 AM in UTC/GMT.
|Creator Application      |         4| 标识创建硬盘的应用，vpc 表示 微软的VIrtualPC
|Creator Version          |     4   | 创建者的版本号啦自己设就好了
|Creator Host OS          |     4 | 如果是windows 0x5769326B, Macintosh???
|Original Size            | 8 | 原始尺寸，用于储存Fixed VHD大小， 
|Current Size            | 8    | 当前尺寸，表示虚拟盘的大小，只有当硬盘被拓展时，值才会被改变
|Disk Geometry          |         4| 硬盘分布， 柱头数目（2字节），磁头数据（1字节），每柱头扇区数（1字节）
|Disk Type         |         4 | 0-None， ..， 2-Fixed， 3-Dynamic， 4-Differencing...
|Checksum      |           4 |  校验和，尾部区域除了校验和位外所有字节之和，   
| Unique Id |16 | UUID，差分VHD中用来标识父盘
| Saved State |1     | 保存状态， 1- 已保存， 0-未保存，先切换为未保存状态在进行修改，然后切回已保存状态
| Reserved |427 | 全部为 0

### Dynamic 头部格式

### 映射硬盘磁道到块磁道

### 硬盘映像划分

### 执行写操作
### 执行读操作
### 父盘映像标识
### 父盘映像修改
