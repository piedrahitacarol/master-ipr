#include <vector>
#include <fstream>
#include <sstream>

#define DEFAULT_FILE "/home/yo/map1.csv"
#define DEFAULT_START_X 2
#define DEFAULT_START_Y 2
#define DEFAULT_END_X 7
#define DEFAULT_END_Y 2

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
    bool parseFileLine(std::vector<int>& intsOnFileLine)
    {
        intsOnFileLine.clear();

        if( file.eof() )
            return false;

        std::string s;
        getline(file, s);
        std::stringstream ss(s);

        int d;
        while (ss >> d)
            intsOnFileLine.push_back(d);

        return true;
    }

    void dump()
    {
        for(int i=0;i<intMap.size();i++)
        {
            for(int j=0;j<intMap[0].size();j++)
            {
                printf("%d ",intMap[i][j]);
            }
            printf("\n");
        }

    }

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

        std::vector<int> intsOnFileLine;

        while( this->parseFileLine(intsOnFileLine) )
        {
            if ( intsOnFileLine.size() == 0 ) continue;

            intMap.push_back( intsOnFileLine );
        }

        file.close();

        intMap[DEFAULT_START_X][DEFAULT_START_Y] = 3;
        intMap[DEFAULT_END_X][DEFAULT_END_Y] = 4;
        this->dump();

        return true;
    }

private:
    std::vector<std::vector<int>> intMap;  //0empty,1wall,2visited,3start,4end
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
