const KPI = require('../models/KPI');

// @desc    Get all KPIs
// @route   GET /api/kpis
// @access  Private
const getKPIs = async (req, res) => {
  try {
    const { namHoc, loaiKPI, trangThai } = req.query;
    const filter = {};

    if (namHoc) filter.namHoc = namHoc;
    if (loaiKPI) filter.loaiKPI = loaiKPI;
    if (trangThai) filter.trangThai = trangThai;

    const kpis = await KPI.find(filter).populate('nguoiTao', 'hoTen email');

    res.json({
      success: true,
      count: kpis.length,
      data: kpis,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Get single KPI
// @route   GET /api/kpis/:id
// @access  Private
const getKPI = async (req, res) => {
  try {
    const kpi = await KPI.findById(req.params.id).populate('nguoiTao', 'hoTen email');

    if (!kpi) {
      return res.status(404).json({
        success: false,
        message: 'Không tìm thấy KPI',
      });
    }

    res.json({
      success: true,
      data: kpi,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Create KPI
// @route   POST /api/kpis
// @access  Private (Admin, Trưởng khoa)
const createKPI = async (req, res) => {
  try {
    const kpi = await KPI.create({
      ...req.body,
      nguoiTao: req.user.id,
    });

    res.status(201).json({
      success: true,
      data: kpi,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Update KPI
// @route   PUT /api/kpis/:id
// @access  Private (Admin, Trưởng khoa)
const updateKPI = async (req, res) => {
  try {
    let kpi = await KPI.findById(req.params.id);

    if (!kpi) {
      return res.status(404).json({
        success: false,
        message: 'Không tìm thấy KPI',
      });
    }

    kpi = await KPI.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
      runValidators: true,
    });

    res.json({
      success: true,
      data: kpi,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// @desc    Delete KPI
// @route   DELETE /api/kpis/:id
// @access  Private (Admin)
const deleteKPI = async (req, res) => {
  try {
    const kpi = await KPI.findById(req.params.id);

    if (!kpi) {
      return res.status(404).json({
        success: false,
        message: 'Không tìm thấy KPI',
      });
    }

    await kpi.deleteOne();

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
  getKPIs,
  getKPI,
  createKPI,
  updateKPI,
  deleteKPI,
};
