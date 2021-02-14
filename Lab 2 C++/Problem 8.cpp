#include <iostream>

using namespace std;

int main()
{
    int a,b,i,m;
    bool flag = false;
    cin >> a >> b >> m;
    for(i = 0; i<=m && !flag; i++){
        if (a*i%m == b){
            cout << i;
            flag = true;
        }
    }
    if (!flag){
        cout << -1;
    }
    return 0;
}
