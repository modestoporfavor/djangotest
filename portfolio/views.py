from django.http import FileResponse, HttpResponse
from PIL import Image, ImageDraw, ImageFont


def createimage(wh, inputtext, font):
    width, height = wh
    image = Image.new("RGB", (100, 100), "purple")
    draw = ImageDraw.Draw(image)
    draw.text((width, height), inputtext, font=font, fill="white")
    return image


def index(request):
    inputtext = request.GET.get('text')

    if inputtext == None:
        inputtext = ""
    fontheight = 80
    font = ImageFont.truetype("//content/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", fontheight)
    image = Image.new("RGB", (100, 100), "purple")
    draw = ImageDraw.Draw(image)

    textwidth, textheight = draw.textsize(inputtext, font)

    frames = []
    x, y = 100, ((100 - textheight) / 2)
    distance = textwidth + 100

    for i in range(100):
        new_frame = createimage((x, y), inputtext, font)
        frames.append(new_frame)
        x += -(distance / 100)

    frames[0].save('my_video.gif', format='GIF',
                   append_images=frames[1:], save_all=True, duration=30, loop=0)

    # files.download("my_video.gif")
    file = open('my_video.gif', 'rb')
    return FileResponse(file)
