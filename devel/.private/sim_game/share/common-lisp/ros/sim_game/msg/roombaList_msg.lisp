; Auto-generated. Do not edit!


(cl:in-package sim_game-msg)


;//! \htmlinclude roombaList_msg.msg.html

(cl:defclass <roombaList_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (roombaList
    :reader roombaList
    :initarg :roombaList
    :type (cl:vector sim_game-msg:roomba_msg)
   :initform (cl:make-array 0 :element-type 'sim_game-msg:roomba_msg :initial-element (cl:make-instance 'sim_game-msg:roomba_msg))))
)

(cl:defclass roombaList_msg (<roombaList_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <roombaList_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'roombaList_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sim_game-msg:<roombaList_msg> is deprecated: use sim_game-msg:roombaList_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <roombaList_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sim_game-msg:header-val is deprecated.  Use sim_game-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'roombaList-val :lambda-list '(m))
(cl:defmethod roombaList-val ((m <roombaList_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sim_game-msg:roombaList-val is deprecated.  Use sim_game-msg:roombaList instead.")
  (roombaList m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <roombaList_msg>) ostream)
  "Serializes a message object of type '<roombaList_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'roombaList))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'roombaList))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <roombaList_msg>) istream)
  "Deserializes a message object of type '<roombaList_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'roombaList) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'roombaList)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'sim_game-msg:roomba_msg))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<roombaList_msg>)))
  "Returns string type for a message object of type '<roombaList_msg>"
  "sim_game/roombaList_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'roombaList_msg)))
  "Returns string type for a message object of type 'roombaList_msg"
  "sim_game/roombaList_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<roombaList_msg>)))
  "Returns md5sum for a message object of type '<roombaList_msg>"
  "3241d533defe0b3d361b06117825fe36")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'roombaList_msg)))
  "Returns md5sum for a message object of type 'roombaList_msg"
  "3241d533defe0b3d361b06117825fe36")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<roombaList_msg>)))
  "Returns full string definition for message of type '<roombaList_msg>"
  (cl:format cl:nil "Header header~%~%roomba_msg[] roombaList~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sim_game/roomba_msg~%Header header~%~%int64 id 			#Roomba id~%float64 x			#Roomba x pose~%float64 y 			#Roomba y pose~%~%bool detected		#Roomba detected by drone~%float64 r 			#Roomba probability radius~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'roombaList_msg)))
  "Returns full string definition for message of type 'roombaList_msg"
  (cl:format cl:nil "Header header~%~%roomba_msg[] roombaList~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sim_game/roomba_msg~%Header header~%~%int64 id 			#Roomba id~%float64 x			#Roomba x pose~%float64 y 			#Roomba y pose~%~%bool detected		#Roomba detected by drone~%float64 r 			#Roomba probability radius~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <roombaList_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'roombaList) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <roombaList_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'roombaList_msg
    (cl:cons ':header (header msg))
    (cl:cons ':roombaList (roombaList msg))
))