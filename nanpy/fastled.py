from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)
from enum import Enum, unique

@unique
class HSVHue(Enum):
	HUE_RED = 0
	HUE_ORANGE = 32
	HUE_YELLOW = 64
	HUE_GREEN = 96
	HUE_AQUA = 128
	HUE_BLUE = 160
	HUE_PURPLE = 192
	HUE_PINK = 224

@unique
class EOrder(Enum):
	RGB=12
	RBG=21
	GRB=102
	GBR=120
	BRG=201
	BGR=210

class CRGB(Enum):
	AliceBlue = 0xF0F8FF
	Amethyst = 0x9966CC
	AntiqueWhite = 0xFAEBD7
	Aqua = 0x00FFFF
	Aquamarine = 0x7FFFD4
	Azure = 0xF0FFFF
	Beige = 0xF5F5DC
	Bisque = 0xFFE4C4
	Black = 0x000000
	BlanchedAlmond = 0xFFEBCD
	Blue = 0x0000FF
	BlueViolet = 0x8A2BE2
	Brown = 0xA52A2A
	BurlyWood = 0xDEB887
	CadetBlue = 0x5F9EA0
	Chartreuse = 0x7FFF00
	Chocolate = 0xD2691E
	Coral = 0xFF7F50
	CornflowerBlue = 0x6495ED
	Cornsilk = 0xFFF8DC
	Crimson = 0xDC143C
	Cyan = 0x00FFFF
	DarkBlue = 0x00008B
	DarkCyan = 0x008B8B
	DarkGoldenrod = 0xB8860B
	DarkGray = 0xA9A9A9
	DarkGrey = 0xA9A9A9
	DarkGreen = 0x006400
	DarkKhaki = 0xBDB76B
	DarkMagenta = 0x8B008B
	DarkOliveGreen = 0x556B2F
	DarkOrange = 0xFF8C00
	DarkOrchid = 0x9932CC
	DarkRed = 0x8B0000
	DarkSalmon = 0xE9967A
	DarkSeaGreen = 0x8FBC8F
	DarkSlateBlue = 0x483D8B
	DarkSlateGray = 0x2F4F4F
	DarkSlateGrey = 0x2F4F4F
	DarkTurquoise = 0x00CED1
	DarkViolet = 0x9400D3
	DeepPink = 0xFF1493
	DeepSkyBlue = 0x00BFFF
	DimGray = 0x696969
	DimGrey = 0x696969
	DodgerBlue = 0x1E90FF
	FireBrick = 0xB22222
	FloralWhite = 0xFFFAF0
	ForestGreen = 0x228B22
	Fuchsia = 0xFF00FF
	Gainsboro = 0xDCDCDC
	GhostWhite = 0xF8F8FF
	Gold = 0xFFD700
	Goldenrod = 0xDAA520
	Gray = 0x808080
	Grey = 0x808080
	Green = 0x008000
	GreenYellow = 0xADFF2F
	Honeydew = 0xF0FFF0
	HotPink = 0xFF69B4
	IndianRed = 0xCD5C5C
	Indigo = 0x4B0082
	Ivory = 0xFFFFF0
	Khaki = 0xF0E68C
	Lavender = 0xE6E6FA
	LavenderBlush = 0xFFF0F5
	LawnGreen = 0x7CFC00
	LemonChiffon = 0xFFFACD
	LightBlue = 0xADD8E6
	LightCoral = 0xF08080
	LightCyan = 0xE0FFFF
	LightGoldenrodYellow = 0xFAFAD2
	LightGreen = 0x90EE90
	LightGrey = 0xD3D3D3
	LightPink = 0xFFB6C1
	LightSalmon = 0xFFA07A
	LightSeaGreen = 0x20B2AA
	LightSkyBlue = 0x87CEFA
	LightSlateGray = 0x778899
	LightSlateGrey = 0x778899
	LightSteelBlue = 0xB0C4DE
	LightYellow = 0xFFFFE0
	Lime = 0x00FF00
	LimeGreen = 0x32CD32
	Linen = 0xFAF0E6
	Magenta = 0xFF00FF
	Maroon = 0x800000
	MediumAquamarine = 0x66CDAA
	MediumBlue = 0x0000CD
	MediumOrchid = 0xBA55D3
	MediumPurple = 0x9370DB
	MediumSeaGreen = 0x3CB371
	MediumSlateBlue = 0x7B68EE
	MediumSpringGreen = 0x00FA9A
	MediumTurquoise = 0x48D1CC
	MediumVioletRed = 0xC71585
	MidnightBlue = 0x191970
	MintCream = 0xF5FFFA
	MistyRose = 0xFFE4E1
	Moccasin = 0xFFE4B5
	NavajoWhite = 0xFFDEAD
	Navy = 0x000080
	OldLace = 0xFDF5E6
	Olive = 0x808000
	OliveDrab = 0x6B8E23
	Orange = 0xFFA500
	OrangeRed = 0xFF4500
	Orchid = 0xDA70D6
	PaleGoldenrod = 0xEEE8AA
	PaleGreen = 0x98FB98
	PaleTurquoise = 0xAFEEEE
	PaleVioletRed = 0xDB7093
	PapayaWhip = 0xFFEFD5
	PeachPuff = 0xFFDAB9
	Peru = 0xCD853F
	Pink = 0xFFC0CB
	Plaid = 0xCC5533
	Plum = 0xDDA0DD
	PowderBlue = 0xB0E0E6
	Purple = 0x800080
	Red = 0xFF0000
	RosyBrown = 0xBC8F8F
	RoyalBlue = 0x4169E1
	SaddleBrown = 0x8B4513
	Salmon = 0xFA8072
	SandyBrown = 0xF4A460
	SeaGreen = 0x2E8B57
	Seashell = 0xFFF5EE
	Sienna = 0xA0522D
	Silver = 0xC0C0C0
	SkyBlue = 0x87CEEB
	SlateBlue = 0x6A5ACD
	SlateGray = 0x708090
	SlateGrey = 0x708090
	Snow = 0xFFFAFA
	SpringGreen = 0x00FF7F
	SteelBlue = 0x4682B4
	Tan = 0xD2B48C
	Teal = 0x008080
	Thistle = 0xD8BFD8
	Tomato = 0xFF6347
	Turquoise = 0x40E0D0
	Violet = 0xEE82EE
	Wheat = 0xF5DEB3
	White = 0xFFFFFF
	WhiteSmoke = 0xF5F5F5
	Yellow = 0xFFFF00
	YellowGreen = 0x9ACD32
	FairyLight = 0xFFE42D
	FairyLightNCC = 0xFF9D2A

