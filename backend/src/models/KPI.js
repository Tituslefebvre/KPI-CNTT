const mongoose = require('mongoose');

const kpiSchema = new mongoose.Schema({
  maKPI: {
    type: String,
    required: [true, 'Vui lòng nhập mã KPI'],
    unique: true,
  },
  tenKPI: {
    type: String,
    required: [true, 'Vui lòng nhập tên KPI'],
  },
  moTa: {
    type: String,
    required: [true, 'Vui lòng nhập mô tả'],
  },
  loaiKPI: {
    type: String,
    enum: ['Giảng dạy', 'Nghiên cứu khoa học', 'Phục vụ cộng đồng', 'Quản lý'],
    required: true,
  },
  donViDo: {
    type: String,
    required: [true, 'Vui lòng nhập đơn vị đo'],
  },
  chiTieu: {
    type: Number,
    required: [true, 'Vui lòng nhập chỉ tiêu'],
  },
  trongSo: {
    type: Number,
    required: [true, 'Vui lòng nhập trọng số'],
    min: 0,
    max: 100,
  },
  namHoc: {
    type: String,
    required: [true, 'Vui lòng nhập năm học'],
  },
  trangThai: {
    type: String,
    enum: ['Đang áp dụng', 'Đã hết hạn'],
    default: 'Đang áp dụng',
  },
  nguoiTao: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
  },
  ngayTao: {
    type: Date,
    default: Date.now,
  },
}, {
  timestamps: true,
});

module.exports = mongoose.model('KPI', kpiSchema);
