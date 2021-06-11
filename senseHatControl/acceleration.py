from sense_hat import SenseHat


class Acceleration:

    def __init__(self):
        self.sense_accel = SenseHat()

    def is_moved(self):
        E = self.sense_accel.accel_raw['x']**2 + self.sense_accel.accel_raw['y']**2 + (self.sense_accel.accel_raw['z']-0.98)**2
         #print("%.4f" %E)

        if E > 0.02:
            return True
        
        return False