class LEDColorCorrection(Enum):
  TypicalSMD5050 = 0xFFB0F0
  TypicalLEDStrip = 0xFFB0F0
  Typical8mmPixel = 0xFFE08C
  TypicalPixelString = 0xFFE08C
  UncorrectedColor = 0xFFFFFF

class ColorTemperature(Enum):
	Candle = 0xFF9329
	Tungsten40W = 0xFFC58F
	Tungsten100W = 0xFFD6AA
	Halogen = 0xFFF1E0
	CarbonArc = 0xFFFAF4
	HighNoonSun = 0xFFFFFB
	DirectSunlight = 0xFFFFFF
	OvercastSky =0xC9E2FF,
	ClearBlueSky =0x409CFF
	WarmFluorescent =0xFFF4E5
	StandardFluorescent =0xF4FFFA
	CoolWhiteFluorescent =0xD4EBFF,
	FullSpectrumFluorescent =0xFFF4F2
	GrowLightFluorescent =0xFFEFF7
	BlackLightFluorescent =0xA700FF
	MercuryVapor =0xD8F7FF,
	SodiumVapor =0xFFD1B2
	MetalHalide =0xF2FCFF
	HighPressureSodium =0xFFB74C
	UncorrectedTemperature =0xFFFFFF


class FastLED(ArduinoObject):

    #def __init__(self, led_type, num_leds, connection=None, matrix=None, serpentine=None rgb_order=Eorder.RGB):
    def __init__(self, led_type, num_leds, connection=None, matrix=None, serpentine=None):
        ArduinoObject.__init__(self, connection=connection)

        self.serpentineLayout = True if serpentine else False
        self.rgb_order = 12

        print("Number of LEDS: {0}\nLED Type: {1}".format(num_leds, led_type))

        if matrix is not None and type(matrix) is list:
            self.matrixHeight = matrix[0]
            self.matrixWidth = matrix[1]
            self.num_leds = (self.matrixHeight * self.matrixWidth) + 1
        else:
            self.matrixWidth = None
            self.matrixHeight = None
            self.num_leds = num_leds

        self.id = self.call('new', led_type, self.num_leds, self.rgb_order)

        return

	# def xySafe(self,x_coord,y_coord):
	# 	if not self.serpentineLayout:
	# 		i = ( y_coord * matrixWidth) + x_coord;
	# 	else:
	# 		if y_coord & 1 :
	# 			reverseX = (matrixWidth - 1) - x_coord
	# 			i = (y_coord * matrixWidth) + reverseX
	# 		else:
	# 			i = (y_coord * matrixWidth) + x_coord
	#
	# 	return i

	# def drawOneFrame( startHue, yHueDelta8, xHueDelta8):
	# 	lineStartHue = startHue8;
	# 	for( byte y = 0; y < kMatrixHeight; y++) {
	# 		lineStartHue += yHueDelta8;
	# 		pixelHue = lineStartHue;
	# 		for x in range(0,matrixWidth):
	# 			pixelHue += xHueDelta8;
	# 			hue =
	# 			self.setitem()
	# 			leds[ XY(x, y)]  = self.CHSV( pixelHue, 255, 255);

    @arduinoobjectmethod
    def show(self):
        return

    @arduinoobjectmethod
    def set_item(self, key, value):
        return

    @arduinoobjectmethod
    def set_color(self, index, value):
        return

    @arduinoobjectmethod
    def fill_rainbow(self, initialHue, deltahue):
        return

    @arduinoobjectmethod
    def fill_solid(self, num, color):
        return

    @arduinoobjectmethod
    def set_rgb(self, index, r=0, g=0, b=0):
        return

	@arduinoobjectmethod
	def setBrightness(self, brightness):
		return

	@returns(int)
	@arduinoobjectmethod
	def getBrightness(self):
		return

	@arduinoobjectmethod
	def showColor(self,rgb, scale=None):
		return

	@arduinoobjectmethod
	def delay(self, ms):
		return

	@arduinoobjectmethod
	def setTemperature(self, rgb):
		return

	@arduinoobjectmethod
	def setCorrection(self, rgb):
		return

	@arduinoobjectmethod
	def setDither(self, ditherMode="BINARY_DITHER"):
		return

	@arduinoobjectmethod
	def setMaxRefreshRate(self, refresh, constrain=False):
		return

    @arduinoobjectmethod
    def countFPS(self,nFrames=25):
        return

    @returns(int)
    @arduinoobjectmethod
    def getFPS(self):
        return

    @returns(int)
    @arduinoobjectmethod
    def count(self):
        return

    @returns(int)
    @arduinoobjectmethod
    def size(self):
        return

    @arduinoobjectmethod
    def clear(self, writeData=False):
        return

	@arduinoobjectmethod
	def clearData(self):
		return


	@arduinoobjectmethod
	def fill_gradient_RGB(self,start_color, end_color):
		return

	@arduinoobjectmethod
	def fadeLightBy(self,fadeBy):
		return

	@arduinoobjectmethod
	def fade_video(self,fadeBy):
		return

	@arduinoobjectmethod
	def nscale8_video(self, scale):
		return

	@arduinoobjectmethod
	def fadeToBlackBy(self, fadeBy):
		return

	@arduinoobjectmethod
	def fade_raw(self, fadeBy):
		return

	@arduinoobjectmethod
	def nscale8(self, scale):
		return

	@arduinoobjectmethod
	def fadeUsingColor(self, colormask):
		return

	@arduinoobjectmethod
	def	setMaxPowerInVoltsAndMilliamps(volts, milliamps):
		return

	@arduinoobjectmethod
	def	setMaxPowerInMilliWatts(powerInmW):
		return

	@arduinoobjectmethod
	def set_max_power_in_volts_and_milliamps(volts, milliamps):
		return

	@arduinoobjectmethod
	def set_max_power_in_milliwatts(powerInmW)
		return

	@arduinoobjectmethod
	def	set_max_power_indicator_LED (pinNumber):
		return

	@arduinoobjectmethod
	def show_at_max_brightness_for_power():
		return

	@arduinoobjectmethod
	def delay_at_max_brightness_for_power(ms):
		return

	@returns(int)
	def	calculate_unscaled_power_mW ():
		return

	@returns(int)
	@arduinoobjectmethod
	def	calculate_max_brightness_for_power_vmA (target_brightness, max_power_V, max_power_mA):
		return

	@returns(int)
	@arduinoobjectmethod
	def calculate_max_brightness_for_power_mW (target_brightness, max_power_mW):
		return
