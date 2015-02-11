Steganana
=========

Steganana is a little project that had to be done individually during a semester at CSUMB.
Its purpose is very simple: hide some content inside an image, without this content actually being visible to the user.

Steganana is actually a simple class, but a sample wrapper is given to simplify its use, as well as providing a console tool.

Dependencies
------------

- python 2.7 or higher
- PIL (or Pillow)


Installation
------------

Installation is a breath: all that's needed is a simple git clone

``` sh
git clone https://github.com/Mandor53/Steganana
```

----------------------------

Console usage
-----

### Help

``` sh
python main.py --help
```

### Encoding a given string

``` sh
python main.py path/to/inputimage.png --encode "this is my sample text" --output path/to/output.png
```

If not provided, the output path will be output.png inside the active directory

### Encoding the content of a file

``` sh
python main.py path/to/inputimage.png --encode "path/to/inputcontent.txt" --output path/to/output.png
```

### Decoding the content encoded in an image

``` sh
python main.py path/to/encodedimage.png
```

### Decode and pipe output

Sometimes, you might want to be able to only get the actual decoded content, and not all the verbose stuff Steganana outputs

``` sh
python main.py path/to/encodedimage.png --silent > output.txt
```

----------------------------

Class usage
-----------

### Import the class

``` python
from src.Steganana import Steganana
```

### Create a new instance of the class

``` python
stegananaInstance = Steganana("path/to/inputimage.png", True)
```

### Encode a given string

``` python
stegananaInstance.encode("I want to encode this string", False, "path/to/output.png")
```

### Encode a given file

``` python
stegananaInstance.encode("path/to/inputcontent.txt", True, "path/to/output.png")
```

### Decode an image

``` python
print(stegananaInstance.decode())
```
