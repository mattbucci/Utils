
Takes one image as an argument and replaces said image with an equivalent placeholded version using placehold.it Prints the resolution required.

you can run this on all images in a directory using
``` find . -name '*.jpg' -exec python ~/placehold.py "{}" \; ```
