#include "Singleton.hpp"

Singleton* Singleton::instance = nullptr;

Singleton* Singleton::getInstance() {
    if ( instance == nullptr ) {
        instance = new Singleton();
    }
    return instance;
}

double Singleton::getPrivateValue() {
    return this->privateValue;
}

Singleton::Singleton()
{
    privateValue = 3.1415;
}