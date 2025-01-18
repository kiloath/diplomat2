#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define DEMO01_RUN_EXPORT __declspec(dllexport)
#else
  #define DEMO01_RUN_EXPORT
#endif

DEMO01_RUN_EXPORT void demo01_run();
DEMO01_RUN_EXPORT void demo01_run_print_vector(const std::vector<std::string> &strings);
