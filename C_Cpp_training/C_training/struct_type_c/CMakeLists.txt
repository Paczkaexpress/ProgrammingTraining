cmake_minimum_required(VERSION 2.8.11)

project(StructTestC)

add_executable(${PROJECT_NAME} struct_c.cpp)

add_library(struct_c struct_c.cpp)