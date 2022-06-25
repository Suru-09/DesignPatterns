#include <iostream>

#include "Singleton.hpp"

int main() {

    auto single = Singleton::getInstance();
    std::cout << "I am private value: " << single->getPrivateValue() << "\n";

    auto second_single = Singleton::getInstance();
    std::cout << "Another instance?: " << single->getPrivateValue() << "\n";

    return 0;
}