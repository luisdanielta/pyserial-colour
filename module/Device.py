import serial


class Device:

    port: str  # serial port COM4 - \dev\ttyACM0
    baudrate: int  # 9600 - 115200

    def __init__(self, port, baudrate) -> None:
        self.port = port
        self.baudrate = baudrate

    def connect(self) -> None:
        try:
            self.device = serial.Serial(self.port, self.baudrate)
        except Exception as e:
            print(e)

    def disconnect(self) -> None:
        self.device.close()

    def read(self) -> str:
        data = self.device.readline()  # readline() reads until \n
        return data.decode("utf-8")

    def write(self, data: str) -> None:
        self.device.write(data.encode("utf-8"))
