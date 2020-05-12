import pygame

pygame.init()
clock=pygame.time.Clock()
win=pygame.display.set_mode((850,480))
pygame.display.set_caption("game")

walkleft=[pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),pygame.image.load("L6.png"),pygame.image.load("L7.png"),pygame.image.load("L8.png"),pygame.image.load("L9.png")]
walkright=[pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png"),pygame.image.load("R7.png"),pygame.image.load("R8.png"),pygame.image.load("R9.png"),]
bg=pygame.image.load("bg.jpg")
walklefte=[pygame.image.load("L1E.png"),pygame.image.load("L2E.png"),pygame.image.load("L3E.png"),pygame.image.load("L4E.png"),pygame.image.load("L5E.png"),pygame.image.load("L6E.png"),pygame.image.load("L7E.png"),pygame.image.load("L8E.png"),pygame.image.load("L9E.png"),pygame.image.load("L10E.png"),pygame.image.load("L11E.png")]
walkrighte=[pygame.image.load("R1E.png"),pygame.image.load("R2E.png"),pygame.image.load("R3E.png"),pygame.image.load("R4E.png"),pygame.image.load("R5E.png"),pygame.image.load("R6E.png"),pygame.image.load("R7E.png"),pygame.image.load("R8E.png"),pygame.image.load("R9E.png"),pygame.image.load("R10E.png"),pygame.image.load("R11E.png")]



class character(object):
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.vel=5
		self.isjump=False
		self.isstanding=True
		self.jump=10
		self.walk=0
		self.left=True
		self.right=False
	def draw(self,win,count,walkleft,walkright):
		if not self.isstanding:
			if self.walk+1>=count:
				self.walk=0

			if self.left:
				win.blit(walkleft[self.walk//3],(self.x,self.y))
				self.walk+=1
			if self.right:
				win.blit(walkright[self.walk//3],(self.x,self.y))
				self.walk+=1
		else:
			if self.left:
				win.blit(walkleft[0],(self.x,self.y))

			else:
				win.blit(walkright[0],(self.x,self.y))




				

class projectile(object):
	def __init__(self,x,y,vel,facing):
		self.x=x
		self.y=y
		self.radius=5
		self.facing=facing
		self.vel=facing*5
	def draw(self,win):
			pygame.draw.circle(win,(255,0,0),(self.x,self.y),self.radius)				

def redrawwindow():
	win.blit(bg,(0,0))
	man.draw(win,27,walkleft,walkright)
	goblin.draw(win,33,walklefte,walkrighte)
	for bullet in bullets:
		bullet.draw(win)
	pygame.display.update()

man=character(200,400,64,64)
goblin=character(100,400,64,64)
start=True
bullets=[]
while start:
	clock.tick(27)
	redrawwindow()
	for events in pygame.event.get():
		if events.type==pygame.QUIT:
			start=False
	for bullet in bullets:
		if (bullet.x>0 and bullet.x<830) and not(bullet.x>=goblin.x and bullet.x<=goblin.x+goblin.width) and bullet.y<goblin.y+goblin.height:
			bullet.x+=bullet.vel
		else:
			bullets.pop(bullets.index(bullet))		
	keys=pygame.key.get_pressed()
	facing=-1
	if keys[pygame.K_SPACE]:
		if(len(bullets)<=1):
			if man.left:
				facing=-1
			else:
				facing=1
			bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),5,facing))
	if keys[pygame.K_LEFT]:
		man.left=True
		man.right=False
		man.isstanding=False
		man.x-=man.vel
	elif keys[pygame.K_RIGHT]:
		man.right=True
		man.left=False
		man.isstanding=False
		man.x+=man.vel
	else:
		man.walk=0
		man.isstanding=True

	if not man.isjump:
		if keys[pygame.K_UP]:
			man.isjump=True
	else:
		if man.jump>=-10:
			neg=1
			if man.jump<0:
				neg=-1
			man.y-=(man.jump**2)*neg*0.5
			man.jump-=1
		else:
			man.isjump=False
			man.jump=10
	goblin.isstanding=False
	goblin.vel=3
	if goblin.left:

		if goblin.x>-20:
			goblin.x-=goblin.vel
		else:
			goblin.left=False
			goblin.right=True
	else:
		if goblin.x<800:
			goblin.x+=goblin.vel
		else:
			goblin.left=True
			goblin.right=False


pygame.quit()




