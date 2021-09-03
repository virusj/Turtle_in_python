import turtle as t
import house_shepes as hs

#title
t.title('Getaway uniprep class')
t.setup(width=1300, height=900)

#speed
t.speed(10)

#bgcolor
t.bgcolor("skyblue")

#sun
hs.Sun(-350,250,30)


#grass
hs.grass(-650,0)

#trees


#road
hs.road(-650,-200)



#road dashs
hs.dot(-370,-260)
hs.dot(-220,-260)
hs.dot(-100,-260)
hs.dot(70,-260)
hs.dot(170,-260)
hs.dot(270,-260)
hs.dot(1070,-260)
hs.dot(70,-260)

#cloud
hs.cloud(510,200,30)
hs.cloud(550,250,20)
hs.cloud(520,230,20)



#house buildind
hs.house(-370,-100,'yellow')
hs.house(-100,-100,'purple')
hs.house(160,-100,'grey')
hs.house(-370,50,'#00ffff')
hs.house(-100,50,'#186874')
hs.house(160,50,'maroon')


#roop
hs.roof(-385,200,'#3b444b')
hs.roof(-115,200,'#3b444b')
hs.roof(150,200,'#3b444b')


#doors
hs.door(-290,-100)
hs.door(-20,-100)
hs.door(240,-100)

#handle
hs.doorhandle(-285,-75)
hs.doorhandle(-15,-75)
hs.doorhandle(245,-75)


#windows
hs.windows(-350,0)
hs.windows(-210,0)
hs.windows(-80,0)
hs.windows(60,0)
hs.windows(180,0)
hs.windows(320,0)

#up windows
hs.windows(-350,150)
hs.windows(-210,150)
hs.windows(-80,150)
hs.windows(60,150)
hs.windows(180,150)
hs.windows(320,150)


# car
hs.car(-490,-200)

hs.trees(-500,-70)
t.penup()
t.goto(-500,0)
t.pendown()
t.color('brown')
t.begin_fill()
#def branch(blen):
blen=100
while blen > 10:
		angle = 30
		t.pensize (blen/10)
		t.fd(blen)
		t.left(angle)
		#branch(blen * 0.7)
		t.right(angle * 2)
		#branch(blen * 0.7)
		t.left(angle)
		t.backward(blen)
#branch(100)
t.end_fill()
    

#t.hideturtle()