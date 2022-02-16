# libraries for controlling lights
import board
import neopixel

def getInitData(num_lights, color_on, color_off):
    mainInitData={
            num_lights = num_lights
            color_on = color_on
            color_off = color_off
            next_light = 0
            prev_light = 0
            pixels = neopixel.NeoPixel(board.D18,
                                        self.num_lights,
                                        brightness=1,
                                        pixel_order=neopixel.RGB)
    }
    mainInitData.pixels.fill((0,0,0))
    return mainInitData

def stateLogic(state, Controller, self):
    if state == Controller.DOWN:
            self.pixels[self.next_light % self.num_lights] = self.color_on
            self.next_light+=1
    else:
        self.pixels[self.prev_light % self.num_lights] = self.color_off
        self.prev_light+=1