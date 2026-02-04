const jwt = require('jsonwebtoken');
const User = require('../models/User');

const protect = async (req, res, next) => {
  let token;

  if (req.headers.authorization && req.headers.authorization.startsWith('Bearer')) {
    try {
      // Get token from header
      token = req.headers.authorization.split(' ')[1];

      // Verify token
      const decoded = jwt.verify(token, process.env.JWT_SECRET || 'ictu-kpi-secret-key-2024');

      // Get user from token
      req.user = await User.findById(decoded.id).select('-matKhau');

      next();
    } catch (error) {
      console.error(error);
      res.status(401).json({ success: false, message: 'Không có quyền truy cập, token không hợp lệ' });
    }
  }

  if (!token) {
    res.status(401).json({ success: false, message: 'Không có quyền truy cập, không có token' });
  }
};

const authorize = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.chucVu)) {
      return res.status(403).json({
        success: false,
        message: `Chức vụ ${req.user.chucVu} không có quyền truy cập tài nguyên này`,
      });
    }
    next();
  };
};

module.exports = { protect, authorize };
