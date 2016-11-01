import sys

sRad = 0.007
mRad = 0.016
lRad = 0.025
small = ['small', 177.45, '',174.7, '', 173.72, '']
small[1] = round(     small[1]*sRad, 2)
small[2] = round(((abs(small[1]-1)/1)*100),2)
small[3] = round(     small[3]*sRad, 2)
small[4] = round((abs(small[3]-1)/1)*100,2)
small[5] = round(     small[5]*sRad, 2)
small[6] = round((abs(small[5]-1)/1)*100,2)

medio = ['medium',  63.65,  '',63.66, '',  63.38, '']
medio[1] = round(     medio[1]*mRad, 2)
medio[2] = round((abs(medio[1]-1)/1)*100,2)
medio[3] = round(     medio[3]*mRad, 2)
medio[4] = round((abs(medio[3]-1)/1)*100,2)
medio[5] = round(     medio[5]*mRad, 2)
medio[6] = round((abs(medio[5]-1)/1)*100,2)

large = ['large',  39.29,  '',39.11, '',  38.99, '']
large[1] = round(     large[1]*lRad, 2)
large[2] = round((abs(large[1]-1)/1)*100,2)
large[3] = round(     large[3]*lRad, 2)
large[4] = round((abs(large[3]-1)/1)*100,2)
large[5] = round(     large[5]*lRad, 2)
large[6] = round((abs(large[5]-1)/1)*100,2)

caption = "Change in Angular Position (rad)"
array = [small, medio, large]

def a(array):
    caption = "{:<35}".format("Change in Angular Position (rad)")

def l(array):
    caption = "{:<35}".format("Change in Linear Position (m)")
    print(caption)
    print('|--------------------------------------------------------------------')
    print('     Size | Trial 1 | % Error | Trial 2 | % Error | Trial 3 | % Error')
    for data in array:
        for each in data:
            sys.stdout.write('|'+"{:<9}".format(each))
        print()

def table(array, caption):
    print(caption)
    print('|--------------------------------------------------------------------')
    print('     Size | Trial 1 | Trial 2 | Trial 3 | Radius')
    for data in array:
        for each in data:
            sys.stdout.write('|',"{:<9}".format(each))
        print()
