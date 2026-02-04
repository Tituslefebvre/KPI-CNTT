const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema({
  maNhanVien: {
    type: String,
    required: [true, 'Vui lòng nhập mã nhân viên'],
    unique: true,
  },
  hoTen: {
    type: String,
    required: [true, 'Vui lòng nhập họ tên'],
  },
  email: {
    type: String,
    required: [true, 'Vui lòng nhập email'],
    unique: true,
    lowercase: true,
  },
  matKhau: {
    type: String,
    required: [true, 'Vui lòng nhập mật khẩu'],
    minlength: 6,
    select: false,
  },
  chucVu: {
    type: String,
    enum: ['Giảng viên', 'Trưởng bộ môn', 'Trưởng khoa', 'Quản trị viên'],
    default: 'Giảng viên',
  },
  khoa: {
    type: String,
    required: [true, 'Vui lòng chọn khoa'],
  },
  boMon: {
    type: String,
  },
  trangThai: {
    type: String,
    enum: ['Đang hoạt động', 'Nghỉ phép', 'Đã nghỉ việc'],
    default: 'Đang hoạt động',
  },
  ngayTao: {
    type: Date,
    default: Date.now,
  },
}, {
  timestamps: true,
});

// Hash password before saving
userSchema.pre('save', async function(next) {
  if (!this.isModified('matKhau')) {
    next();
  }
  const salt = await bcrypt.genSalt(10);
  this.matKhau = await bcrypt.hash(this.matKhau, salt);
});

// Match user password
userSchema.methods.matchPassword = async function(enteredPassword) {
  return await bcrypt.compare(enteredPassword, this.matKhau);
};

module.exports = mongoose.model('User', userSchema);
