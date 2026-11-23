#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to aisd_msgs__srv__Speak_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Speak_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub words: std::string::String,

}



impl Default for Speak_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Speak_Request::default())
  }
}

impl rosidl_runtime_rs::Message for Speak_Request {
  type RmwMsg = super::srv::rmw::Speak_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        words: msg.words.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        words: msg.words.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      words: msg.words.to_string(),
    }
  }
}


// Corresponds to aisd_msgs__srv__Speak_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Speak_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub response: std::string::String,

}



impl Default for Speak_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Speak_Response::default())
  }
}

impl rosidl_runtime_rs::Message for Speak_Response {
  type RmwMsg = super::srv::rmw::Speak_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        response: msg.response.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        response: msg.response.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      response: msg.response.to_string(),
    }
  }
}






#[link(name = "aisd_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__aisd_msgs__srv__Speak() -> *const std::ffi::c_void;
}

// Corresponds to aisd_msgs__srv__Speak
#[allow(missing_docs, non_camel_case_types)]
pub struct Speak;

impl rosidl_runtime_rs::Service for Speak {
    type Request = Speak_Request;
    type Response = Speak_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__aisd_msgs__srv__Speak() }
    }
}


