import os
import glob
import time
import datetime
import MySQLdb as mdb

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def read_temp():
    lines = read_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

def read_raw():
	f = open('/sys/bus/w1/devices/28-00000560af11/w1_slave','r')
        lines = f.readlines()
        f.close()
        return lines

while True:
        try:
                con = mdb.connect('YOURIPADDRESS','YOURUSER','YOURPASSWORD','YOURDATABASE')
        except _mysql.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)
        finally:
                with con:
                        temperature = read_temp()
			temperature = str(temperature)
			timestamp = datetime.datetime.now()
                        cur = con.cursor()
                        cur.execute(YOURQUERYSTRINGHERE)
       		time.sleep(60)

