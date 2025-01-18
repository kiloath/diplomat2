#include "demo01_run.h"
#include <vector>
#include <string>

int main() {
    demo01_run();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    demo01_run_print_vector(vec);
}
