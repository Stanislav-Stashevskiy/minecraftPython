from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x + 3
y = pos.y
z = pos.z

a = int(input('введите первое число:'))
b = int(input('введите второе число:'))

if a > b:
    mc.setBlocks(x, y, z, x + 3, y + 3, z + 3, 5)

else:
    mc.setBlocks(x, y, z, x + 3, y + 3, z + 3, 1)
