def create_door_mat(n,m):

    for i in range(1,n,2):
        pattern = (".|." * i).center(m, '-')
        print(pattern)


    word = "WELCOME"
    w_count = int((m - len(word))/2)

    print("-"*w_count + word + "-"*w_count)

    for i in range(n-2,0,-2):
        pattern = (".|." * i).center(m, '-')
        print(pattern)

if __name__ == "__main__":
    n = int(input("Enter an odd natural number (X): "))
    m = n * 3
    create_door_mat(n, m)