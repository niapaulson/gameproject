import pygame as pg
import utility as u
import bullet

class Tank(pg.sprite.Sprite):
	def __init__(self, x, y, tankImg, shootyThingImg,tankNum):
		self.image, self.rect = u.loadImage(tankImg)
		self.shootyThingImage, self.shootyThingRect = u.loadImage(shootyThingImg)
		if tankNum == 1:		
			self.rect.x = 100
			self.shootyThingRect.x = self.rect.x + 80

		elif tankNum == 2:
			self.rect.x = 971
			self.shootyThingRect.x = self.rect.x + 10
		
		self.rect.y = u.GROUND
		self.shootyThingRect.y = u.GROUND + 23
		pg.sprite.Sprite.__init__(self)
		self.tankSpeed = 2
		self.health = 50

	def move(self, direction):
		if(direction == pg.K_LEFT or direction == pg.K_a):
			self.rect.x -= self.tankSpeed
			self.shootyThingRect.x -= self.tankSpeed
		elif(direction == pg.K_RIGHT or direction == pg.K_d):
			self.rect.x += self.tankSpeed
			self.shootyThingRect.x += self.tankSpeed
		return self.rect.x, self.rect.y, self.shootyThingRect.x, self.shootyThingRect.y
	    
	def angle(self, direction,the_angle):   
		self.the_angle = the_angle   
		if direction == pg.K_UP:
			self.the_angle += 1
			for i in u.ANGLE_DICTIONARY_2.keys():
				diff = self.the_angle - i
				if i == self.the_angle or (diff <= 4 and diff > 0):
					self.shootyThingImage, junk = u.loadImage(u.ANGLE_DICTIONARY_2.get(i))
			return self.the_angle
		if direction == pg.K_w:
			self.the_angle += 1
			for i in u.ANGLE_DICTIONARY.keys():
				diff = self.the_angle - i
				if i == self.the_angle or (diff <= 4 and diff > 0):
					self.shootyThingImage, junk = u.loadImage(u.ANGLE_DICTIONARY.get(i))
			return self.the_angle
		if direction == pg.K_DOWN:
			self.the_angle += 1
			for i in u.ANGLE_DICTIONARY_2.keys():
				diff = self.the_angle - i
				if i == self.the_angle or (diff <= 4 and diff > 0):
					self.shootyThingImage, junk = u.loadImage(u.ANGLE_DICTIONARY_2.get(i))
			return self.the_angle
		if direction == pg.K_s:
			self.the_angle += 1
			for i in u.ANGLE_DICTIONARY.keys():
				diff = self.the_angle - i
				if i == self.the_angle or (diff <= 4 and diff > 0):
					self.shootyThingImage, junk = u.loadImage(u.ANGLE_DICTIONARY.get(i))
			return self.the_angle
		return self.the_angle

	def shoot(self, key):
		if key == pg.K_SPACE:
			direction = 1
			self.shot = bullet.Bullet(self.shootyThingRect.x, self.shootyThingRect.y, direction, "myBullet.png")
		if key == pg.K_RSHIFT: #elif doesn't work what?
			direction = -1
			self.shot = bullet.Bullet(self.shootyThingRect.x, self.shootyThingRect.y, direction, "myBullet2.png")
		return self.shot
