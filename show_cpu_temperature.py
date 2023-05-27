import smbus
import time
import subprocess

class LCD():
  def __init(self):
    self.i2c = smbus.SMBus(1)
    self.addr02 = 0x3e
    self.command = 0x00
    self.data = 0x40
    self.clear = 0x01
    self.home = 0x02
    self.display = 0x0f
    self.LCD_2ndline = 0x40 + 0x80
    

    def command(code):
      i2c.write_byte_data(self.addr02, self.command, code)
      time.sleep(0.1)

    def writeLCD(message):
      charlist = []
      for char in message:
        charlist.append(ord(char))
      i2c.write_i2c_block_data(self.addr02, self.data, charlist)
      time.sleep(0.1)

    def init():
      command(0x38)
      command(0x39)
      command(0x14)
      command(0x73)
      command(0x56)
      command(0x6c)
      command(0x38)
      command(self.clear)
      command(self.display)

init()
command(_clear)
writeLCD("CPU: ")
while 1:
	command(LCD_2ndline)
	res = subprocess.check_output(['vcgencmd', 'measure_temp'])
	decoded = res.decode('utf-8').replace('\n', '')
	print(decoded)
	writeLCD(decoded)
	time.sleep(0.3)

