#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int x,i,j;
    int a,b = 0;
    bool flag = false;
    cin >> x;
    for(i = 0; i <= sqrt(x) && !flag; i++){
        for(j = 0; j <= sqrt(x) && !flag; j++){
            if ( i*i*i + j*j*j == x){
                flag = true;
                cout << i << "\n" << j;
            }
        }
    }
    if (!flag) {
        cout << "impossible";
    }
    return 0;
}
