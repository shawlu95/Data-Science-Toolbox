def csv_parser(delimiter=','):
    field = []
    while True:
        char = (yield(''.join(field)))
        field = []

        leading_whitespace = []
        while char and char == ' ':
            leading_whitespace.append(char)
            char = (yield)

        if char == '"' or char == "'":
            suround = char
            char = (yield)
            while True:
                if char == suround:
                    char = (yield)
                    if char != suround:
                        break

                field.append(char)
                char = (yield)

            while not char == delimiter:
                if not char:
                    (yield(''.join(field)))
                char = (yield)
        else:
            field = leading_whitespace
            while char != delimiter:
                if not char:
                    (yield(''.join(field)))
                field.append(char)
                char = (yield)

def parser(s):
    queue = list(s)
    cells = []
    while queue:
        cell = []
        leading = []
        c = queue.pop(0)

        while c == " ":
            leading.append(c)
            if not queue:
                break
            c = queue.pop(0)

        if c == "\"":
            c = queue.pop(0)
            while True:
                if c == "\"":
                    c = queue.pop(0)
                    if c != "\"":
                        break
                cell.append(c)
                if not queue:
                    break
                c = queue.pop(0)
        else:
            cell += leading
            while c != ",":
                cell.append(c)
                if not queue:
                    break
                c = queue.pop(0)
        cells.append("".join(cell))
    return cells


def parse_csv(csv_text):
    processor = csv_parser()
    next(processor)

    split_result = []
    for c in list(csv_text) + [None]:
        emit = processor.send(c)
        if emit:
            split_result.append(emit)

    return split_result


s = '1997,Ford,E350,"Super, luxurious truck"'
s = 'Weronika,Zaborska,njkfdsv@dsgfk.sn,"running, sci-fi",new,Krakow,25'
s = 'Ryuichi,Akiyama,jkg@ljnsfd.fjn,music,guide,Tokyo,65'
s = 'Elena, 42 years old, is from Valencia and is interested in cooking, traveling.'
s = 'Elena,Martinez,emrt@lsofnbr.rt,"cooking, traveling",superhost,Valencia,42'
s = '"John ""Mo""",Smith,sfn@flkaei.km,biking and hiking,,"Seattle, WA",23'

print(list("   1  2"))
# print(parse_csv(s))

idx_fname = 0
idx_age = 6
idx_city = 5
idx_interests = 3
formatter = "%s, %s years old, is from %s and is interseted in %s."
cells = parser(s)
print(formatter%(cells[idx_fname],
                 cells[idx_age],
                 cells[idx_city],
                 cells[idx_interests]))

# submission
import sys


class Parser:
    key_fname = "first_name"
    key_lname = "last_name"
    key_email = "email"
    key_interests = "interests"
    key_notes = "notes"
    key_city = "city"
    key_age = "age"
    formatter = "%s, %s years old, is from %s and is interested in %s."
    keys = [key_fname, key_lname, key_email, key_interests, key_notes, key_city, key_age]

    # default delimitor is comma, but user may specify as needed
    def __init__(self, delimitor=","):
        self.delimitor = delimitor

    # Time complexity: O(n), each character is read once
    # Space complexity: O(n), use use queue to represent line, and cells as storage space
    def parseLine(self, line):
        # process the line/row as a queue, remove "\n" at the end
        queue = list(line[:-1])

        # storing delimitor-separated cells
        cells = []

        while queue:
            c = queue.pop(0)

            # word buffer
            cell = []

            # handle leading space
            leading = []
            while c == " ":
                leading.append(c)
                if not queue:
                    break
                c = queue.pop(0)

            # if char is quote, ignore delimitor until end quote
            if c == "\"":
                c = queue.pop(0)
                while True:
                    if c == "\"":
                        # quote ended
                        c = queue.pop(0)
                        if c != "\"":
                            break
                    cell.append(c)
                    if not queue:
                        break
                    c = queue.pop(0)
            else:
                # while char is not delimitor, add to buffer
                cell += leading
                while c != self.delimitor:
                    cell.append(c)
                    if not queue:
                        break
                    c = queue.pop(0)

            # when reaching an end quote or a delimitor, a whole cell has been retrieved
            cells.append("".join(cell))

        return {self.keys[i]: cells[i] for i in range(len(self.keys))}

    def getBio(self, line):
        cells = self.parseLine(line)
        return self.formatter % (cells[self.key_fname],
                                 cells[self.key_age],
                                 cells[self.key_city],
                                 cells[self.key_interests])


parser = Parser()
for line in sys.stdin:
    print(parser.getBio(line))

