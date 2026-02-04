const jwt = require('jsonwebtoken');
const User = require('../models/User');

// Generate JWT Token
const generateToken = (id) => {
  return jwt.sign({ id }, process.env.JWT_SECRET || 'ictu-kpi-secret-key-2024', {
    expiresIn: '30d',
  });
};

// @desc    Register user
// @route   POST /api/auth/register
// @access  Public
const register = async (req, res) => {
  try {
    const { maNhanVien, hoTen, email, matKhau, chucVu, khoa, boMon } = req.body;

    // Check if user exists
    const userExists = await User.findOne({ $or: [{ email }, { maNhanVien }] });

    if (userExists) {
      return res.status(400).json({
        success: false,
        message: 'Nhân viên đã tồn tại với email hoặc mã nhân viên này',
      });
    }

    // Create user
    const user = await User.create({
      maNhanVien,
      hoTen,
      email,
      matKhau,
      chucVu,
      khoa,
      boMon,
    });

    if (user) {
      res.status(201).json({
        success: true,
        data: {
          _id: user._id,
          maNhanVien: user.maNhanVien,
          hoTen: user.hoTen,
          email: user.email,
          chucVu: user.chucVu,
          khoa: user.khoa,
          boMon: user.boMon,
          token: generateToken(user._id),
        },
      });
    }
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Login user
// @route   POST /api/auth/login
// @access  Public
const login = async (req, res) => {
  try {
    const { email, matKhau } = req.body;

    // Check for user
    const user = await User.findOne({ email }).select('+matKhau');

    if (!user) {
      return res.status(401).json({
        success: false,
        message: 'Thông tin đăng nhập không hợp lệ',
      });
    }

    // Check password
    const isMatch = await user.matchPassword(matKhau);

    if (!isMatch) {
      return res.status(401).json({
        success: false,
        message: 'Thông tin đăng nhập không hợp lệ',
      });
    }

    res.json({
      success: true,
      data: {
        _id: user._id,
        maNhanVien: user.maNhanVien,
        hoTen: user.hoTen,
        email: user.email,
        chucVu: user.chucVu,
        khoa: user.khoa,
        boMon: user.boMon,
        token: generateToken(user._id),
      },
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Get current user
// @route   GET /api/auth/me
// @access  Private
const getMe = async (req, res) => {
  try {
    const user = await User.findById(req.user.id);

    res.json({
      success: true,
      data: user,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

module.exports = {
  register,
  login,
  getMe,
};
