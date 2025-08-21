import imageio.v3 as iio

filenames = ['sp1.png', 'sp2.png', 'sp3.png', 'sp4.png', 'sp5.png', 'sp6.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))
    
iio.imwrite('team.gif', images, duration = 500, loop = 0)