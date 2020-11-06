cmake_minimum_required(VERSION 3.16.5)

project(cpp_training CXX)

enable_testing()
find_package(GTest REQUIRED)
add_subdirectory(${GTEST_INCLUDE_DIR})

add_subdirectory(call_back)
add_subdirectory(list_implementation)
add_subdirectory(tests)