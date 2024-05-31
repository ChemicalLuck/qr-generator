
# QR Code Generator with Logo

This package provides a simple yet powerful tool for generating QR codes with custom logos embedded. You can easily create QR codes for your URLs with added branding using this package.

## Features
- Generate QR codes with custom logos embedded.
- Simple command-line interface for easy usage.

## Installation
You can install the package using pip:

```bash
pip install qr-generator
```

## Usage
To generate QR codes with logos, you can use the provided command-line interface. Here's the basic usage:

```bash
qrg <logo> <url> <suffix> <count> [-o OUTPUT]
```

<logo>: Path to the logo image file. The image must be in PNG format and have dimensions of 130px by 90px.
<url>: Base URL to which the suffix will be added to generate the QR codes.
<suffix>: Suffix to add to the base URL. This suffix will be appended to the base URL for each QR code generated.
<count>: Number of QR codes to generate.

### Optional Arguments:
-o OUTPUT, --output OUTPUT: Directory where the generated QR codes will be saved. If not specified, the current working directory will be used.

## Example
Generate 5 QR codes with logos for a website:

```bash
qrg logo.png https://example.com/page/ item_ 5 -o output_directory
```

This will generate 5 QR codes with logos for the URLs 
- https://example.com/page/item_001,
- https://example.com/page/item_002, 
- ...,
- https://example.com/page/item_005
and save them in the specified output_directory.


## License
This package is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
This package utilizes the qrcode and PIL libraries for generating QR codes and handling images, respectively.
