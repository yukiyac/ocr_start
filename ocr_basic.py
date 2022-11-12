from PIL import Image
import pyocr

tools = pyocr.get_available_tools()
tool = tools[0]

# print(tool)
# print(tool.get_name())

img = Image.open("sparta_camp_eng.png")
# img.show()

txt = tool.image_to_string(
    img,
    lang="eng+jpn",
    builder=pyocr.builders.TextBuilder()
)

print(txt)
