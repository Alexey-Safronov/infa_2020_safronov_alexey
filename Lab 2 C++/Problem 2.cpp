#include <iostream>

using namespace std;

int main()
{
    int a,s;
    std::cin >> a;
    s = a / 100 + (a / 10) % 10 + a % 10;
    std::cout << s;
    return 0;
}
