class FibGenerator:

    def generateFibonacci(self, length):
        seq = [1, 1]
        to_generate = length - len(seq)
        if to_generate > 0:
            for i in range(to_generate):
                current = seq[len(seq) - 1] + seq[len(seq) - 2]
                seq.append(current)
        if length > 0:
            return seq[0:length]
        else:
            return []


def main():
    print(FibGenerator().generateFibonacci(15))


if __name__ == "__main__":
    main()
