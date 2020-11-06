cmake_minimum_required(VERSION 3.16.5)

project(list_training)

add_executable(${PROJECT_NAME} list.cpp)

add_library(list list.cpp)