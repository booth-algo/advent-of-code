import re

def parser(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    rules_pattern = re.compile(r"(\d+)\|(\d+)")
    print_pattern = re.compile(r"^\d+(,\d+)*$")
    
    rules_list = []
    print_list = []

    for line in lines:
        rules_match = rules_pattern.match(line)
        print_match = print_pattern.match(line)
        if rules_match:
            first = int(rules_match.group(1))
            second = int(rules_match.group(2))
            rules_list.append((first,second))
        if print_match:
            numbers = [int(num) for num in line.split(',')]
            print_list.append(numbers)

    rule_graph = {}

    for rule in rules_list:
        if rule[0] not in rule_graph:
            rule_graph[rule[0]] = []

        rule_graph[rule[0]].append(rule[1])

    return rule_graph, print_list

def part1(rule_graph, print_list):
    for print_line in print_list:
        for num in print_line:
            rule_graph[num] 
        

def main():
    rule_graph, print_list = parser('test_input.txt')
    print(rule_graph)
    print(print_list)


if __name__ == "__main__":
    main()

