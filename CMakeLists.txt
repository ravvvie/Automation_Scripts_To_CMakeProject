# general info
cmake_minimum_required(VERSION 3.10)
set(PROJECT_NAME FightclubGame)
project(${PROJECT_NAME} VERSION 1.0.0)

# common options
if(WIN32)
    message("Running on Windows")
elseif(LINUX)
    message("Running on Linux")
endif()
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
message("Output binaries directory: ${CMAKE_BINARY_DIR}/bin")
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ${PROJECT_NAME})
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CMAKE_SUPPRESS_REGENERATION TRUE)

# cpp options
set( CMAKE_CXX_STANDARD 20)


#app options
set(SOURCES Source/Utils/Math.cpp Source/Game/Weapon.cpp Source/main.cpp Source/Game/Character.cpp)
set(INCLUDES Source/Utils/Math.h Source/Game/Weapon.h Source/Game/Character.h)


source_group("Source files/Utils" FILES Source/Utils/Math.cpp)
source_group("Header files/Utils" FILES Source/Utils/Math.h)

source_group("Source files/Game" FILES Source/Game/Character.cpp)
source_group("Source files/Game" FILES Source/Game/Weapon.cpp)

source_group("Header files/Game" FILES Source/Game/Weapon.h)
source_group("Header files/Game" FILES Source/Game/Character.h)


add_executable(${PROJECT_NAME} ${SOURCES} ${INCLUDES})

#includes
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/Source)

message("Using ${CMAKE_CXX_COMPILER_ID} compiler")



if (MSVC)
    message("UsingMSVC")
    message("MSVC current version: ${MSVC_VERSION}")
    message("MSVC toolset version: ${MSVC_TOOLSET_VERSION}")
    target_compile_definitions(${PROJECT_NAME} PRIVATE /FAC)    
endif()


message( "Compiler flags: ${CMAKE_CXX_FLAGS}")
message("Configuration types: ${CMAKE_CONFIGURATION_TYPES}")
