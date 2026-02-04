const mongoose = require('mongoose');

const danhGiaSchema = new mongoose.Schema({
  maDanhGia: {
    type: String,
    required: [true, 'Vui lòng nhập mã đánh giá'],
    unique: true,
  },
  nhanVien: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
  },
  kpi: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'KPI',
    required: true,
  },
  namHoc: {
    type: String,
    required: [true, 'Vui lòng nhập năm học'],
  },
  kyDanhGia: {
    type: String,
    enum: ['Học kỳ 1', 'Học kỳ 2', 'Cả năm'],
    required: true,
  },
  ketQuaThucHien: {
    type: Number,
    required: [true, 'Vui lòng nhập kết quả thực hiện'],
  },
  diemTuDanhGia: {
    type: Number,
    min: 0,
    max: 100,
  },
  diemTruongBoMon: {
    type: Number,
    min: 0,
    max: 100,
  },
  diemTruongKhoa: {
    type: Number,
    min: 0,
    max: 100,
  },
  diemCuoiCung: {
    type: Number,
    min: 0,
    max: 100,
  },
  ghiChu: {
    type: String,
  },
  trangThai: {
    type: String,
    enum: ['Chưa đánh giá', 'Tự đánh giá', 'Trưởng bộ môn đánh giá', 'Trưởng khoa đánh giá', 'Hoàn thành'],
    default: 'Chưa đánh giá',
  },
  nguoiDanhGia: [{
    nguoiDung: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User',
    },
    capDo: String,
    diem: Number,
    nhanXet: String,
    ngayDanhGia: Date,
  }],
  ngayTao: {
    type: Date,
    default: Date.now,
  },
}, {
  timestamps: true,
});

module.exports = mongoose.model('DanhGia', danhGiaSchema);
