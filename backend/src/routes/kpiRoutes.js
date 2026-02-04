const express = require('express');
const router = express.Router();
const {
  getKPIs,
  getKPI,
  createKPI,
  updateKPI,
  deleteKPI,
} = require('../controllers/kpiController');
const { protect, authorize } = require('../middleware/auth');

router
  .route('/')
  .get(protect, getKPIs)
  .post(protect, authorize('Quản trị viên', 'Trưởng khoa'), createKPI);

router
  .route('/:id')
  .get(protect, getKPI)
  .put(protect, authorize('Quản trị viên', 'Trưởng khoa'), updateKPI)
  .delete(protect, authorize('Quản trị viên'), deleteKPI);

module.exports = router;
