h, b, c, s = map(int, input().split())
out = (h * b * c * s) / 8

print("%.1f MB" % (out / (1024 * 1024)))
