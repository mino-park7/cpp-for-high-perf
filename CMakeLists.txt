cmake_minimum_required(VERSION 3.10)
project(cpp_for_high_perf VERSION 1.0)

# C++ 17 표준 사용
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# pybind11 설정
find_package(pybind11 CONFIG REQUIRED)

# Python 모듈 생성
pybind11_add_module(cpp_for_high_perf_core MODULE
    csrc/main.cpp
    python/bindings.cpp
)

# include 디렉토리 추가
target_include_directories(cpp_for_high_perf_core
    PRIVATE
    ${PROJECT_SOURCE_DIR}/include
)
