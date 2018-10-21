import serial
from time import sleep

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data
sum_string = ""
str_split = ""
if __name__ == '__main__':
    ser = serial.Serial('COM5', 9600, timeout=0.5)  #/dev/ttyUSB0
    if ser.isOpen() :
        print("open success")
    else :
        print("open failed")
    # data = "01020304aa"
    # data = data.decode("hex")
    while True:
        # data =ser.read(1)
        data = ser.read_all()
        print data
        # ser.write(data)
        # if len(data) == 1:
        #     data = "0" + data
        sum_string += data
        # print sum_string
        # print "sum_string", sum_string
        if len(sum_string)>32:
            sum_string = ""
        if sum_string != '':
            str_split = sum_string.split('/')
            # print 'sumstr_split', str_split
            for n in range(len(str_split)):
                if str_split[n] != '':
                    if (str_split[n].find("T") != -1)&(len(str_split[n])>=6):
                        print "str_splitT:", str_split[n]
                    if (str_split[n].find("Y") != -1) & (len(str_split[n]) >= 6):
                        print "str_splitY:", str_split[n]

        # if data != b'' :
        #     print("receive : ",data)
        #     serial.write(data)

