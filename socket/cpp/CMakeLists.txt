cmake_minimum_required(VERSION 3.12)

project(socket_server)
project(socket_client)


include_directories(${Boost_INCLUDE_DIR})
find_package(Boost REQUIRED COMPONENTS system regex)


add_executable(socket_server server.cpp)
add_executable(socket_client client.cpp)


target_link_libraries(socket_client ${Boost_LIBRARIES})
target_link_libraries(socket_server ${Boost_LIBRARIES})