ice_cream_chocolate = int(input('введите количество шоколадного мороженного:'))
ice_cream_strawberry = int(input('введите количество клубничного мороженного:'))
ice_cream_vanilla = 5

if ice_cream_chocolate != 0:
    print('беру шоколадное!')
elif ice_cream_chocolate == 0 and ice_cream_strawberry != 0:
    print('беру клубничное!')
else:
    print('беру ванильное!')
