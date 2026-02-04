const express = require('express');
const router = express.Router();
const {
  getDanhGias,
  getDanhGia,
  createDanhGia,
  updateSelfEvaluation,
  updateManagerEvaluation,
  deleteDanhGia,
} = require('../controllers/danhGiaController');
const { protect, authorize } = require('../middleware/auth');

router
  .route('/')
  .get(protect, getDanhGias)
  .post(protect, authorize('Quản trị viên', 'Trưởng khoa'), createDanhGia);

router
  .route('/:id')
  .get(protect, getDanhGia)
  .delete(protect, authorize('Quản trị viên'), deleteDanhGia);

router.put('/:id/self', protect, updateSelfEvaluation);

router.put(
  '/:id/manager',
  protect,
  authorize('Trưởng bộ môn', 'Trưởng khoa'),
  updateManagerEvaluation
);

module.exports = router;
