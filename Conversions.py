def KmM_conversion(km):
    m=km*1000
    return m
def MKm_conversion(m):
    km=m/1000
    return km
def getText(Filename):
    fp=open(Filename,"r")
    contents=fp.read()
    return contents
def setText(Textfile,Text):
    fp=open(Textfile,"w")
    contents=fp.write(Text)
    fp.close()