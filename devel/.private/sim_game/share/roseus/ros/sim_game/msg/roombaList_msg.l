;; Auto-generated. Do not edit!


(when (boundp 'sim_game::roombaList_msg)
  (if (not (find-package "SIM_GAME"))
    (make-package "SIM_GAME"))
  (shadow 'roombaList_msg (find-package "SIM_GAME")))
(unless (find-package "SIM_GAME::ROOMBALIST_MSG")
  (make-package "SIM_GAME::ROOMBALIST_MSG"))

(in-package "ROS")
;;//! \htmlinclude roombaList_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sim_game::roombaList_msg
  :super ros::object
  :slots (_header _roombaList _delta ))

(defmethod sim_game::roombaList_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:roombaList __roombaList) (let (r) (dotimes (i 0) (push (instance sim_game::roomba_msg :init) r)) r))
    ((:delta __delta) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _roombaList __roombaList)
   (setq _delta (float __delta))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:roombaList
   (&rest __roombaList)
   (if (keywordp (car __roombaList))
       (send* _roombaList __roombaList)
     (progn
       (if __roombaList (setq _roombaList (car __roombaList)))
       _roombaList)))
  (:delta
   (&optional __delta)
   (if __delta (setq _delta __delta)) _delta)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; sim_game/roomba_msg[] _roombaList
    (apply #'+ (send-all _roombaList :serialization-length)) 4
    ;; float64 _delta
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; sim_game/roomba_msg[] _roombaList
     (write-long (length _roombaList) s)
     (dolist (elem _roombaList)
       (send elem :serialize s)
       )
     ;; float64 _delta
       (sys::poke _delta (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; sim_game/roomba_msg[] _roombaList
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _roombaList (let (r) (dotimes (i n) (push (instance sim_game::roomba_msg :init) r)) r))
     (dolist (elem- _roombaList)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; float64 _delta
     (setq _delta (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get sim_game::roombaList_msg :md5sum-) "370246b649b0531a1f6b86644b0b7197")
(setf (get sim_game::roombaList_msg :datatype-) "sim_game/roombaList_msg")
(setf (get sim_game::roombaList_msg :definition-)
      "Header header

roomba_msg[] roombaList
float64 delta 
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sim_game/roomba_msg
Header header

int64 id 			# Roomba id
float64 x			# Roomba x pose
float64 y 			# Roomba y pose
bool removed		# Roomba removed
 
bool detected		# Roomba detected by drone
float64 static_x	# Last known x pose 
float64 static_y 	# Last known y pose
float64 r 			# Roomba probability radius
")



(provide :sim_game/roombaList_msg "370246b649b0531a1f6b86644b0b7197")


