#include <iostream>

using namespace std;

int main()
{

    int N;
    std::cin >> N;
    for (int i = 0; i < N; i++) {
            for (int i = 0; i < N; i++){
                std::cout << "*";
            }
            std::cout << "\n";
    }
    return 0;
}
