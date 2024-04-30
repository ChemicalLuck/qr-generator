import argparse
import os

import qrcode
from PIL import Image

BASE_WIDTH = 130


def load_logo(logo_path):
    logo = Image.open(logo_path)
    wpercent = BASE_WIDTH / float(logo.size[0])
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((BASE_WIDTH, hsize))
    return logo


def generate_qr(base_url, suffix, logo, output_dir):
    qr = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_H, border=4)

    url = f"{base_url}{suffix}"

    qr.add_data(url)
    qr.make()

    # adding color to QR code
    image = qr.make_image().convert("RGBA")

    # set size of QR code
    pos = ((image.size[0] - logo.size[0]) // 2, (image.size[1] - logo.size[1]) // 2)
    image.paste(logo, pos)

    image.save(f"{output_dir}/{suffix}.png")


def get_parser():
    parser = argparse.ArgumentParser(description="Generate QR codes with logo")
    parser.add_argument(
        "logo",
        help="Path to the logo image file. The image must be in PNG format and have dimensions of 130px by 90px.",
    )

    parser.add_argument(
        "url",
        help="Base URL to which the suffix will be added to generate the QR codes.",
    )

    parser.add_argument(
        "suffix",
        help="Suffix to add to the base URL. This suffix will be appended to the base URL for each QR code generated.",
    )

    parser.add_argument("count", type=int, help="Number of QR codes to generate.")

    # Optional arguments
    parser.add_argument(
        "-o",
        "--output",
        help="Directory where the generated QR codes will be saved. If not specified, the current working directory will be used.",
        default=os.getcwd(),
    )

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    logo = load_logo(args.logo)
    for i in range(1, int(args.count) + 1, 1):
        suffix = f"{args.suffix}{i:03d}"
        generate_qr(args.url, suffix, logo, args.output)


if __name__ == "__main__":
    main()
