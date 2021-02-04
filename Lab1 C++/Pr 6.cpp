#include <iostream>

using namespace std;

int main()
{

    int N;
    std::cin >> N;
    for (int i = 0; i < N; i++) {
            for (int k = 0; k < i; k++){
                std::cout << " ";
            }
            for (int j = 0; j < N-2*i; j++){
                std::cout << "*";
            }
            for (int k = 0; k < i+1; k++){
                std::cout << " ";
            }
            std::cout << "\n";
    }
    return 0;
}
