const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const connectDB = require('./config/database');

// Load env vars
dotenv.config();

// Connect to database
connectDB();

// Route files
const authRoutes = require('./routes/authRoutes');
const kpiRoutes = require('./routes/kpiRoutes');
const danhGiaRoutes = require('./routes/danhGiaRoutes');

const app = express();

// Body parser
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Enable CORS
app.use(cors());

// Mount routes
app.use('/api/auth', authRoutes);
app.use('/api/kpis', kpiRoutes);
app.use('/api/evaluations', danhGiaRoutes);

// Home route
app.get('/', (req, res) => {
  res.json({
    success: true,
    message: 'Hệ thống đánh giá KPI ICTU API',
    version: '1.0.0',
  });
});

const PORT = process.env.PORT || 5000;

const server = app.listen(PORT, () => {
  console.log(`Server đang chạy trên cổng ${PORT}`);
});

// Handle unhandled promise rejections
process.on('unhandledRejection', (err, promise) => {
  console.log(`Error: ${err.message}`);
  server.close(() => process.exit(1));
});

module.exports = app;
