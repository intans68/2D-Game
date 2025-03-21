import pygame
from copy import deepcopy

pygame.init()
win = pygame.display.set_mode((800,400))
fon = pygame.image.load("FON.jpg")

level = [[0,300, 400,400,],[500, 800, 0,300]]

#kirp = pygame.image.load("KIRP.jpg")



x = 100
y = 200

poz = x
widht = 60
height = 60
speed = 5
x_speed =20
vprige = False
jumpCount = 10
i_p = 9
grav = 3
padat = False


# map = [[0,300,300,400],[301,200,500,400],[501,350,800,400],[0,0,150,150],[151,0,800,5]]


karta = [0000000000000000000000000000,
         1000000000000000000000000111,
         1000000000000000000000010111,
         1000000001111110000111000000,
         1000000000000000000000000000,
         1001000000000000000000000000,
         1011110000000000000000000000,
         1111111111111111111111111111


         ]

string = 0
coll = 0
map =[]
for i in karta:
    i = str(i)
    for s in i:
        s = int(s)
        if s == 1:
            li = []
            li.append(1+string)
            li.append(1 + coll)
            li.append(1 + string+49)
            li.append(1 + coll+49)
            map.append(li)
            string += 50

        else:
            string += 50
    coll+=50
    string = 0


print(map)












run = True

while run:
    globals()
    pygame.time.delay(50)


    coord_hero = [x,y,x+widht,y+height]



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if vprige == False:  #падение

        list3 = []
        list4 = []
        for el in map:
            list3 = [s for s in range(el[0]-widht+1, el[2]+widht+1)]

            if coord_hero[0] in list3 and coord_hero[2] in list3 and el[1]>=coord_hero[3]:

                list4.append(el[1])

        if len(list4) == 1:

            show = y + height
            if show < list4[0]:
                show += speed*grav
                if show < list4[0]:
                    y += speed*grav
                    grav+=1
                    padat = True
                else:
                    y = list4[0] - height-1
                    padat = False
                    grav = 3

        elif len(list4) > 1:

            ss = min(list4, key=lambda x: abs(x - coord_hero[3]))


            show2 = y + height

            if show2 < ss:
                show2 += speed*grav

                if show2 < ss:
                    y += speed*grav
                    grav += 1
                    padat = True
                else:
                    y = ss - height-1
                    padat = False
                    grav = 3







        #if mask_y1 >  y+height:
         #   y += speed*grav
          #  grav += 1
           # padat = True
        #else:
         #   grav = 4
          #  padat = False


    if vprige == False and padat == False: # если не в прыжке

        if keys[pygame.K_SPACE]: # запускаем прыжок
            vprige = True
            print(vprige)
    if  vprige == True:  # запускаем прыжок
        list5 = []
        verh_objeckt = []
        niz_objeckt = []
        for el in map:
            list5 = [s for s in range(el[0]-widht+1, el[2]+widht+1)] # границы объекта с котороми персонаж может взаимодействовать
            if coord_hero[0] in list5 and coord_hero[2] in list5 and el[3]<coord_hero[1]: # если обе его координаты попадают в координаты объекта и !!! низ объекта находится выше верха персонажа
                niz_objeckt.append(el[3]) # добавляем нижние координаты объектов в список

        if len(niz_objeckt)==1:
            sn = niz_objeckt[0]
            print(sn)
        elif len(niz_objeckt)>1:
            sn = max(niz_objeckt)
        else:
            sn=0



        print(niz_objeckt)
        show3 = coord_hero[1]
        if  show3 > sn:  # если верх персонажа ниже достинг низа платформы
            print("FFFFFFFFFF")
            if i_p != 0:  # если  счетчик прыжка не равно нулю (НЕ ПРЫГАЛИ ЕЩЕ) - прыгаем
                show3 -= speed * i_p
                if show3 > sn:
                    y -= speed * i_p
                    i_p -= 1
                else:
                    y = sn
                    i_p = 9
                    vprige = False
            else:
                i_p = 9
                vprige = False








    if keys[pygame.K_LEFT] and x>0 : # ЛЕВО
        list2 = []
        list = [s for s in range(y, y+height+ 1)]
        for el in map:
            if (el[1] in list or el[3] in list) and x>=el[2]:
                list2.append(el[2])
        if len(list2) == 0:
            x -= x_speed
        else:
            sll = max(list2)
            show4 = coord_hero[0]
            if show4 >sll:
                show4 -= x_speed
                if show4 >sll:
                    x -= x_speed
                else:
                    x = sll+1



    if keys[pygame.K_RIGHT]: # ПРАВО
        list1 = []
        list = [s for s in range(y, y + height + 1)]
        for el in map:
            if (el[1] in list or el[3] in list) and x <= el[0]:
                list1.append(el[0])

        print(list1)
        if len(list1) == 0:
            x += x_speed
        else:
            sp = min(list1)
            show3 = coord_hero[2]
            if show3 <sp:
                show3 += x_speed
                if show3 <sp:
                    x += x_speed
                else:
                    x = sp -widht







    win.blit(fon, (0, 0))




    if x <= poz:
        for i in map:
            pygame.draw.rect(win, (0, 100, 100), (i[0], i[1], 50, 50))
        pygame.draw.rect(win, (0, 0, 255), (x, y, widht, height))

    else:
        for i in map:
            pygame.draw.rect(win, (0, 100, 100), (-x+i[0]+poz, i[1], 50, 50))
        pygame.draw.rect(win, (0, 0, 255), (poz, y, widht, height))

    pygame.display.update()


        #win.blit(fon, (-x+poz, 0))
        #pygame.draw.rect(win, (0, 0, 255), (poz, y, widht, height))














