import math
  fileopen=open("CO_ORDINATES.txt",'w+')
  latitude=34.020701
  longitude=-118.289680
  a=0.005
  b=0.003
  c=0.005
  nRev=8
  t=0.00
  while t<(math.pi*nRev):
    x=(a+b)*math.cos(t)-c*math.cos((a/b+1)*t)+latitude
    y=(a+b)*math.sin(t)-c*math.sin((a/b+1)*t)+longitude
    temp='<Placemark><styleUrl>#point_style</styleUrl><Point><coordinates>'+str(y)+','+str(x)+',100</coordinates></Point></Placemark>'+'\n'
    fileopen.write(str(temp))
    t+=0.01
fileopen.close()
