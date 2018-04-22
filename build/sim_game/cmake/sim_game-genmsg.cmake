# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "sim_game: 2 messages, 0 services")

set(MSG_I_FLAGS "-Isim_game:/home/alexander/test_space/src/sim_game/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(sim_game_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg" NAME_WE)
add_custom_target(_sim_game_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sim_game" "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg" "sim_game/roomba_msg:std_msgs/Header"
)

get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg" NAME_WE)
add_custom_target(_sim_game_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sim_game" "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sim_game
)
_generate_msg_cpp(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sim_game
)

### Generating Services

### Generating Module File
_generate_module_cpp(sim_game
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sim_game
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(sim_game_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(sim_game_generate_messages sim_game_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_cpp _sim_game_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_cpp _sim_game_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sim_game_gencpp)
add_dependencies(sim_game_gencpp sim_game_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sim_game_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sim_game
)
_generate_msg_eus(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sim_game
)

### Generating Services

### Generating Module File
_generate_module_eus(sim_game
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sim_game
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(sim_game_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(sim_game_generate_messages sim_game_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_eus _sim_game_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_eus _sim_game_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sim_game_geneus)
add_dependencies(sim_game_geneus sim_game_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sim_game_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sim_game
)
_generate_msg_lisp(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sim_game
)

### Generating Services

### Generating Module File
_generate_module_lisp(sim_game
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sim_game
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(sim_game_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(sim_game_generate_messages sim_game_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_lisp _sim_game_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_lisp _sim_game_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sim_game_genlisp)
add_dependencies(sim_game_genlisp sim_game_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sim_game_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sim_game
)
_generate_msg_nodejs(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sim_game
)

### Generating Services

### Generating Module File
_generate_module_nodejs(sim_game
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sim_game
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(sim_game_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(sim_game_generate_messages sim_game_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_nodejs _sim_game_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_nodejs _sim_game_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sim_game_gennodejs)
add_dependencies(sim_game_gennodejs sim_game_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sim_game_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sim_game
)
_generate_msg_py(sim_game
  "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sim_game
)

### Generating Services

### Generating Module File
_generate_module_py(sim_game
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sim_game
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(sim_game_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(sim_game_generate_messages sim_game_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roombaList_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_py _sim_game_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexander/test_space/src/sim_game/msg/roomba_msg.msg" NAME_WE)
add_dependencies(sim_game_generate_messages_py _sim_game_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sim_game_genpy)
add_dependencies(sim_game_genpy sim_game_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sim_game_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sim_game)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sim_game
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(sim_game_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sim_game)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sim_game
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(sim_game_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sim_game)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sim_game
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(sim_game_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sim_game)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sim_game
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(sim_game_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sim_game)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sim_game\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sim_game
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(sim_game_generate_messages_py std_msgs_generate_messages_py)
endif()
