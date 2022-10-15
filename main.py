import qrcode
from config import PATH


def generate(name, text):
    qr = qrcode.make(text)
    qr.save(f"{PATH}{name}.png")


def gen():
    name = input("Name: ")
    text = input("Text/URL: ")
    generate(name, text)


if __name__ == "__main__":
    gen()
