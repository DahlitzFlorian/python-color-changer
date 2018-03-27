# Python Color Changer #
## Description ##
This lightweight color-changer allows you to change the colors<br>
of a given picture and creates a new file of it.

## Installation ##
You can install it from source or using `pip`

```bash
$ pip install color-changer
```

## Available Arguments ##
Short | Long | Values
------|------|-------
-i | --image | path to image
-c | --changer | red-green or gree-blue or blue-red
-r | --result | new image name

## Examples ##
```bash
$ python app.py -i image.jpg
$ python app.py -i image.png -c red-green
```