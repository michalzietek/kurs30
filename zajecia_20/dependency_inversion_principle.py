from abc import ABC, abstractmethod

# class Light:
#     def turn_on(self):
#         print("Wlaczylem swiatlo")
#
#     def turn_off(self):
#         print("Wylaczylem swiatlo")
#
# class LightSwitch:
#     def __init__(self, light):
#         self.light = light
#         self.is_on = False
#
#     def press(self):
#         if self.is_on:
#             self.light.turn_off()
#             self.is_on = False
#         else:
#             self.light.turn_on()
#             self.is_on = True
#
# light = Light()
# wlacznik = LightSwitch(light)
# wlacznik.press()
# wlacznik.press()
# wlacznik.press()


class LightSource(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class BulbLight(LightSource):

    def turn_on(self):
        print("Wlaczam swiatlo w zarowce")

    def turn_off(self):
        print("Wylaczam swiatlo w zarowce")

class LedLight(LightSource):
    def turn_on(self):
        print("Wlaczam swiatlo ledowe")

    def turn_off(self):
        print("Wylaczam swiatlo ledowe")


class LightSwitch:
    def __init__(self, light: LightSource):
        self.light = light
        self.is_on = False

    def press(self):
        if self.is_on:
            self.light.turn_off()
            self.is_on = False
        else:
            self.light.turn_on()
            self.is_on = True


bulb_light = BulbLight()
bulb_light.turn_on()
led_light = LedLight()
switch = LightSwitch(led_light)
switch.press()
switch.press()
switch.light = bulb_light
switch.press()
switch.press()
