def main():
    n , k = map(int, input().split())
    result = (factorial(n)) / (factorial(n-k)*factorial(k))
    print(int(result))
    
def factorial(number: int) -> int:
    result = 1
    for i in range(2, number+1):
        result *= i
    return result

main()