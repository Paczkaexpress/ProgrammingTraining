#include <iostream>

class Pytriples
{
    public:
    
    int x;
    int y;
    int z;

    Pytriples()
    {
        this->x = 1;
        this->y = 1;
        this->z = 1;    
    }

    void next()
    {
        do
        {
            if (this->y <= this->z)
            {
                ++this->y;
            }
            else
            {
                if (this->x <= this->z)
                {
                    ++this->x;
                }
                else
                {
                    this->x = 1;
                    ++this->z;
                }
                this->y = this->x;
            }
        } while ((this->x * this->x + this->y * this->y) != (this->z * this->z));
    }
};

int main()
{
    Pytriples py;

    std::cout<<py.x<<" "<<py.y<<" "<<py.z<<std::endl;
    py.next();
    std::cout<<py.x<<" "<<py.y<<" "<<py.z<<std::endl;
    py.next();
    std::cout<<py.x<<" "<<py.y<<" "<<py.z<<std::endl;
    py.next();
    std::cout<<py.x<<" "<<py.y<<" "<<py.z<<std::endl;
}