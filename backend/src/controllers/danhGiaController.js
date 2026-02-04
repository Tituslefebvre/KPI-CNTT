const DanhGia = require('../models/DanhGia');

// @desc    Get all evaluations
// @route   GET /api/evaluations
// @access  Private
const getDanhGias = async (req, res) => {
  try {
    const { namHoc, kyDanhGia, nhanVien, trangThai } = req.query;
    const filter = {};

    if (namHoc) filter.namHoc = namHoc;
    if (kyDanhGia) filter.kyDanhGia = kyDanhGia;
    if (nhanVien) filter.nhanVien = nhanVien;
    if (trangThai) filter.trangThai = trangThai;

    // If not admin, only show user's own evaluations
    if (req.user.chucVu !== 'Quản trị viên' && req.user.chucVu !== 'Trưởng khoa') {
      filter.nhanVien = req.user.id;
    }

    const danhGias = await DanhGia.find(filter)
      .populate('nhanVien', 'hoTen maNhanVien email khoa')
      .populate('kpi', 'tenKPI loaiKPI trongSo chiTieu')
      .populate('nguoiDanhGia.nguoiDung', 'hoTen chucVu');

    res.json({
      success: true,
      count: danhGias.length,
      data: danhGias,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Get single evaluation
// @route   GET /api/evaluations/:id
// @access  Private
const getDanhGia = async (req, res) => {
  try {
    const danhGia = await DanhGia.findById(req.params.id)
      .populate('nhanVien', 'hoTen maNhanVien email khoa boMon')
      .populate('kpi', 'tenKPI moTa loaiKPI trongSo chiTieu donViDo')
      .populate('nguoiDanhGia.nguoiDung', 'hoTen chucVu');

    if (!danhGia) {
      return res.status(404).json({
        success: false,
        message: 'Không tìm thấy đánh giá',
      });
    }

    res.json({
      success: true,
      data: danhGia,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Create evaluation
// @route   POST /api/evaluations
// @access  Private
const createDanhGia = async (req, res) => {
  try {
    const danhGia = await DanhGia.create(req.body);

    res.status(201).json({
      success: true,
      data: danhGia,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Update evaluation (Self-evaluation)
// @route   PUT /api/evaluations/:id/self
// @access  Private
const updateSelfEvaluation = async (req, res) => {
  try {
    const danhGia = await DanhGia.findById(req.params.id);

    if (!danhGia) {
      return res.status(404).json({
        success: false,
        message: 'Không tìm thấy đánh giá',
      });
    }

    // Check if user is the employee being evaluated
    if (danhGia.nhanVien.toString() !== req.user.id) {
      return res.status(403).json({
        success: false,
        message: 'Bạn không có quyền tự đánh giá này',
      });
    }

    danhGia.ketQuaThucHien = req.body.ketQuaThucHien;
    danhGia.diemTuDanhGia = req.body.diemTuDanhGia;
    danhGia.ghiChu = req.body.ghiChu;
    danhGia.trangThai = 'Tự đánh giá';
    
    danhGia.nguoiDanhGia.push({
      nguoiDung: req.user.id,
      capDo: 'Tự đánh giá',
      diem: req.body.diemTuDanhGia,
      nhanXet: req.body.ghiChu,
      ngayDanhGia: Date.now(),
    });

    await danhGia.save();

    res.json({
      success: true,
      data: danhGia,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Update evaluation (Manager evaluation)
// @route   PUT /api/evaluations/:id/manager
// @access  Private (Trưởng bộ môn, Trưởng khoa)
const updateManagerEvaluation = async (req, res) => {
  try {
    const danhGia = await DanhGia.findById(req.params.id);

    if (!danhGia) {
      return res.status(404).json({
        success: false,
        message: 'Không tìm thấy đánh giá',
      });
    }

    const { diem, nhanXet } = req.body;
    let capDo = '';
    let trangThaiMoi = '';

    if (req.user.chucVu === 'Trưởng bộ môn') {
      danhGia.diemTruongBoMon = diem;
      capDo = 'Trưởng bộ môn';
      trangThaiMoi = 'Trưởng bộ môn đánh giá';
    } else if (req.user.chucVu === 'Trưởng khoa') {
      danhGia.diemTruongKhoa = diem;
      danhGia.diemCuoiCung = diem; // Final score
      capDo = 'Trưởng khoa';
      trangThaiMoi = 'Hoàn thành';
    }

    danhGia.trangThai = trangThaiMoi;
    danhGia.nguoiDanhGia.push({
      nguoiDung: req.user.id,
      capDo,
      diem,
      nhanXet,
      ngayDanhGia: Date.now(),
    });

    await danhGia.save();

    res.json({
      success: true,
      data: danhGia,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Delete evaluation
// @route   DELETE /api/evaluations/:id
// @access  Private (Admin)
const deleteDanhGia = async (req, res) => {
  try {
    const danhGia = await DanhGia.findById(req.params.id);

    if (!danhGia) {
      return res.status(404).json({
        success: false,
        message: 'Không tìm thấy đánh giá',
      });
    }

    await danhGia.deleteOne();

    res.json({
      success: true,
      data: {},
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

module.exports = {
  getDanhGias,
  getDanhGia,
  createDanhGia,
  updateSelfEvaluation,
  updateManagerEvaluation,
  deleteDanhGia,
};
