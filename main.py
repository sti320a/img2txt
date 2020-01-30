import cv2
import pyocr
from PIL import Image


def get_ocr_tool():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        return None
    return tools[0]


def save_img(
        src_path: str,
        out_path: str,
        lang: str,
        layout: int) -> None:
    builder = pyocr.builders.WordBoxBuilder(
        tesseract_layout=layout
    )
    ret = tool.image_to_string(
        Image.open(src_path),
        lang=lang,
        builder=builder
    )
    out = cv2.imread(src_path)
    for d in ret:
        cv2.rectangle(
            out,
            d.position[0],
            d.position[1],
            (0, 0, 255),
            2
        )
    cv2.imwrite(out_path, out)


def get_text(
        src_path: str,
        out_path: str,
        lang: str,
        layout: int) -> str:
    builder = pyocr.builders.TextBuilder(tesseract_layout=layout)
    ret = tool.image_to_string(
        Image.open(src_path),
        lang=lang,
        builder=builder
    )
    with open(out_path, 'w') as f:
        ret = ret.replace(' ', '')
        f.write(ret)
    return ret


if __name__ == "__main__":
    tool = get_ocr_tool()
    if tool:
        src = './images/test.png'
        lang = 'jpn'
        layout = 1

        out_png = './images/test_ret.png'
        save_img(
            src,
            out_png,
            lang,
            layout
        )

        out_txt = './text/test_ret.txt'
        get_text(
            src,
            out_txt,
            lang,
            layout
        )
