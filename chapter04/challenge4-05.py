def a(seisuu):
    try:
        return float(seisuu)
    except (ValueError,TypeError):
        print("syousuu")

b = a(11)
print(b)

