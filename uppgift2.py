def uppgift2_1a():
    answer = 0

    for i in range(1, 11):
        answer += i

    print("Summan av talen 1 till 10 är: " + str(answer))


def uppgift2_1b():
    answer = 0

    for i in range(1, 101):
        answer += i

    print("Summan av talen 1 till 100 är: " + str(answer))


def uppgift2_1c():
    answer = 0
    i = 1

    while i <= 100:
        answer += i
        i += 1

    print("Summan av talen 1 till 100 är: " + str(answer))


def uppgift2_2():
    numbers = [1, -2, 3, -2, 4, -3]
    answer = 0

    for number in numbers:
        answer += number

    print("Summan av elementen i listan är: " + str(answer))


def uppgift2_3a():
    movies = ["Alien", "Gladiator", "Inception", "Interstellar"]

    print(movies)


def uppgift2_3b():
    movies = ["Alien", "Gladiator", "Inception", "Interstellar"]

    movies.append("Fellowship of the ring")

    print(movies)


def uppgift2_3c():
    movies = ["Alien", "Gladiator", "Inception", "Interstellar"]

    movies.append("Fellowship of the ring")
    movies.insert(0, "The two towers")

    print(movies)


def uppgift2_3d():
    movies = ["Alien", "Gladiator", "Inception", "Interstellar"]

    movies.append("Fellowship of the ring")
    movies.insert(0, "The two towers")

    index = movies.index("Fellowship of the ring")

    print("Fellowship of the ring har index: " + str(index))


def uppgift2_3e():
    movies = ["Alien", "Gladiator", "Inception", "Interstellar"]

    movies.append("Fellowship of the ring")
    movies.insert(0, "The two towers")

    index_before = movies.index("Fellowship of the ring")

    movies.remove("Alien")

    index_after = movies.index("Fellowship of the ring")

    print(movies)
    print("Index före borttagning: " + str(index_before))
    print("Index efter borttagning: " + str(index_after))


def uppgift2_3f():
    movies = ["Alien", "Gladiator", "Inception", "Interstellar"]

    movies.append("Fellowship of the ring")
    movies.insert(0, "The two towers")
    movies.remove("Alien")

    print("Listans längd är: " + str(len(movies)))


def uppgift2_3g():
    movies = ["Alien", "Gladiator", "Inception", "Interstellar"]

    movies.append("Fellowship of the ring")
    movies.insert(0, "The two towers")
    movies.remove("Alien")

    movies.reverse()

    print(movies)


def uppgift2_3h():
    movies = ["Alien", "Gladiator", "Inception", "Interstellar"]

    movies.append("Fellowship of the ring")
    movies.insert(0, "The two towers")
    movies.remove("Alien")
    movies.reverse()
    movies.sort()

    print(movies)