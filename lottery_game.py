import random

if __name__ == '__main__':
    random_list = random.sample(range(1, 50), 10)
    print('******** Luck Draw *********')
    print(sorted(random_list))
