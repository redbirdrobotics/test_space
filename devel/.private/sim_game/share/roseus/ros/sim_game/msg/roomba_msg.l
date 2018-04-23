;; Auto-generated. Do not edit!


(when (boundp 'sim_game::roomba_msg)
  (if (not (find-package "SIM_GAME"))
    (make-package "SIM_GAME"))
  (shadow 'roomba_msg (find-package "SIM_GAME")))
(unless (find-package "SIM_GAME::ROOMBA_MSG")
  (make-package "SIM_GAME::ROOMBA_MSG"))

(in-package "ROS")
;;//! \htmlinclude roomba_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sim_game::roomba_msg
  :super ros::object
  :slots (_header _id _x _y _detected _static_x _static_y _r ))

(defmethod sim_game::roomba_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:id __id) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:detected __detected) nil)
    ((:static_x __static_x) 0.0)
    ((:static_y __static_y) 0.0)
    ((:r __r) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _id (round __id))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _detected __detected)
   (setq _static_x (float __static_x))
   (setq _static_y (float __static_y))
   (setq _r (float __r))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:detected
   (&optional __detected)
   (if __detected (setq _detected __detected)) _detected)
  (:static_x
   (&optional __static_x)
   (if __static_x (setq _static_x __static_x)) _static_x)
  (:static_y
   (&optional __static_y)
   (if __static_y (setq _static_y __static_y)) _static_y)
  (:r
   (&optional __r)
   (if __r (setq _r __r)) _r)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int64 _id
    8
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; bool _detected
    1
    ;; float64 _static_x
    8
    ;; float64 _static_y
    8
    ;; float64 _r
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int64 _id
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _id (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _id) (= (length (_id . bv)) 2)) ;; bignum
              (write-long (ash (elt (_id . bv) 0) 0) s)
              (write-long (ash (elt (_id . bv) 1) -1) s))
             ((and (class _id) (= (length (_id . bv)) 1)) ;; big1
              (write-long (elt (_id . bv) 0) s)
              (write-long (if (>= _id 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _id s)(write-long (if (>= _id 0) 0 #xffffffff) s)))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _detected
       (if _detected (write-byte -1 s) (write-byte 0 s))
     ;; float64 _static_x
       (sys::poke _static_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _static_y
       (sys::poke _static_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _r
       (sys::poke _r (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int64 _id
#+(or :alpha :irix6 :x86_64)
      (setf _id (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _id (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _detected
     (setq _detected (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float64 _static_x
     (setq _static_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _static_y
     (setq _static_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _r
     (setq _r (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get sim_game::roomba_msg :md5sum-) "ff0d2705bf902e1f7a93e5088d820b1d")
(setf (get sim_game::roomba_msg :datatype-) "sim_game/roomba_msg")
(setf (get sim_game::roomba_msg :definition-)
      "Header header

int64 id 			# Roomba id
float64 x			# Roomba x pose
float64 y 			# Roomba y pose
 
bool detected		# Roomba detected by drone
float64 static_x	# Last known x pose 
float64 static_y 	# Last known y pose
float64 r 			# Roomba probability radius
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

")



(provide :sim_game/roomba_msg "ff0d2705bf902e1f7a93e5088d820b1d")


