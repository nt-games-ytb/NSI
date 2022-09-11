                                                                                                                                                                                                            
'''                                                                                                                                                                                                    dddddddd
MMMMMMMM               MMMMMMMM                                           tttt                                                  MMMMMMMM               MMMMMMMM  iiii                               d::::::d
M:::::::M             M:::::::M                                        ttt:::t                                                  M:::::::M             M:::::::M i::::i                              d::::::d
M::::::::M           M::::::::M                                        t:::::t                                                  M::::::::M           M::::::::M  iiii                               d::::::d
M:::::::::M         M:::::::::M                                        t:::::t                                                  M:::::::::M         M:::::::::M                                     d:::::d 
M::::::::::M       M::::::::::M  aaaaaaaaaaaaa      ssssssssss   ttttttt:::::ttttttt        eeeeeeeeeeee    rrrrr   rrrrrrrrr   M::::::::::M       M::::::::::Miiiiiiinnnn  nnnnnnnn        ddddddddd:::::d 
M:::::::::::M     M:::::::::::M  a::::::::::::a   ss::::::::::s  t:::::::::::::::::t      ee::::::::::::ee  r::::rrr:::::::::r  M:::::::::::M     M:::::::::::Mi:::::in:::nn::::::::nn    dd::::::::::::::d 
M:::::::M::::M   M::::M:::::::M  aaaaaaaaa:::::ass:::::::::::::s t:::::::::::::::::t     e::::::eeeee:::::eer:::::::::::::::::r M:::::::M::::M   M::::M:::::::M i::::in::::::::::::::nn  d::::::::::::::::d 
M::::::M M::::M M::::M M::::::M           a::::as::::::ssss:::::stttttt:::::::tttttt    e::::::e     e:::::err::::::rrrrr::::::rM::::::M M::::M M::::M M::::::M i::::inn:::::::::::::::nd:::::::ddddd:::::d 
M::::::M  M::::M::::M  M::::::M    aaaaaaa:::::a s:::::s  ssssss       t:::::t          e:::::::eeeee::::::e r:::::r     r:::::rM::::::M  M::::M::::M  M::::::M i::::i  n:::::nnnn:::::nd::::::d    d:::::d 
M::::::M   M:::::::M   M::::::M  aa::::::::::::a   s::::::s            t:::::t          e:::::::::::::::::e  r:::::r     rrrrrrrM::::::M   M:::::::M   M::::::M i::::i  n::::n    n::::nd:::::d     d:::::d 
M::::::M    M:::::M    M::::::M a::::aaaa::::::a      s::::::s         t:::::t          e::::::eeeeeeeeeee   r:::::r            M::::::M    M:::::M    M::::::M i::::i  n::::n    n::::nd:::::d     d:::::d 
M::::::M     MMMMM     M::::::Ma::::a    a:::::assssss   s:::::s       t:::::t    tttttte:::::::e            r:::::r            M::::::M     MMMMM     M::::::M i::::i  n::::n    n::::nd:::::d     d:::::d 
M::::::M               M::::::Ma::::a    a:::::as:::::ssss::::::s      t::::::tttt:::::te::::::::e           r:::::r            M::::::M               M::::::Mi::::::i n::::n    n::::nd::::::ddddd::::::dd
M::::::M               M::::::Ma:::::aaaa::::::as::::::::::::::s       tt::::::::::::::t e::::::::eeeeeeee   r:::::r            M::::::M               M::::::Mi::::::i n::::n    n::::n d:::::::::::::::::d
M::::::M               M::::::M a::::::::::aa:::as:::::::::::ss          tt:::::::::::tt  ee:::::::::::::e   r:::::r            M::::::M               M::::::Mi::::::i n::::n    n::::n  d:::::::::ddd::::d
MMMMMMMM               MMMMMMMM  aaaaaaaaaa  aaaa sssssssssss              ttttttttttt      eeeeeeeeeeeeee   rrrrrrr            MMMMMMMM               MMMMMMMMiiiiiiii nnnnnn    nnnnnn   ddddddddd   ddddd
'''                                                                                                                                                                                                         

# Paint 3D                                                                                                                                                                                             
'''from PIL import Image

# creating a object
im = Image.open('./MasterMind/images.jpeg')
  
im.show()'''


'''from IPython.display import Image
Image('./MasterMind/images.jpeg')'''

'''import IPython.display as display
from PIL import Image
display.display(Image.open('./MasterMind/images.jpeg'))'''

# Tableau
'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('./MasterMind/images.jpeg')
imgplot = plt.imshow(img)
plt.show()'''

# Ouvre une forme
'''
import cv2

img = cv2.imread('./MasterMind/images.jpeg',0)
cv2.imshow('./MasterMind/images.jpeg',img)'''

'''
import os
os.system('./MasterMind/images.jpeg')'''

'''from simshow import simshow
simshow('./MasterMind/images.jpeg')  # display from local file'''

def tri_insertion(T):
    for i in range(1,len(T)):
        # mémoriser T[i] dans x
        x = T[i]                            

        # décaler les éléments T[0]..T[i-1] qui sont plus grands que x, en partant de T[i-1]
        j = i                               
        
        while j > 0 and T[j - 1] > x:
            T[j] = T[j - 1]
            j = j - 1

        # placer x dans le "trou" laissé par le décalage
        T[j] = x 
    #return T
    print(T)

#tri_insertion([9,4,5,1,7,6])

def tri_selection(t):
    n = len(t) 
    for i in range(0, n): #for i in range(0, n - 2):
        min = i       
        for j in range(i + 1, n): #for j in range(i + 1, n - 1):
            if t[j] < t[min]:
                min = j
        
        if min != i:
            t[i], t[min] = t[min], t[i]
    #return t
    print(t)

tri_selection([9,4,5,1,7,6])


"""une fonction crepier(pile de crêpe):
    n <- longeur de la pile#nombre de crêpes
    c <- pile de crêpe(0) #crêpe

    tant que 
    si c < c + 1:"""


def dichotomique (tab, x):
    """
    :param res: booléen qui indique si un élèment x se trouve ou non dans le tableau tab
    :param tab: tableau contenant différents élèments déjà triés
    :param x: élèment recherché
    """
    res = False
    
    if tab == []:
        return res

    else:
        n = len(tab) #--> 9
        milieu = n//2 #plus tard check si c'est un float #--> 4

        if tab[milieu] == x:
            res = True
            return res

        if tab[milieu] < x:
            #créer le nouveau tableau
            tab1 = []
            for i in range(milieu): 
                tab1 = tab1 + tab[milieu+i]

    


    pass

dichotomique([1,2,6,9,12,14,18,21,42], 14)

def correction(tab, x):