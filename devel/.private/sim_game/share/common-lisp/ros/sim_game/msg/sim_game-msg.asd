
(cl:in-package :asdf)

(defsystem "sim_game-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "roombaList_msg" :depends-on ("_package_roombaList_msg"))
    (:file "_package_roombaList_msg" :depends-on ("_package"))
    (:file "roomba_msg" :depends-on ("_package_roomba_msg"))
    (:file "_package_roomba_msg" :depends-on ("_package"))
  ))