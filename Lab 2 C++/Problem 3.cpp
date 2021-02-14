#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int a;
    int i;
    std::cin >> a;
        for (i = 2; i <= sqrt(a); i++){
        while (a % i == 0){
            a = a / i;
            std::cout << i;
            std::cout << "\n";
        }

}
  if (a != 1) {std::cout << a;
                     std::cout << "\n";}
    return 0;
}

