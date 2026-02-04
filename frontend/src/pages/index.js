import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import { authAPI } from '../services/api';
import styles from '../styles/Login.module.css';

export default function Login() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    email: '',
    matKhau: '',
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Check if already logged in
    const token = localStorage.getItem('token');
    if (token) {
      router.push('/dashboard');
    }
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await authAPI.login(formData);
      
      if (response.data.success) {
        localStorage.setItem('token', response.data.data.token);
        localStorage.setItem('user', JSON.stringify(response.data.data));
        router.push('/dashboard');
      }
    } catch (err) {
      setError(err.response?.data?.message || 'Đăng nhập thất bại');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Head>
        <title>Đăng nhập - Hệ thống KPI ICTU</title>
      </Head>
      
      <div className={styles.container}>
        <div className={styles.loginBox}>
          <div className={styles.header}>
            <h1>Hệ thống đánh giá KPI</h1>
            <h2>Trường Đại học Công nghệ Thông tin và Truyền thông</h2>
          </div>

          <form onSubmit={handleSubmit} className={styles.form}>
            <div className={styles.formGroup}>
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                placeholder="Nhập email của bạn"
              />
            </div>

            <div className={styles.formGroup}>
              <label htmlFor="matKhau">Mật khẩu</label>
              <input
                type="password"
                id="matKhau"
                name="matKhau"
                value={formData.matKhau}
                onChange={handleChange}
                required
                placeholder="Nhập mật khẩu"
              />
            </div>

            {error && <div className={styles.error}>{error}</div>}

            <button type="submit" className={styles.submitBtn} disabled={loading}>
              {loading ? 'Đang đăng nhập...' : 'Đăng nhập'}
            </button>
          </form>
        </div>
      </div>
    </>
  );
}
