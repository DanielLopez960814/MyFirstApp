import io
import eel
import crop
import Analysis
import loadImages

eel.init('web')


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

@eel.expose
def LoadImagesFromPage():
    loadImages.Load()

@eel.expose
def AnalyzeFromPage():
    Analysis.imageAnalysis()

@eel.expose
def CropFromPage():
    crop.Cropping()



# @eel.expose
# def generate_qr(data):
#     img = pyqrcode.create(data)
#     buffers = io.BytesIO()
#     img.png(buffers, scale=8)
#     encoded = b64encode(buffers.getvalue()).decode("ascii")
#     print("QR code generation successful.")
#     return "data:image/png;base64, " + encoded

eel.start('index.html', size=(1000, 620))
