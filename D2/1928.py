from base64 import b64decode


for t in range(int(input())):

    word = input()
    result = b64decode(word).decode('UTF-8')

    print(f'#{t+1} {result}')