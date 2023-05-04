def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x

def thegcd(num, arr):
    num1 = arr[0]
    num2 = arr[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(arr)):
        gcd = find_gcd(gcd, arr[i])

    return(gcd)



def my_gcd():
    numbers = [2, 4, 6, 8, 16]
    gcd = thegcd(5, numbers)
    print(gcd)

if __name__ == "__main__":
    my_gcd()