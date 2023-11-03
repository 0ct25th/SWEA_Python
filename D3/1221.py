# 정렬용 알파벳
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for t in range(int(input())):
    n = list(map(str, input().split()))

    # 영어 단어로 된 숫자들을 공백으로 구분하여 입력받아, number_list 리스트에 저장
    number_list = list(map(str, input().split()))

    # 각 숫자가 몇 번 등장하는지 세는 데 사용
    chk = [0] * 10

    # number_list의 각 원소에 대해, 그 원소가 nums 리스트의 몇 번째에 있는지 찾아 chk 리스트의 해당 인덱스를 증가
    for i in number_list:
        chk[nums.index(i)] += 1

    print(f"#{t+1}")
    # chk 리스트의 각 원소에 대해, 그 원소가 나타내는 숫자를 해당 횟수만큼 반복해 출력
    for i in range(10):
        result = nums[i] + " "
        print(f"{result * chk[i]}", end="")
