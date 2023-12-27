from rich_pixels import Pixels
from rich.console import Console

console = Console()
pixels = Pixels.from_image_path("art/Sprite-0003.png")
console.print(pixels)