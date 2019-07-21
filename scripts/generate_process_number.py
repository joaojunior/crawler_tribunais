def generate(year: str, j: str, tr: str, final: str, qty=10) -> str:
    for i in range(qty):
        n = int(f'{i}{year}{j}{tr}{final}00')
        digit = 98 - (n % 97)
        yield f'{i}-{digit}.{year}.{j}.{tr}.{final}'.rjust(25, '0')


def main():
    process_tjal = generate('2018', '8', '02', '0001')
    process_tjms = generate('2018', '8', '12', '0001')
    for process in [process_tjal, process_tjms]:
        for process_number in process:
            print(process_number)


if __name__ == '__main__':
    main()
