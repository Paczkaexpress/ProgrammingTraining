cmake_minimum_required(VERSION 3.16.5)

project(list_tests)

add_library(list-test_lib list.cpp)

add_executable(${PROJECT_NAME} list.cpp)
