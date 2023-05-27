import smbus
import time

class LCD:
  def __init__(self):
    self.i2c = smbus.SMBus(1)
    self.addr02 = 0x3e
    self.command_line = 0x00
    self.data = 0x40
    self.clear = 0x01
    self.home = 0x02
    self.display = 0x0f
    self.LCD_2ndline = 0x40 + 0x80
    

  def command(self, code):
    self.i2c.write_byte_data(self.addr02, self.command_line, code)
    time.sleep(0.1)

  def writeLCD(self, message):
    charlist = []
    for char in message:
      charlist.append(ord(char))
    self.i2c.write_i2c_block_data(self.addr02, self.data, charlist)
    time.sleep(0.1)

  def LCDinit(self):
    self.command(0x38)
    self.command(0x39)
    self.command(0x14)
    self.command(0x73)
    self.command(0x56)
    self.command(0x6c)
    self.command(0x38)
    self.command(self.clear)
    self.command(self.display)


