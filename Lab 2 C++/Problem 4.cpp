#include <iostream>
#include <cmath>

using namespace std;

int prime(int n){
    int a = 2;
    int k = 0;
    int flag = 1;
    int i;
    while (k != n){
        for (i = 2; i <= sqrt(a); i++){
            if (a % i == 0) {
                flag = 0;
            }
        }

        if (flag == 1){
                k++;
        }
        flag = 1;
        a++;
    }
    return a-1;
}

int main()
{
    int n;
    int s;
    std::cin >> n;
    s = prime(n);
    std::cout << s;

    return 0;
}
