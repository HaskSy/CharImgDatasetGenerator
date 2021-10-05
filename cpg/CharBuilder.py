import io
import random
import string
import pkg_resources
from base64 import b64encode
from PIL import Image, ImageDraw, ImageFont


class CharBuilder:

    def __init__(self, lang="Latin"):

        # General
        self._size = (64, 64)
        self._lang = lang
        self._charset = None

        if self._lang == "Latin":
            self._charset = string.ascii_letters + string.digits
        elif self._lang == "Greek":
            self._charset = "αβγδεζηθικλμνξοπρςστυφχψω"
        else:
            print("Unknown language")
            return

        # Chars
        self._fonts = []
        for f in pkg_resources.resource_listdir("cpg", f"fonts/{self._lang}"):
            self._fonts.append(ImageFont.truetype(pkg_resources.resource_filename("cpg", f"fonts/{self._lang}/{f}"), 55))

        self._chars = ''.join(i for i in self._charset)

        # build()
        self.character = None
        self._image = None
        self._image_draw = None

    def _draw_char(self):

        """Draws char"""

        font = random.choice(self._fonts)

        max_x_add = int((self._size[0] - font.getsize(self.character)[0]))

        (_, height), (_, offset_y) = font.font.getsize(self.character)
        y_add = random.randint(1, self._size[1] - height)
        self._image_draw.text((random.randint(0, max_x_add), y_add - offset_y), self.character, fill=(0, 0, 0), font=font)
        print(height
              , offset_y)

    def build(self):

        """Create а new image."""

        self._image = Image.new("RGB", self._size, (255, 255, 255))
        self._image_draw = ImageDraw.Draw(self._image)
        self.character = random.choice(self._chars)
        self._draw_char()

    def show(self):

        """Shows image."""

        self._image.show()

    def save(self, filename):

        """Saves image to file."""

        self._image.save(filename)

    def base64(self, image_format='JPEG') -> str:

        """Returns a base64 encoded picture."""

        ret = io.BytesIO()
        self._image.save(ret, format=image_format)
        ret.seek(0)

        return b64encode(ret.getvalue()).decode()
