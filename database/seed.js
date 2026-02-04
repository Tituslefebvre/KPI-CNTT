const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const User = require('../src/models/User');
const KPI = require('../src/models/KPI');
const DanhGia = require('../src/models/DanhGia');

const connectDB = async () => {
  try {
    await mongoose.connect('mongodb://localhost:27017/kpi-ictu', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB Connected');
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
};

const seedData = async () => {
  try {
    // Clear existing data
    await User.deleteMany({});
    await KPI.deleteMany({});
    await DanhGia.deleteMany({});

    console.log('Cleared existing data');

    // Create users
    const users = await User.create([
      {
        maNhanVien: 'ADMIN001',
        hoTen: 'Nguyễn Văn Admin',
        email: 'admin@ictu.edu.vn',
        matKhau: 'admin123',
        chucVu: 'Quản trị viên',
        khoa: 'Khoa Công nghệ Thông tin',
      },
      {
        maNhanVien: 'TK001',
        hoTen: 'Trần Thị Hoa',
        email: 'truongkhoa@ictu.edu.vn',
        matKhau: 'tk123456',
        chucVu: 'Trưởng khoa',
        khoa: 'Khoa Công nghệ Thông tin',
      },
      {
        maNhanVien: 'TBM001',
        hoTen: 'Lê Văn Bình',
        email: 'truongbomon@ictu.edu.vn',
        matKhau: 'tbm123456',
        chucVu: 'Trưởng bộ môn',
        khoa: 'Khoa Công nghệ Thông tin',
        boMon: 'Bộ môn Công nghệ Phần mềm',
      },
      {
        maNhanVien: 'GV001',
        hoTen: 'Phạm Thị Mai',
        email: 'giangvien1@ictu.edu.vn',
        matKhau: 'gv123456',
        chucVu: 'Giảng viên',
        khoa: 'Khoa Công nghệ Thông tin',
        boMon: 'Bộ môn Công nghệ Phần mềm',
      },
      {
        maNhanVien: 'GV002',
        hoTen: 'Hoàng Văn Nam',
        email: 'giangvien2@ictu.edu.vn',
        matKhau: 'gv123456',
        chucVu: 'Giảng viên',
        khoa: 'Khoa Công nghệ Thông tin',
        boMon: 'Bộ môn Hệ thống Thông tin',
      },
    ]);

    console.log('Created users');

    // Create KPIs
    const kpis = await KPI.create([
      {
        maKPI: 'KPI-GD-001',
        tenKPI: 'Số giờ giảng dạy',
        moTa: 'Tổng số giờ giảng dạy trong năm học',
        loaiKPI: 'Giảng dạy',
        donViDo: 'giờ',
        chiTieu: 270,
        trongSo: 30,
        namHoc: '2024-2025',
        nguoiTao: users[1]._id, // Trưởng khoa
      },
      {
        maKPI: 'KPI-GD-002',
        tenKPI: 'Điểm đánh giá giảng dạy của sinh viên',
        moTa: 'Điểm đánh giá chất lượng giảng dạy từ sinh viên',
        loaiKPI: 'Giảng dạy',
        donViDo: 'điểm',
        chiTieu: 4.0,
        trongSo: 20,
        namHoc: '2024-2025',
        nguoiTao: users[1]._id,
      },
      {
        maKPI: 'KPI-NCKH-001',
        tenKPI: 'Số bài báo khoa học',
        moTa: 'Số bài báo khoa học được công bố trên tạp chí uy tín',
        loaiKPI: 'Nghiên cứu khoa học',
        donViDo: 'bài',
        chiTieu: 2,
        trongSo: 25,
        namHoc: '2024-2025',
        nguoiTao: users[1]._id,
      },
      {
        maKPI: 'KPI-NCKH-002',
        tenKPI: 'Đề tài nghiên cứu',
        moTa: 'Số đề tài nghiên cứu khoa học được phê duyệt và thực hiện',
        loaiKPI: 'Nghiên cứu khoa học',
        donViDo: 'đề tài',
        chiTieu: 1,
        trongSo: 15,
        namHoc: '2024-2025',
        nguoiTao: users[1]._id,
      },
      {
        maKPI: 'KPI-PVCĐ-001',
        tenKPI: 'Tham gia hoạt động cộng đồng',
        moTa: 'Số hoạt động phục vụ cộng đồng, hướng dẫn sinh viên',
        loaiKPI: 'Phục vụ cộng đồng',
        donViDo: 'hoạt động',
        chiTieu: 3,
        trongSo: 10,
        namHoc: '2024-2025',
        nguoiTao: users[1]._id,
      },
    ]);

    console.log('Created KPIs');

    // Create evaluations for giảng viên 1
    const danhGias = await DanhGia.create([
      {
        maDanhGia: 'DG-2024-001',
        nhanVien: users[3]._id, // Giảng viên 1
        kpi: kpis[0]._id, // Số giờ giảng dạy
        namHoc: '2024-2025',
        kyDanhGia: 'Học kỳ 1',
        ketQuaThucHien: 280,
        diemTuDanhGia: 95,
        trangThai: 'Tự đánh giá',
      },
      {
        maDanhGia: 'DG-2024-002',
        nhanVien: users[3]._id,
        kpi: kpis[1]._id, // Điểm đánh giá
        namHoc: '2024-2025',
        kyDanhGia: 'Học kỳ 1',
        ketQuaThucHien: 4.2,
        diemTuDanhGia: 90,
        trangThai: 'Tự đánh giá',
      },
      {
        maDanhGia: 'DG-2024-003',
        nhanVien: users[3]._id,
        kpi: kpis[2]._id, // Bài báo khoa học
        namHoc: '2024-2025',
        kyDanhGia: 'Cả năm',
        ketQuaThucHien: 2,
        diemTuDanhGia: 100,
        trangThai: 'Chưa đánh giá',
      },
    ]);

    console.log('Created evaluations');

    console.log('\n=== Seed Data Summary ===');
    console.log('Users:', users.length);
    console.log('KPIs:', kpis.length);
    console.log('Evaluations:', danhGias.length);
    console.log('\n=== Test Accounts ===');
    console.log('Admin: admin@ictu.edu.vn / admin123');
    console.log('Trưởng khoa: truongkhoa@ictu.edu.vn / tk123456');
    console.log('Trưởng bộ môn: truongbomon@ictu.edu.vn / tbm123456');
    console.log('Giảng viên 1: giangvien1@ictu.edu.vn / gv123456');
    console.log('Giảng viên 2: giangvien2@ictu.edu.vn / gv123456');

  } catch (error) {
    console.error('Seed error:', error);
  } finally {
    mongoose.connection.close();
  }
};

// Run seed
connectDB().then(seedData);
