# Contributing Guide - Hệ thống KPI ICTU

Cảm ơn bạn đã quan tâm đến việc đóng góp cho dự án! Tài liệu này sẽ hướng dẫn bạn cách đóng góp vào dự án một cách hiệu quả.

---

## Mục lục
1. [Code of Conduct](#code-of-conduct)
2. [Bắt đầu](#bắt-đầu)
3. [Quy trình Phát triển](#quy-trình-phát-triển)
4. [Coding Standards](#coding-standards)
5. [Testing](#testing)
6. [Pull Request Process](#pull-request-process)
7. [Báo cáo Bugs](#báo-cáo-bugs)

---

## Code of Conduct

Dự án này tuân thủ các nguyên tắc:
- Tôn trọng lẫn nhau
- Tiếp nhận phản hồi một cách xây dựng
- Tập trung vào lợi ích của cộng đồng
- Thể hiện sự đồng cảm với các thành viên khác

---

## Bắt đầu

### 1. Fork Repository
```bash
# Fork repo về tài khoản của bạn
# Sau đó clone về máy local
git clone https://github.com/YOUR_USERNAME/KPI-CNTT.git
cd KPI-CNTT
```

### 2. Thêm Remote Upstream
```bash
git remote add upstream https://github.com/Tituslefebvre/KPI-CNTT.git
```

### 3. Cài đặt Dependencies
```bash
# Backend
cd backend
npm install

# Frontend
cd ../frontend
npm install
```

### 4. Tạo Branch mới
```bash
git checkout -b feature/ten-tinh-nang-moi
# hoặc
git checkout -b fix/ten-bug-can-sua
```

---

## Quy trình Phát triển

### 1. Cập nhật Code từ Upstream
```bash
git fetch upstream
git rebase upstream/main
```

### 2. Làm việc trên Branch của bạn
```bash
# Thực hiện các thay đổi
# Commit thường xuyên với messages rõ ràng
git add .
git commit -m "feat: thêm tính năng X"
```

### 3. Test Changes
```bash
# Backend tests
cd backend
npm test

# Frontend tests
cd ../frontend
npm test
```

### 4. Push Changes
```bash
git push origin feature/ten-tinh-nang-moi
```

---

## Coding Standards

### JavaScript/Node.js Standards

#### 1. Naming Conventions
```javascript
// Variables và Functions: camelCase
const userName = 'John';
function getUserData() { }

// Classes: PascalCase
class UserController { }

// Constants: UPPER_SNAKE_CASE
const MAX_RETRY_COUNT = 3;

// Private methods: _prefix
function _privateMethod() { }
```

#### 2. Code Style
```javascript
// Sử dụng const/let, không dùng var
const data = [];
let count = 0;

// Arrow functions khi phù hợp
const add = (a, b) => a + b;

// Async/await thay vì callbacks
async function fetchData() {
  try {
    const data = await api.getData();
    return data;
  } catch (error) {
    console.error(error);
  }
}

// Destructuring
const { name, email } = user;
```

#### 3. Error Handling
```javascript
// Luôn handle errors
try {
  await riskyOperation();
} catch (error) {
  console.error('Error:', error.message);
  // Handle error appropriately
}

// API error responses
res.status(400).json({
  success: false,
  message: 'Error message here',
});
```

### React/Frontend Standards

#### 1. Component Structure
```javascript
// Functional components với hooks
import { useState, useEffect } from 'react';

function MyComponent({ prop1, prop2 }) {
  const [state, setState] = useState(initialValue);

  useEffect(() => {
    // Effect logic
  }, [dependencies]);

  return (
    <div className={styles.container}>
      {/* JSX */}
    </div>
  );
}

export default MyComponent;
```

#### 2. Props và State
```javascript
// PropTypes (nếu không dùng TypeScript)
MyComponent.propTypes = {
  prop1: PropTypes.string.isRequired,
  prop2: PropTypes.number,
};

// Default props
MyComponent.defaultProps = {
  prop2: 0,
};
```

### API Standards

#### 1. Endpoint Naming
```
GET    /api/resources          # Get all
GET    /api/resources/:id      # Get one
POST   /api/resources          # Create
PUT    /api/resources/:id      # Update
DELETE /api/resources/:id      # Delete
```

#### 2. Response Format
```javascript
// Success
{
  "success": true,
  "data": { ... },
  "count": 10  // For lists
}

// Error
{
  "success": false,
  "message": "Error description"
}
```

---

## Testing

### Backend Tests

```javascript
// backend/src/__tests__/user.test.js
const request = require('supertest');
const app = require('../server');

describe('User API', () => {
  test('POST /api/auth/login - success', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'test@ictu.edu.vn',
        matKhau: 'password123',
      });

    expect(response.status).toBe(200);
    expect(response.body.success).toBe(true);
  });
});
```

### Frontend Tests

```javascript
// frontend/src/__tests__/Login.test.js
import { render, screen, fireEvent } from '@testing-library/react';
import Login from '../pages/index';

describe('Login Page', () => {
  test('renders login form', () => {
    render(<Login />);
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
  });
});
```

---

## Pull Request Process

### 1. Chuẩn bị PR

- ✅ Code passes all tests
- ✅ Code follows style guide
- ✅ Documentation updated
- ✅ Commit messages are clear
- ✅ No merge conflicts

### 2. PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots here

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings
```

### 3. Review Process

1. Submit PR với description rõ ràng
2. Đợi review từ maintainers
3. Giải quyết các comments
4. Update PR nếu cần
5. Sau khi approved, PR sẽ được merge

---

## Báo cáo Bugs

### Bug Report Template

```markdown
**Mô tả Bug**
Mô tả ngắn gọn về bug

**Các bước Tái hiện**
1. Vào trang '...'
2. Click vào '...'
3. Scroll xuống '...'
4. Thấy lỗi

**Kết quả Mong đợi**
Mô tả điều bạn mong đợi xảy ra

**Screenshots**
Nếu có, thêm screenshots

**Environment:**
 - OS: [e.g. Windows 10]
 - Browser: [e.g. Chrome 120]
 - Node version: [e.g. 18.17.0]

**Additional context**
Thêm bất kỳ thông tin nào khác
```

---

## Đề xuất Tính năng

### Feature Request Template

```markdown
**Tính năng đề xuất**
Mô tả rõ ràng tính năng bạn muốn

**Lý do**
Giải thích tại sao tính năng này cần thiết

**Giải pháp đề xuất**
Mô tả cách bạn muốn thực hiện

**Các phương án khác**
Mô tả các giải pháp thay thế bạn đã xem xét

**Additional context**
Thêm screenshots, mockups, v.v.
```

---

## Commit Message Guidelines

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: Tính năng mới
- `fix`: Sửa bug
- `docs`: Chỉ thay đổi documentation
- `style`: Format, missing semi-colons, etc
- `refactor`: Code refactoring
- `test`: Thêm tests
- `chore`: Maintenance tasks

### Examples
```bash
feat(auth): add password reset functionality

fix(kpi): correct calculation of weighted scores

docs(api): update authentication endpoints

style(frontend): format dashboard components

refactor(backend): simplify evaluation controller

test(user): add unit tests for user model

chore(deps): update dependencies
```

---

## Branch Naming

### Pattern
```
<type>/<short-description>
```

### Examples
```bash
feature/add-email-notifications
fix/evaluation-calculation-bug
docs/update-api-documentation
refactor/simplify-user-controller
test/add-kpi-tests
```

---

## Documentation

### Code Comments

```javascript
/**
 * Calculate weighted KPI score
 * @param {Number} actualValue - The actual value achieved
 * @param {Number} targetValue - The target value
 * @param {Number} weight - The weight percentage (0-100)
 * @returns {Number} The weighted score
 */
function calculateWeightedScore(actualValue, targetValue, weight) {
  const percentage = (actualValue / targetValue) * 100;
  return (percentage * weight) / 100;
}
```

### README Updates

Khi thêm tính năng mới, cập nhật:
- README.md
- API.md (nếu có API mới)
- USER_GUIDE.md (nếu có UX changes)
- FEATURES.md

---

## Questions?

Nếu có câu hỏi:
1. Kiểm tra [Documentation](docs/)
2. Tìm trong [Issues](https://github.com/Tituslefebvre/KPI-CNTT/issues)
3. Tạo issue mới với tag `question`
4. Email: dev@ictu.edu.vn

---

## License

Bằng việc đóng góp vào dự án, bạn đồng ý rằng contributions của bạn sẽ được licensed dưới MIT License.

---

**Cảm ơn bạn đã đóng góp vào dự án! 🎉**
