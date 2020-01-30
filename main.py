import pyocr
from PIL import Image


def get_ocr_tool():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        return None
    return tools[0]


if __name__ == "__main__":
    tool = get_ocr_tool()
    if tool:
        path = './images/book.png'
        lang = 'jpn'
        text = tool.image_to_string(
            Image.open(path),
            lang=lang,
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        print(text.replace(' ', ''))
