# Spritegen
Easily generate placeholder sprites sheets for your game.

## Installation
Install package using pip
```bash
pip install spritegen
```

## Usage
This script generates a sprite sheet image, which is a single image file containing a grid of smaller images (sprites).

A row in the sprite sheet consist of multiple sprites with the same reference text and an increasing number.

For example a row can be 10 sprites with text "Idle 0", "Idle 1", "Idle 2" etc.

Each row can have different number of sprites and sprite size.

## How to use

To use spritegen, you will need to provide it with some information about the sprites you want it to include. Specifically, for each row you can specify

- The reference text
- The sprite size
- The number of sprites

You can specify multiple rows of sprites by providing this information multiple times.

The script can be executed from the command line, or you can import it as a module use it in your own python code.

### Command line usage

```bash
spritegen --sprite text size number [-o OUTPUT]
```

For example:

```bash
spritegen --sprite Idle 32 5 --sprite Left 32 3  --sprite Right 32 3 --sprite Boss 128 3
```

This will generate a sprite sheet with 4 rows of sprites. The first row will contain 5 sprites with the text "Idle 0", "Idle 1", "Idle 2" etc. The second row will contain 3 sprites with the text "Left 0", "Left 1", "Left 2". The third row will contain 3 sprites with the text "Right 0", "Right 1", "Right 2". The fourth row will contain 3 sprites with the text "Boss 0", "Boss 1", "Boss 2". First three rows will have sprites of size 32x32 and the last row will have sprites of size 128x128.
