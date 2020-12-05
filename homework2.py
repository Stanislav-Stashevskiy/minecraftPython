from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y - 1
z = pos.z

block = mc.getBlock(x, y, z)

if block == 2:
    mc.setBlock(x, y, z, 8)

else:
    mc.setBlock(x, y, z, 2)
