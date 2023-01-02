from __future__ import annotations

import argparse
from dataclasses import dataclass
from io import BytesIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


@dataclass
class SpriteAnimation:
    """A row in the spritesheet.

    Args:
        text (str): The text to use for the sprites. If not specified,
         no text will be used.
        size (int): The size of the sprites.
        number (int): The number of sprites in the row.
    """

    text: str
    size: int
    number: int


class SpriteSheetGenerator:
    """Generates a spritesheet with a given number of sprites.

    Args:
        sprite_animations (list): A list of SpriteAnimation objects.
        output (str): The output file. If not specified, the spritesheet will be
        returned as a byte string representing a PNG image.
    """

    def __init__(self, sprite_animations, output):
        self.sprite_animations = sprite_animations
        self.output = output

    def generate(self):
        # Calculate the size of the spritesheet
        total_height = 0
        for row in self.sprite_animations:
            total_height += row.size

        width = 0
        for row in self.sprite_animations:
            width = max(width, row.size * row.number)

        spritesheet = Image.new(
            "RGB",
            (width, total_height),
            color=(255, 255, 255),
        )
        draw = ImageDraw.Draw(spritesheet)

        # Generate the text for each sprite
        y_offset = 0
        for row in self.sprite_animations:
            sprites = []
            for i in range(1, row.number + 1):
                if row.text:
                    sprites.append(f"{row.text} {i}")
                else:
                    sprites.append(str(i))

            font = ImageFont.load_default()

            # Draw the sprites
            x_offset = 0
            for sprite in sprites:
                # Calculate the size of the text
                bbox = font.getbbox(sprite)
                w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

                x = x_offset + row.size // 2 - w // 2
                y = y_offset + row.size // 2 - h // 2

                draw.text((x, y), sprite, font=font, fill=(0, 0, 0))
                draw.rectangle(
                    (
                        x_offset,
                        y_offset,
                        x_offset + row.size - 1,
                        y_offset + row.size - 1,
                    ),
                    outline=(0, 0, 0),
                )

                x_offset += row.size

            y_offset += row.size

        if self.output:
            spritesheet.save(self.output)
        else:
            buffer = BytesIO()
            spritesheet.save(buffer, format="png")
            return buffer.getvalue()


def cli():
    def check_positive(value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(
                f"Should be a positive integer, got {value}",
            )
        return ivalue

    # Set up the command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--sprite",
        nargs=3,
        metavar=("text", "size", "number"),
        action="append",
        required=True,
        help="A row in the spritesheet",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output.png",
        help="The output file",
    )
    args = parser.parse_args()

    sprite_animations = []
    for s in args.sprite:
        s[1] = check_positive(s[1])
        s[2] = check_positive(s[2])
        sprite_animations.append(SpriteAnimation(*s))

    generator = SpriteSheetGenerator(
        sprite_animations=sprite_animations,
        output=args.output,
    )
    generator.generate()


if __name__ == "__main__":
    cli()
