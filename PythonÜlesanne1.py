import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill((34,53,140))
pygame.display.set_caption("Esimene aken")
font=pygame.font.SysFont("Esimene aken",40)
sõnad="Tere tulemast!"
varv=[200,200,200]
teksti_lisamine=font.render(sõnad,False,varv)
ekraani_pind.blit(teksti_lisamine,(250,25))
kollane=[255,255,10]
lopp_x=300
lopp_y=0
for i in range(30):
    pygame.draw.line(ekraani_pind,kollane,(0,0),(lopp_x, lopp_y),3)
    lopp_x-=10
    lopp_y+=12
   
    

lill6=pygame.Rect(140,20,100,100)
pygame.draw.ellipse(ekraani_pind,(205,250,205),lill6)
lill7=pygame.Rect(70,20,100,100)
pygame.draw.ellipse(ekraani_pind,(205,250,205),lill7)
lill7=pygame.Rect(70,90,100,100)
pygame.draw.ellipse(ekraani_pind,(205,250,205),lill7)
lill6=pygame.Rect(140,90,100,100)
pygame.draw.ellipse(ekraani_pind,(205,250,205),lill6)
lill2=pygame.Rect(100,90,100,100)
pygame.draw.ellipse(ekraani_pind,(205,250,205),lill2)
lill3=pygame.Rect(100,10,100,100)
pygame.draw.ellipse(ekraani_pind,(205,250,205),lill3)
lill4=pygame.Rect(50,50,100,100)
pygame.draw.ellipse(ekraani_pind,(205,250,205),lill4)
lill5=pygame.Rect(150,50,100,100)
pygame.draw.ellipse(ekraani_pind,(205,250,205),lill5)
jaig=pygame.Rect(135,140,30,200)
pygame.draw.rect(ekraani_pind,(50,205,0),jaig)
lill1=pygame.Rect(100,50,100,100)
pygame.draw.ellipse(ekraani_pind,(255,0,255),lill1)
kaka1=pygame.Rect(120,80,10,10)
pygame.draw.ellipse(ekraani_pind,(100,50,200),kaka1)
kaka2=pygame.Rect(160,80,10,10)
pygame.draw.ellipse(ekraani_pind,(100,50,200),kaka2)
kaka3=pygame.Rect(120,100,50,10)
pygame.draw.ellipse(ekraani_pind,(25,0,55),kaka3)
kaka4=pygame.Rect(90,150,50,10)
pygame.draw.rect(ekraani_pind,(50,205,0),kaka4)
kaka5=pygame.Rect(140,180,90,10)
pygame.draw.rect(ekraani_pind,(50,205,0),kaka5)
kaka6=pygame.Rect(100,220,40,10)
pygame.draw.rect(ekraani_pind,(50,205,0),kaka6)
kaka7=pygame.Rect(100,70,80,10)
pygame.draw.rect(ekraani_pind,(0,125,0),kaka7)






pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: #функцмя для кнопки "выход" (крест)
        break
pygame.quit()
