R = int(input())
G = int(input())
B = int(input())

hex_R = hex(R)[2:].upper().zfill(2)

hex_G = hex(G)[2:].upper().zfill(2)

hex_B = hex(B)[2:].upper().zfill(2)

color_hexadecimal = f"#{hex_R}{hex_G}{hex_B}"

print(color_hexadecimal)