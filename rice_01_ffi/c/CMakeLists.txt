cmake_minimum_required(VERSION 3.15)
project(demo01_run CXX)



add_executable(demo01_run src/demo01_run.cpp src/main.cpp)



install(TARGETS demo01_run DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
