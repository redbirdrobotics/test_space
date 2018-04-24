// Auto-generated. Do not edit!

// (in-package sim_game.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let roomba_msg = require('./roomba_msg.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class roombaList_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.roombaList = null;
      this.delta = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('roombaList')) {
        this.roombaList = initObj.roombaList
      }
      else {
        this.roombaList = [];
      }
      if (initObj.hasOwnProperty('delta')) {
        this.delta = initObj.delta
      }
      else {
        this.delta = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type roombaList_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [roombaList]
    // Serialize the length for message field [roombaList]
    bufferOffset = _serializer.uint32(obj.roombaList.length, buffer, bufferOffset);
    obj.roombaList.forEach((val) => {
      bufferOffset = roomba_msg.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [delta]
    bufferOffset = _serializer.float64(obj.delta, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type roombaList_msg
    let len;
    let data = new roombaList_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [roombaList]
    // Deserialize array length for message field [roombaList]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.roombaList = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.roombaList[i] = roomba_msg.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [delta]
    data.delta = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.roombaList.forEach((val) => {
      length += roomba_msg.getMessageSize(val);
    });
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sim_game/roombaList_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '370246b649b0531a1f6b86644b0b7197';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new roombaList_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.roombaList !== undefined) {
      resolved.roombaList = new Array(msg.roombaList.length);
      for (let i = 0; i < resolved.roombaList.length; ++i) {
        resolved.roombaList[i] = roomba_msg.Resolve(msg.roombaList[i]);
      }
    }
    else {
      resolved.roombaList = []
    }

    if (msg.delta !== undefined) {
      resolved.delta = msg.delta;
    }
    else {
      resolved.delta = 0.0
    }

    return resolved;
    }
};

module.exports = roombaList_msg;
