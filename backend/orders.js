const orders = require("../data/orders.json");

function getOrderById(orderId) {
  const order = orders.find(
    (item) => item.orderId.toLowerCase() === orderId.toLowerCase()
  );

  if (!order) {
    return {
      success: false,
      message: "Order not found. Please check your order number."
    };
  }

  return {
    success: true,
    order: {
      orderId: order.orderId,
      status: order.status,
      estimatedArrival: order.estimatedArrival,
      trackingNumber: order.trackingNumber
    }
  };
}

module.exports = {
  getOrderById
};