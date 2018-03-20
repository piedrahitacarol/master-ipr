#include <vector>
#include <fstream>

#define DEFAULT_FILE "/home/yo/repos/2018-ptmr/map1/map1.csv"

class Node
{
public:
    Node(int x,int y,int id,int parentId) {
      _x = x; _y = y;
      _id = id; _parentId = parentId;
    }

    int _x,_y,_id,_parentId;
};

class Program
{
public:
    bool run()
    {
        std::string fileName = DEFAULT_FILE;
        file.open(fileName);
        if( ! file.is_open() )
        {
              printf("Not able to open file: %s\n",fileName.c_str());
              return false;
        }
        printf("Opened file: %s\n",fileName.c_str());


        return true;
    }

private:
    std::vector<std::vector<int>> mapInt;  //0empty,1wall,2visited,3start,4end
    std::vector<Node*> nodes;
    std::ifstream file;
};

int main()
{
    Program program;
    if( ! program.run() )
        return 1;
    return 0;
}
