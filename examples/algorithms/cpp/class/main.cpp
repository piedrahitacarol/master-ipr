#include <vector>
#include <fstream>


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
        return true;
    }

private:
    std::vector<Node*> nodes;
};

int main()
{
    Program program;
    if( ! program.run() )
        return 1;
    return 0;
}
