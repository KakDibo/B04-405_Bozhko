#include <iostream>
void change(int x) {
    x = 100;
}

int main() {
    int a = 42;
    change(a);
    std::cout << change(a);  // 42 (не изменилось!)
}
