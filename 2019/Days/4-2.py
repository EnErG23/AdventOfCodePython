req2 = [245182, 790572]

i = req2[0]

result = 0

while i < req2[1] + 1:
    asStr = str(i)

    req3 = False
    for j in range(1, len(asStr)):
        if asStr[j - 1] == asStr[j]:
            req3 = True
            if j < len(asStr)-1:
                j += 1
            elif asStr[j - 2] == asStr[j]:
                req3 = False

    req4 = True
    for j in range(1, len(asStr)):
        if int(asStr[j - 1]) > int(asStr[j]):
            req4 = False
            break

    if req3 and req4:
        print(i)
        result += 1

    i += 1

print(result)
