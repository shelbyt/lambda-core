cmake_minimum_required (VERSION 2.6)
project (Controller)
SET(LIBLOC "/home/shelbyt/research/gitprojects/lambda-core/lib")
SET(LIBLOCSO
    "/home/shelbyt/research/gitprojects/lambda-core/lib/libpqos.so.1.1.0")
SET(GCC_COVERAGE_COMPILE_FLAGS "-l${LIBLOC} -W -Wall -Wextra -Wstrict-prototypes
-Wmissing-prototypes
-Wmissing-declarations -Wold-style-definition -Wpointer-arith
-Wcast-qual -Wundef -Wwrite-strings  
-Wformat -Wformat-security -fstack-protector -fPIE
-D_FORTIFY_SOURCE=2 
-Wunreachable-code -Wmissing-noreturn -Wsign-compare
-Wno-endif-labels 
-g -O2")
#add_definitions(${GCC_COVERAGE_COMPILE_FLAGS})
#link_directories(${LIBLOC})
add_executable(controller controller.cpp)
target_link_libraries(controller ${LIBLOCSO})




