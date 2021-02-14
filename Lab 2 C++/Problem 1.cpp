#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double a,b,c;
    double p;
    std::cin >> a >> b >> c;

    if (b < c){
        p = b;
        b = c;
        c = p;
    }
    if (a < c){
        p = a;
        a = c;
        c = p;

    }

   if (a < b){
        p = a;
        a = b;
        b = p;
   }


   if (b + c <= a) {
        std::cout << "impossible";
   } else
   if (a > sqrt(b*b+c*c)) {
        std::cout << "obtuse";
   }
   if (a == sqrt(b*b+c*c)) {
        std::cout << "right";
   }
   if (a < sqrt(b*b+c*c)) {
        std::cout << "acute";
   }




    return 0;
}
