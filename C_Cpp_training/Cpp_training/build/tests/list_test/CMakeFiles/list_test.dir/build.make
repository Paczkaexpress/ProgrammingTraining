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
include tests/list_test/CMakeFiles/list_test.dir/depend.make

# Include the progress variables for this target.
include tests/list_test/CMakeFiles/list_test.dir/progress.make

# Include the compile flags for this target's objects.
include tests/list_test/CMakeFiles/list_test.dir/flags.make

tests/list_test/CMakeFiles/list_test.dir/list.cpp.o: tests/list_test/CMakeFiles/list_test.dir/flags.make
tests/list_test/CMakeFiles/list_test.dir/list.cpp.o: ../tests/list_test/list.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/paczynsk/src/ProgrammingTraining/Cpp_training/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object tests/list_test/CMakeFiles/list_test.dir/list.cpp.o"
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/tests/list_test && /home/paczynsk/src/sdk/sysroots/x86_64-oesdk-linux/usr/bin/x86_64-linux-gnu-g++   -m64 --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/list_test.dir/list.cpp.o -c /home/paczynsk/src/ProgrammingTraining/Cpp_training/tests/list_test/list.cpp

tests/list_test/CMakeFiles/list_test.dir/list.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/list_test.dir/list.cpp.i"
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/tests/list_test && /home/paczynsk/src/sdk/sysroots/x86_64-oesdk-linux/usr/bin/x86_64-linux-gnu-g++   -m64 --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/paczynsk/src/ProgrammingTraining/Cpp_training/tests/list_test/list.cpp > CMakeFiles/list_test.dir/list.cpp.i

tests/list_test/CMakeFiles/list_test.dir/list.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/list_test.dir/list.cpp.s"
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/tests/list_test && /home/paczynsk/src/sdk/sysroots/x86_64-oesdk-linux/usr/bin/x86_64-linux-gnu-g++   -m64 --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu --sysroot=/home/paczynsk/src/sdk/sysroots/x86_64-linux-gnu $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/paczynsk/src/ProgrammingTraining/Cpp_training/tests/list_test/list.cpp -o CMakeFiles/list_test.dir/list.cpp.s

# Object files for target list_test
list_test_OBJECTS = \
"CMakeFiles/list_test.dir/list.cpp.o"

# External object files for target list_test
list_test_EXTERNAL_OBJECTS =

tests/list_test/list_test: tests/list_test/CMakeFiles/list_test.dir/list.cpp.o
tests/list_test/list_test: tests/list_test/CMakeFiles/list_test.dir/build.make
tests/list_test/list_test: tests/list_test/CMakeFiles/list_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/paczynsk/src/ProgrammingTraining/Cpp_training/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable list_test"
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/tests/list_test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/list_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/list_test/CMakeFiles/list_test.dir/build: tests/list_test/list_test

.PHONY : tests/list_test/CMakeFiles/list_test.dir/build

tests/list_test/CMakeFiles/list_test.dir/clean:
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/tests/list_test && $(CMAKE_COMMAND) -P CMakeFiles/list_test.dir/cmake_clean.cmake
.PHONY : tests/list_test/CMakeFiles/list_test.dir/clean

tests/list_test/CMakeFiles/list_test.dir/depend:
	cd /home/paczynsk/src/ProgrammingTraining/Cpp_training/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/paczynsk/src/ProgrammingTraining/Cpp_training /home/paczynsk/src/ProgrammingTraining/Cpp_training/tests/list_test /home/paczynsk/src/ProgrammingTraining/Cpp_training/build /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/tests/list_test /home/paczynsk/src/ProgrammingTraining/Cpp_training/build/tests/list_test/CMakeFiles/list_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/list_test/CMakeFiles/list_test.dir/depend

