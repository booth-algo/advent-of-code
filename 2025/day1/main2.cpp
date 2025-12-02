#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

struct Instruction
{
    std::string direction;
    int num;
};

Instruction parse(std::string line)
{
    Instruction instruction;
    std::string st1 = "", st2 = "";
    for (auto c : line)
    {
        if (isalpha(c))
        {
            st1 += c;
        }
        else if (isdigit(c))
        {
            st2 += c;
        }
    }
    instruction.direction = st1;
    instruction.num = std::stoi(st2);

    return instruction;
}

int main()
{
    std::ifstream file("data.txt");
    std::string line;

    std::vector<Instruction> instructions;
    int val = 50;
    int count = 0;

    while (std::getline(file, line))
    {
        instructions.push_back(parse(line));
    }

    for (Instruction instr : instructions)
    {
        for (int i = 0; i < instr.num; i++)
        {
            int delta = (instr.direction == "L") ? -1 : 1;
            val = (val + delta) % 100;
            if (val == 0)
            {
                count++;
            }
        }
    }

    std::cout << count << std::endl;

}