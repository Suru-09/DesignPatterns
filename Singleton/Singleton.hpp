#ifndef SINGLETON_HPP
#define SINGLETON_HPP

#include <iostream>

class Singleton {
public:
    static Singleton* getInstance();
    double getPrivateValue();
private:
    static Singleton* instance;
    double privateValue;
    Singleton();
};



#endif