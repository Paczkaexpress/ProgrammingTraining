#include <iostream>

void simpleCallBack(int a)
{
    std::cout<<"Simple callback.\nValue is: "<<a<<std::endl;
}

void simpleCallBackTest(void (*callBack)(int))
{
    const int a = 5;

    callBack(a);
}

void simpleCallBackCalculator(float a, float b, float (*operation)(float, float))
{
    float result = operation(a,b);
    std::cout<<"The result of the operation is: "<<result<<std::endl;
}

struct MouseAction
{
    int changePosX;
    int changePosY;
    bool buttonLeftClick;
    bool buttonRightClick;
};

void simpleCallBackTest()
{
    std::cout<<"## Simple call-back example ##"<<std::endl;
    simpleCallBackTest(*simpleCallBack);

    std::cout<<"Calculator test\n"<<std::endl;
    simpleCallBackCalculator(3,2,[](float a, float b){
        return a + b;
    });

    simpleCallBackCalculator(3,2,[](float a, float b){
        return a - b;
    });

    simpleCallBackCalculator(3,2,[](float a, float b){
        return a * b;
    });

    simpleCallBackCalculator(3,2,[](float a, float b){
        return a / b;
    });
}

void mouseMoveXAction(MouseAction &mouse)
{
    if(mouse.changePosX == 0)
    {
        return;
    }
    std::cout<<"The mouse has been moved in x direction"<<std::endl;
    mouse.changePosX = 0;
}

void mouseMoveYAction(MouseAction &mouse)
{
    if(mouse.changePosY == 0)
    {
        return;
    }
    std::cout<<"The mouse has been moved in y direction"<<std::endl;
    mouse.changePosY = 0;
}

void mouseRightClickAction(MouseAction &mouse)
{
    if(mouse.buttonRightClick == false)
    {
        return;
    }
    std::cout<<"The right button of the mouse has been clicked"<<std::endl;
    mouse.buttonRightClick = false;
}

void mouseLeftClickAction(MouseAction &mouse)
{
    if(mouse.buttonLeftClick == false)
    {
        return;
    }
    std::cout<<"The left button of the mouse has been clicked"<<std::endl;
    mouse.buttonLeftClick = false;
}
void fcnPointerArrayCallBack()
{
    std::cout<<"## Function array ##"<<std::endl;
    MouseAction mouse = {2,4, true, false};

    void (*fcnPtr[])(MouseAction &mouse) = 
        {(*mouseMoveXAction), (*mouseMoveYAction), 
        (*mouseRightClickAction), (*mouseLeftClickAction)};

    for(int i = 0; i < 4; ++i)
    {
        (*fcnPtr[static_cast<int>(i)])(mouse);
    }
}

int main(int argc, char* argv[])
{
    simpleCallBackTest();
    fcnPointerArrayCallBack();

    return 0;
}