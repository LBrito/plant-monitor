import time
from unittest import TestCase

from devices.relay_device import RelayDevice


class RelayDeviceTest(TestCase):
    def test_relay_device(self):
        device = RelayDevice(22)
        try:
            device.switch(True)
            time.sleep(50)
            device.switch(False)
        except KeyboardInterrupt:
            device.switch(False)
        finally:
            device.reset()
        self.fail()
