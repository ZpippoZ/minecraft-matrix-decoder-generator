import mcschematic
import time

schem = mcschematic.MCSchematic()

horizontal_bits=int(input("Input the number of bits of the horizontal decoder: "))
vertical_bits=int(input("Input the number of bits of the vertical decoder: "))


# Vertical decoder + matrix lines

for y in range(2**vertical_bits):
    value=list(bin(y)[2:].zfill(vertical_bits))
    for x in range(vertical_bits):
        schem.setBlock((x*2,y*2-2**vertical_bits*2,-1), "minecraft:red_stained_glass")
        schem.setBlock((x*2,y*2+1-2**vertical_bits*2,-2), "minecraft:red_stained_glass")
        schem.setBlock((x*2,y*2+1-2**vertical_bits*2,-1), "minecraft:redstone_wire[south=side,north=up]")
        schem.setBlock((x*2,y*2-2**vertical_bits*2,-2), "minecraft:redstone_wire[south=up,north=side]")
        schem.setBlock((x*2,y*2-2**vertical_bits*2,1), "minecraft:red_concrete")
        schem.setBlock((x*2-1,y*2-2**vertical_bits*2,1), "minecraft:red_concrete")
        schem.setBlock((x*2,y*2+1-2**vertical_bits*2,1), "minecraft:redstone_wire")
        schem.setBlock((x*2-1,y*2+1-2**vertical_bits*2,1), "minecraft:redstone_wire")

        if value[x]=='0':
            schem.setBlock((x*2,y*2-2**vertical_bits*2,0), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2+1-2**vertical_bits*2,0), "minecraft:repeater")
        if value[x]=='1':
            schem.setBlock((x*2,y*2+1-2**vertical_bits*2,0), "minecraft:red_concrete")
            schem.setBlock((x*2-1,y*2+1-2**vertical_bits*2,0),"minecraft:redstone_wall_torch[facing=west]")

        
        if not y % 8:
            schem.setBlock((x*2,y*2-2-2**vertical_bits*2, -3), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2-1-2**vertical_bits*2, -3), "minecraft:redstone_torch")
            schem.setBlock((x*2,y*2-2**vertical_bits*2, -3), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2-2**vertical_bits*2, -2), "minecraft:redstone_wall_torch[facing=south]")
            schem.setBlock((x*2,y*2-1-2**vertical_bits*2, -2), "minecraft:air")
            schem.setBlock((x*2,y*2-2**vertical_bits*2, -1), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2+1-2**vertical_bits*2, -2), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2-1-2**vertical_bits*2, -1), "minecraft:redstone_wire[north=side,south=side]")
    
    schem.setBlock((6+(vertical_bits-4)*2, y*2-2**vertical_bits*2, 2), "minecraft:red_concrete")
    schem.setBlock((6+(vertical_bits-4)*2, y*2+1-2**vertical_bits*2, 2), "minecraft:comparator[facing=north,mode=subtract]")
    for z in range(2**horizontal_bits):
        schem.setBlock((6+(vertical_bits-4)*2, y*2-2**vertical_bits*2, z*2+3), "minecraft:red_concrete")
        schem.setBlock((6+(vertical_bits-4)*2, y*2-2**vertical_bits*2, z*2+4), "minecraft:red_concrete")
        schem.setBlock((6+(vertical_bits-4)*2, y*2+1-2**vertical_bits*2, z*2+3), "minecraft:repeater[facing=north]" if not z % 8 else "minecraft:redstone_wire[north=side,south=side]")
        schem.setBlock((6+(vertical_bits-4)*2, y*2+1-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[north=side,south=side]")
        schem.setBlock((5+(vertical_bits-4)*2, y*2-2**vertical_bits*2, z*2+4), "minecraft:redstone_wall_torch[facing=west]")

for x in range(vertical_bits):
    schem.setBlock((x*2,-1,-2), "minecraft:air")
    schem.setBlock((x*2,-1, -1), "minecraft:redstone_wire[north=side,south=side]")


# Horizontal decoder + matrix towers

for z in range(2**horizontal_bits):
    for y in range(2**vertical_bits):
        schem.setBlock((7+(vertical_bits-4)*2, y*2-1-2**vertical_bits*2, z*2+4), "minecraft:red_concrete")
        schem.setBlock((8+(vertical_bits-4)*2, y*2-1-2**vertical_bits*2, z*2+4), "minecraft:red_stained_glass")
        schem.setBlock((9+(vertical_bits-4)*2, y*2-2**vertical_bits*2, z*2+4), "minecraft:red_stained_glass")
        schem.setBlock((7+(vertical_bits-4)*2, y*2-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[east=side,west=side]")
        schem.setBlock((8+(vertical_bits-4)*2, y*2-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[east=up,west=side]")
        schem.setBlock((9+(vertical_bits-4)*2, y*2-1-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[east=side,west=up]")

        if not y % 8:
            schem.setBlock((10+(vertical_bits-4)*2, y*2-1-2**vertical_bits*2, z*2+4), "minecraft:red_concrete")
            schem.setBlock((9+(vertical_bits-4)*2, y*2-2**vertical_bits*2, z*2+4), "minecraft:red_concrete")
            schem.setBlock((8+(vertical_bits-4)*2, y*2-1-2**vertical_bits*2, z*2+4), "minecraft:red_concrete")
            schem.setBlock((10+(vertical_bits-4)*2, y*2-3-2**vertical_bits*2, z*2+4), "minecraft:red_concrete")
            schem.setBlock((10+(vertical_bits-4)*2, y*2-2-2**vertical_bits*2, z*2+4), "minecraft:redstone_torch")
            schem.setBlock((9+(vertical_bits-4)*2, y*2-1-2**vertical_bits*2, z*2+4), "minecraft:redstone_wall_torch[facing=west]")

    schem.setBlock((7+(vertical_bits-4)*2, -1, z*2+4), "minecraft:red_concrete")
    schem.setBlock((9+(vertical_bits-4)*2, -2, z*2+4), "minecraft:air")
    schem.setBlock((8+(vertical_bits-4)*2, -2, z*2+4), "minecraft:redstone_wire[east=side,west=side]")
    schem.setBlock((9+(vertical_bits-4)*2, -3-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[east=side,west=side]")

    value=list(bin(z)[2:].zfill(horizontal_bits))
    for y in range(horizontal_bits):
        schem.setBlock((6+(vertical_bits-4)*2, y*2-2-horizontal_bits*2-2**vertical_bits*2, z*2+4), "minecraft:red_concrete")
        schem.setBlock((6+(vertical_bits-4)*2, y*2-2-horizontal_bits*2-2**vertical_bits*2, z*2+3), "minecraft:red_concrete")
        schem.setBlock((6+(vertical_bits-4)*2, y*2-1-horizontal_bits*2-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[north=side,south=side]")
        schem.setBlock((6+(vertical_bits-4)*2, y*2-1-horizontal_bits*2-2**vertical_bits*2, z*2+3), "minecraft:redstone_wire[north=side,south=side]" if z % 8 else "minecraft:repeater[facing=north]")
        schem.setBlock((7+(vertical_bits-4)*2, y*2-3-horizontal_bits*2-2**vertical_bits*2, z*2+4), "minecraft:red_stained_glass")
        schem.setBlock((8+(vertical_bits-4)*2, y*2-3-horizontal_bits*2-2**vertical_bits*2, z*2+4), "minecraft:red_stained_glass")
        schem.setBlock((8+(vertical_bits-4)*2, y*2-2-horizontal_bits*2-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[east=up,west=side]")
        schem.setBlock((9+(vertical_bits-4)*2, y*2-2-horizontal_bits*2-2**vertical_bits*2, z*2+4), "minecraft:red_stained_glass")
        schem.setBlock((9+(vertical_bits-4)*2, y*2-1-horizontal_bits*2-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[east=side,west=up]")
        schem.setBlock((7+(vertical_bits-4)*2, y*2-2-horizontal_bits*2-2**vertical_bits*2, z*2+4), "minecraft:repeater[facing=west]" if value[y]=='0' else "minecraft:redstone_wall_torch[facing=east]")

    schem.setBlock((9+(vertical_bits-4)*2, -3-2**vertical_bits*2, z*2+4), "minecraft:redstone_wire[east=side,west=side]")


schem.save("C:/Users/zPippo/curseforge/minecraft/Instances/Redstone/config/worldedit/schematics", str(2**horizontal_bits) + "by" + str(2**vertical_bits) + "matrixDecoder", mcschematic.Version.JE_1_20)
print("Schematic saved")
time.sleep(5)
