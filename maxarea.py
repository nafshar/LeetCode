def maxarea(heights):
    maxar = 0
    for i in range(len(heights)-1):
        for j in range(1, len(heights)):
            area = min(heights[i], heights[j]) * (j-i)
            if area >= maxar:
                maxar = area
    return maxar


#heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
heights = [1,0,0,0,0,0,0,2,2]
mxr = maxarea(heights)
print(mxr)
