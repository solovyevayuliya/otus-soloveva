cmake_minimum_required(VERSION 3.25)
project(server)
link_libraries(ws2_32 wsock32)

set(CMAKE_CXX_STANDARD 17)

add_executable(server main.c)
