// Generated by gencpp from file sim_game/roomba_msg.msg
// DO NOT EDIT!


#ifndef SIM_GAME_MESSAGE_ROOMBA_MSG_H
#define SIM_GAME_MESSAGE_ROOMBA_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace sim_game
{
template <class ContainerAllocator>
struct roomba_msg_
{
  typedef roomba_msg_<ContainerAllocator> Type;

  roomba_msg_()
    : header()
    , id(0)
    , x(0.0)
    , y(0.0)
    , removed(false)
    , detected(false)
    , static_x(0.0)
    , static_y(0.0)
    , r(0.0)  {
    }
  roomba_msg_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , id(0)
    , x(0.0)
    , y(0.0)
    , removed(false)
    , detected(false)
    , static_x(0.0)
    , static_y(0.0)
    , r(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int64_t _id_type;
  _id_type id;

   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef uint8_t _removed_type;
  _removed_type removed;

   typedef uint8_t _detected_type;
  _detected_type detected;

   typedef double _static_x_type;
  _static_x_type static_x;

   typedef double _static_y_type;
  _static_y_type static_y;

   typedef double _r_type;
  _r_type r;





  typedef boost::shared_ptr< ::sim_game::roomba_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sim_game::roomba_msg_<ContainerAllocator> const> ConstPtr;

}; // struct roomba_msg_

typedef ::sim_game::roomba_msg_<std::allocator<void> > roomba_msg;

typedef boost::shared_ptr< ::sim_game::roomba_msg > roomba_msgPtr;
typedef boost::shared_ptr< ::sim_game::roomba_msg const> roomba_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sim_game::roomba_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sim_game::roomba_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace sim_game

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'sim_game': ['/home/alexander/test_space/src/sim_game/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::sim_game::roomba_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sim_game::roomba_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sim_game::roomba_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sim_game::roomba_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sim_game::roomba_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sim_game::roomba_msg_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sim_game::roomba_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "63fa31bbe183fb576960c616db4b2bac";
  }

  static const char* value(const ::sim_game::roomba_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x63fa31bbe183fb57ULL;
  static const uint64_t static_value2 = 0x6960c616db4b2bacULL;
};

template<class ContainerAllocator>
struct DataType< ::sim_game::roomba_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sim_game/roomba_msg";
  }

  static const char* value(const ::sim_game::roomba_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sim_game::roomba_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
\n\
int64 id 			# Roomba id\n\
float64 x			# Roomba x pose\n\
float64 y 			# Roomba y pose\n\
bool removed		# Roomba removed\n\
 \n\
bool detected		# Roomba detected by drone\n\
float64 static_x	# Last known x pose \n\
float64 static_y 	# Last known y pose\n\
float64 r 			# Roomba probability radius\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::sim_game::roomba_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sim_game::roomba_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.id);
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.removed);
      stream.next(m.detected);
      stream.next(m.static_x);
      stream.next(m.static_y);
      stream.next(m.r);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct roomba_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sim_game::roomba_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sim_game::roomba_msg_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "id: ";
    Printer<int64_t>::stream(s, indent + "  ", v.id);
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "removed: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.removed);
    s << indent << "detected: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.detected);
    s << indent << "static_x: ";
    Printer<double>::stream(s, indent + "  ", v.static_x);
    s << indent << "static_y: ";
    Printer<double>::stream(s, indent + "  ", v.static_y);
    s << indent << "r: ";
    Printer<double>::stream(s, indent + "  ", v.r);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SIM_GAME_MESSAGE_ROOMBA_MSG_H
