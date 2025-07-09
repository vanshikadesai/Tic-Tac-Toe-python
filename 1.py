def wateri(water):
    min_water=float('inf')
    max_water=0

    for k in water:
        min_water=min(min_water,k)
        pro=k-min_water
        max_water=max(max_water,pro)
        area=max_water*max_water

    return area
water=[1,2,3,4,8,3]
print(wateri(water))
