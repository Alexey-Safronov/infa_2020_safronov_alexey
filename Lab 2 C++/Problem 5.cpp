#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int x;
    bool flag = false;
    cin >> x;
    int a,b,c,d;
    for(a = 0; a <= sqrt(x) && !flag; a++){
        for(b = 0; b <= sqrt(x) && !flag; b++){
            for(c = 0; c <= sqrt(x) && !flag; c++){
                for(d = 0; d <= sqrt(x) && !flag; d++){
                    if (a*a + b*b + c*c + d*d == x){
                        flag = true;
                        cout << a << "\n" << b << "\n" << c << "\n" << d;
                    }
                }
            }
        }
    }


    return 0;
}
