cmake_minimum_required(VERSION 3.15)
project(diplomat_example C)

include(ExternalProject)
ExternalProject_Add(
        rust_code
        SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/..
        CONFIGURE_COMMAND ""
        BUILD_COMMAND cargo build
        INSTALL_COMMAND ""
)

set(RUST_LIB_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../target/debug/libdiplomat_example.a")

add_executable(${PROJECT_NAME} main.c)
target_link_libraries(${PROJECT_NAME} ${RUST_LIB_PATH} dl pthread m)
set(CMAKE_EXE_LINKER_FLAGS "-static")

# add_custom_command(
#         TARGET ${PROJECT_NAME} POST_BUILD
#         COMMAND ${CMAKE_COMMAND} -E copy_if_different
#         "${CMAKE_CURRENT_SOURCE_DIR}/../../target/debug/libdiplomat_example.so"
#         "${CMAKE_BINARY_DIR}"
# )
# export LD_LIBRARY_PATH=$(pwd):$LD_LIBRARY_PATH