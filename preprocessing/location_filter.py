def location_filter(data, lat, lon) :
    filtered = list()
    x = list()

    for i in range(0,len(data)):
        if data[i][0] < lat[0] or data[i][0]>lat[1]:
            filtered.append(data[i])
    for i in range(0,len(filtered)):
        if filtered[i][1] < lon[0] or data[i][1] > lon[1]:
            x.append(filtered)

    for i in x:
        filtered.remove(i)
