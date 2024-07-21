from mosaico import widget, config

text = widget.createText()
text.setText(config["text"])
text.setHexColor(config["color"])
text.setFont(config["font"])
text.moveTo(2,30)

def loop():
    # This breaks animation
    #text.centerHorizontally()  
    pass
