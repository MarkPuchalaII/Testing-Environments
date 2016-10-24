mass1          = 0.512
mass2          = 0.508
massWithWeight = 0.609
        #0    1      2  3      4      5      6  7
data = [[1, -0.3976, 0, 3, -0.0806, -0.3126, 6, 7],
        [2, -0.4549, 0, 3, -0.0907, -0.3389, 6, 7],
        [3, -0.4564, 0, 3, -0.1940, -0.2103, 6, 7],
        [4, -0.3772, 0, 3, -0.1820, -0.1737, 6, 7],
        [5, -0.2359, 0, 3,  0.0094, -0.2068, 6, 7],
        [6, -0.2201, 0, 3,  0.0036, -0.1814, 6, 7],
        [7, -0.1919, 0, 3,  0.0319, -0.2004, 6, 7],
        [8, -0.2276, 0, 3,  0.0218, -0.1762, 6, 7]]

def dataBack(data):
    data = [[1, -0.3976, 0, 3, -0.0806, -0.3126, 6, 7],
            [2, -0.4549, 0, 3, -0.0907, -0.3389, 6, 7],
            [3, -0.4564, 0, 3, -0.1940, -0.2103, 6, 7],
            [4, -0.3772, 0, 3, -0.1820, -0.1737, 6, 7],
            [5, -0.2359, 0, 3,  0.0094, -0.2068, 6, 7],
            [6, -0.2201, 0, 3,  0.0036, -0.1814, 6, 7],
            [7, -0.1919, 0, 3,  0.0319, -0.2004, 6, 7],
            [8, -0.2276, 0, 3,  0.0218, -0.1762, 6, 7]]
    return data

def kinetics(m,v):
    return(m * v**2) / 2

def velocity(data):
    caption = '                Velocity of Carts: Before & After Collision'
    table(data, caption)


def momentum(data):
    count = 1
    for each in data:
        each[1] *= mass1
        each[4] *= mass1
        if count < 7:
            each[2] *= mass2
            each[5] *= mass2
        else:
            each[2] *= massWithWeight
            each[5] *= massWithWeight
        each[3] = each[1] + each[2]
        each[6] = each[4] + each[5]
        each[7] = each[6] / each[3]
        count += 1


    caption = '                Momentum of Carts: Before & After Collision'
    table(data, caption)

def energy(data):
    count = 1
    for each in data:
        each[1] = kinetics(mass1,each[1])
        each[4] = kinetics(mass1,each[4])
        if count < 7:
            each[2] = kinetics(mass2,each[2])
            each[5] = kinetics(mass2,each[5])
        else:
            each[2] = kinetics(massWithWeight,each[2])
            each[5] = kinetics(massWithWeight,each[5])
        each[3] = each[1] + each[2]
        each[6] = each[4] + each[5]
        each[7] = each[3] / each[6]
        count += 1

    caption = '                  Energy of Carts: Before & After Collision'
    table(data, caption)

def table(data,caption):
	print(caption)
	print('R |--------------------------------------------------------------------')
	print('U |         Before Collision      |        After Collision       | Ratio')
	print('N |   Cart 1  | Cart 2 | Total p  |  Cart 1 |  Cart 2 | Total p  | A / B')
	for each in data:
		print(each[0],'| ',
		      "{:<6}".format(round(each[1],4)),' |', "{:<6}".format(round(each[2],4)),'| ', "{:<7}".format(round(each[3],4)),'|',
                      "{:<7}".format(round(each[4],4)), '|', "{:<7}".format(round(each[5],4)),'|',  "{:<7}".format(round(each[6],4)),' |',
                      "{:<6}".format(round(each[7],4)))
