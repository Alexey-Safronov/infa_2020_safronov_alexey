#include <iostream>

using namespace std;

int main()
{
    int N,x,i;
    int bigmax, max, lilmin, min;
    bigmax = max = -10000;
    min = lilmin = 10000;
    cin >> N;
    for(i = 0; i < N; i++){
        cin >> x;
        if (x > bigmax){
            max = bigmax;
            bigmax = x;
        } else if (x > max) {
        max = x;}

        if (x < lilmin){
            min = lilmin;
            lilmin = x;

        } else if (x < min){
        min = x;}

    }
    cout << bigmax << " " << max << "\n" << lilmin << " " << min;
    return 0;
}
