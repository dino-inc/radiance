import discord
from discord.ext import commands
import asyncio
import time
from rpi_ws281x import *


# Configuration taken from the strandtest example in rpi_ws281x
# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()


    @commands.command(help = "test light command.")
    async def testlight(self, ctx):
        strip = self.strip
        await ctx.send(f"LIGHT!")
        strip.fill(Color(255, 0, 0))
        strip.show()

    @commands.command(help = "Gradual color fill.")
    async def fill(self, ctx, r, g, b):
        if(int(r) > 255 or int(g) > 255 or int(b) > 255):
            await ctx.send(f"At least one color is higher than 255. Please fix.")
            return
        if(int(r) < 0 or int(g) < 0 or int(b) < 0):
            await ctx.send(f"At least one color is lower than 0. Please fix.")
            return
        await gradualColorFill(self.strip, Color(int(r), int(g), int(b)), 5)
        await ctx.send(f"COLOR!")

    @commands.command(help = "Clears the colors.")
    async def clear(self, ctx):
        await gradualColorFill(self.strip, Color(0, 0, 0), 1)

# Also mostly taken from strandtest
async def gradualColorFill(strip, color, pause):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(pause/1000.0)


def setup(bot):
    bot.add_cog(Fun(bot))