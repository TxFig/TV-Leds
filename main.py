from image import getFrame, release
from leds import update
from processing import getColors


try:
    while True:
        frame = getFrame()
        if frame is None:
            raise Exception("Error getting frame from video capture.")

        colors = getColors(frame)
        update(colors)

except KeyboardInterrupt: pass
except Exception as err:
    print(err)
finally:
    release()
