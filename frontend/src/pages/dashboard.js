import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import { kpiAPI, evaluationAPI } from '../services/api';
import styles from '../styles/Dashboard.module.css';

export default function Dashboard() {
  const router = useRouter();
  const [user, setUser] = useState(null);
  const [kpis, setKpis] = useState([]);
  const [evaluations, setEvaluations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('overview');

  useEffect(() => {
    const token = localStorage.getItem('token');
    const userData = localStorage.getItem('user');
    
    if (!token) {
      router.push('/');
      return;
    }

    setUser(JSON.parse(userData));
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [kpisRes, evaluationsRes] = await Promise.all([
        kpiAPI.getAll({ namHoc: '2024-2025' }),
        evaluationAPI.getAll({ namHoc: '2024-2025' }),
      ]);

      setKpis(kpisRes.data.data || []);
      setEvaluations(evaluationsRes.data.data || []);
    } catch (error) {
      console.error('Error loading data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    router.push('/');
  };

  if (loading) {
    return <div className={styles.loading}>Đang tải...</div>;
  }

  return (
    <>
      <Head>
        <title>Dashboard - Hệ thống KPI ICTU</title>
      </Head>

      <div className={styles.container}>
        <header className={styles.header}>
          <div className={styles.logo}>
            <h1>Hệ thống KPI ICTU</h1>
          </div>
          <div className={styles.userInfo}>
            <span>{user?.hoTen} ({user?.chucVu})</span>
            <button onClick={handleLogout} className={styles.logoutBtn}>
              Đăng xuất
            </button>
          </div>
        </header>

        <div className={styles.main}>
          <nav className={styles.sidebar}>
            <ul>
              <li className={activeTab === 'overview' ? styles.active : ''}>
                <a onClick={() => setActiveTab('overview')}>Tổng quan</a>
              </li>
              <li className={activeTab === 'kpis' ? styles.active : ''}>
                <a onClick={() => setActiveTab('kpis')}>Danh sách KPI</a>
              </li>
              <li className={activeTab === 'evaluations' ? styles.active : ''}>
                <a onClick={() => setActiveTab('evaluations')}>Đánh giá của tôi</a>
              </li>
              {(user?.chucVu === 'Quản trị viên' || user?.chucVu === 'Trưởng khoa') && (
                <>
                  <li className={activeTab === 'manage-kpis' ? styles.active : ''}>
                    <a onClick={() => setActiveTab('manage-kpis')}>Quản lý KPI</a>
                  </li>
                  <li className={activeTab === 'reports' ? styles.active : ''}>
                    <a onClick={() => setActiveTab('reports')}>Báo cáo</a>
                  </li>
                </>
              )}
            </ul>
          </nav>

          <main className={styles.content}>
            {activeTab === 'overview' && (
              <div className={styles.overview}>
                <h2>Tổng quan</h2>
                <div className={styles.statsGrid}>
                  <div className={styles.statCard}>
                    <h3>Tổng số KPI</h3>
                    <p className={styles.statValue}>{kpis.length}</p>
                  </div>
                  <div className={styles.statCard}>
                    <h3>Đánh giá của tôi</h3>
                    <p className={styles.statValue}>{evaluations.length}</p>
                  </div>
                  <div className={styles.statCard}>
                    <h3>Đã hoàn thành</h3>
                    <p className={styles.statValue}>
                      {evaluations.filter(e => e.trangThai === 'Hoàn thành').length}
                    </p>
                  </div>
                  <div className={styles.statCard}>
                    <h3>Chờ đánh giá</h3>
                    <p className={styles.statValue}>
                      {evaluations.filter(e => e.trangThai !== 'Hoàn thành').length}
                    </p>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'kpis' && (
              <div className={styles.kpiList}>
                <h2>Danh sách KPI năm học 2024-2025</h2>
                <table className={styles.table}>
                  <thead>
                    <tr>
                      <th>Mã KPI</th>
                      <th>Tên KPI</th>
                      <th>Loại</th>
                      <th>Chỉ tiêu</th>
                      <th>Trọng số (%)</th>
                      <th>Trạng thái</th>
                    </tr>
                  </thead>
                  <tbody>
                    {kpis.map((kpi) => (
                      <tr key={kpi._id}>
                        <td>{kpi.maKPI}</td>
                        <td>{kpi.tenKPI}</td>
                        <td>{kpi.loaiKPI}</td>
                        <td>{kpi.chiTieu} {kpi.donViDo}</td>
                        <td>{kpi.trongSo}%</td>
                        <td>
                          <span className={kpi.trangThai === 'Đang áp dụng' ? styles.statusActive : styles.statusInactive}>
                            {kpi.trangThai}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}

            {activeTab === 'evaluations' && (
              <div className={styles.evaluationList}>
                <h2>Đánh giá KPI của tôi</h2>
                <table className={styles.table}>
                  <thead>
                    <tr>
                      <th>Mã đánh giá</th>
                      <th>KPI</th>
                      <th>Năm học</th>
                      <th>Kỳ đánh giá</th>
                      <th>Điểm</th>
                      <th>Trạng thái</th>
                    </tr>
                  </thead>
                  <tbody>
                    {evaluations.map((eval) => (
                      <tr key={eval._id}>
                        <td>{eval.maDanhGia}</td>
                        <td>{eval.kpi?.tenKPI}</td>
                        <td>{eval.namHoc}</td>
                        <td>{eval.kyDanhGia}</td>
                        <td>{eval.diemCuoiCung || eval.diemTuDanhGia || '-'}</td>
                        <td>
                          <span className={styles.statusBadge}>
                            {eval.trangThai}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </main>
        </div>
      </div>
    </>
  );
}
