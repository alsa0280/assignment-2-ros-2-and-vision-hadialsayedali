#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to aisd_msgs__msg__Hand

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Hand {

    // This member is not documented.
    #[allow(missing_docs)]
    pub xpinky: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub xindex: f64,

}



impl Default for Hand {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Hand::default())
  }
}

impl rosidl_runtime_rs::Message for Hand {
  type RmwMsg = super::msg::rmw::Hand;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        xpinky: msg.xpinky,
        xindex: msg.xindex,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      xpinky: msg.xpinky,
      xindex: msg.xindex,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      xpinky: msg.xpinky,
      xindex: msg.xindex,
    }
  }
}


