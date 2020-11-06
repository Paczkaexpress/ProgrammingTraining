cmake_minimum_required(VERSION 3.16.5)

project(CallBackTests)

add_executable(${PROJECT_NAME} call_back.cpp)

add_library(call_back call_back.cpp)