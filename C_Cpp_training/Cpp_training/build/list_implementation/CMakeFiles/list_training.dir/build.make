# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/paczynsk/src/sdk/sysroots/x86_64-oesdk-linux/usr/bin/cmake

# The command to remove a file.
RM = /home/paczynsk/src/sdk/sysroots/x86_64-oesdk-linux/usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/paczynsk/src/ProgrammingTraining/Cpp_training

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/paczynsk/src/ProgrammingTraining/Cpp_training/build

# Include any dependencies generated for this target.
include list_implementation/CMakeFiles/list_training.dir/depend.make

# Include the progress variables for this target.
include list_implementation/CMakeFiles/list_training.dir/progress.make

# Include the compile flags for this target's objects.
include list_implementation/CMakeFiles/list_training.dir/flags.make

list_implementation/CMakeFiles/list_training.dir/list.cpp.o: list_implementation/CMakeFiles/list_training.dir/flags.make
list_implementation/CMakeFiles/list_training.dir/list.cpp.o: ../list_implementation/list.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/paczynsk/src/ProgrammingTraining/Cpp_training/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object list_implementation/CMakeFiles/list_training.dir/list.cpp.o"
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/list_implementation && /home/paczynsk/src/sdk/sysroots/x86_64-oesdk-linux/usr/bin/x86_64-linux-gnu-g++   -m64 --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/list_training.dir/list.cpp.o -c /home/paczynsk/src/ProgrammingTraining/Cpp_training/list_implementation/list.cpp

list_implementation/CMakeFiles/list_training.dir/list.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/list_training.dir/list.cpp.i"
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/list_implementation && /home/paczynsk/src/sdk/sysroots/x86_64-oesdk-linux/usr/bin/x86_64-linux-gnu-g++   -m64 --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/paczynsk/src/ProgrammingTraining/Cpp_training/list_implementation/list.cpp > CMakeFiles/list_training.dir/list.cpp.i

list_implementation/CMakeFiles/list_training.dir/list.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/list_training.dir/list.cpp.s"
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/list_implementation && /home/paczynsk/src/sdk/sysroots/x86_64-oesdk-linux/usr/bin/x86_64-linux-gnu-g++   -m64 --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/paczynsk/src/ProgrammingTraining/Cpp_training/list_implementation/list.cpp -o CMakeFiles/list_training.dir/list.cpp.s

# Object files for target list_training
list_training_OBJECTS = \
"CMakeFiles/list_training.dir/list.cpp.o"

# External object files for target list_training
list_training_EXTERNAL_OBJECTS =

list_implementation/list_training: list_implementation/CMakeFiles/list_training.dir/list.cpp.o
list_implementation/list_training: list_implementation/CMakeFiles/list_training.dir/build.make
list_implementation/list_training: list_implementation/CMakeFiles/list_training.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/paczynsk/src/ProgrammingTraining/Cpp_training/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable list_training"
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/list_implementation && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/list_training.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
list_implementation/CMakeFiles/list_training.dir/build: list_implementation/list_training

.PHONY : list_implementation/CMakeFiles/list_training.dir/build

list_implementation/CMakeFiles/list_training.dir/clean:
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/list_implementation && $(CMAKE_COMMAND) -P CMakeFiles/list_training.dir/cmake_clean.cmake
.PHONY : list_implementation/CMakeFiles/list_training.dir/clean

list_implementation/CMakeFiles/list_training.dir/depend:
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/paczynsk/src/ProgrammingTraining/Cpp_training /home/paczynsk/src/ProgrammingTraining/Cpp_training/list_implementation /home/paczynsk/src/ProgrammingTraining/Cpp_training/build /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/list_implementation /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/list_implementation/CMakeFiles/list_training.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : list_implementation/CMakeFiles/list_training.dir/depend

