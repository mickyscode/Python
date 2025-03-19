import Conversions
Filename=input("Please enter filename")
contents=Conversions.getText(Filename)
contents2=contents.replace(" ","$")
Conversions.setText(Filename,contents2)