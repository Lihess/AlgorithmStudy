w, h, b= map(int, input().split())
out = (w * h * b) / 8

print("%.2f MB" % (out / (1024 * 1024)))
