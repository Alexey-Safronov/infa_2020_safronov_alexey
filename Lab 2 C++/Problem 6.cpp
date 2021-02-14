#include <iostream>

using namespace std;

int main()
{
    int k = 0;
    int m = 0;
    int x;
    cin >> x;
    while (x != 0){

        if (x > m) {
            m = x;
            k = 1;
        } else if (x == m) {
        ++k;}
        cin >> x;
    }
    cout << k;
    return 0;
}
