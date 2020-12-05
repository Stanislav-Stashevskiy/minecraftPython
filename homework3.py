from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x, y, z, x + 10, y + 7, z + 10, 89)
mc.setBlocks(x + 1, y + 1, z + 1, x + 9, y + 6, z + 9, 0)
mc.setBlocks(x + 3, y + 2, z, x + 7, y + 3, z, 20)
mc.setBlocks(x + 10, y + 2, z + 1, x + 10, y + 4, z + 9, 20)
mc.setBlocks(x + 10, y + 2, z + 1, x + 10, y + 3, z + 1, 0)
mc.setBlocks(x + 10, y + 2, z + 1, x + 10, y + 2, z + 1, 64)

mc.setBlocks(x, y  + 7, z, x + 10, y + 14, z + 10, 89)
mc.setBlocks(x + 1, y + 8, z + 1, x + 9, y + 13, z + 9, 0)
mc.setBlocks(x + 3, y + 9, z, x + 7, y + 12, z, 20)
mc.setBlocks(x + 10, y + 11, z + 1, x + 10, y + 14, z + 9, 20)
mc.setBlocks(x + 10, y + 11, z + 1, x + 10, y + 12, z + 1, 0)
mc.setBlocks(x + 10, y + 11, z + 1, x + 10, y + 11, z + 1, 64)

mc.setBlocks(x, y + 15, z, x + 10, y + 15, z + 10, 12)
mc.setBlocks(x + 1, y + 15, z + 1, x + 9, y + 15, z + 9, 11)
