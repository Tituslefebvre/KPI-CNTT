# Installation Checklist - KPI ICTU System

Use this checklist to verify your installation is complete and working properly.

## Pre-Installation

- [ ] Node.js 16+ installed (`node --version`)
- [ ] MongoDB installed and running (`mongod --version`)
- [ ] npm or yarn installed (`npm --version`)
- [ ] Git installed (`git --version`)

## Backend Installation

- [ ] Navigate to backend directory (`cd backend`)
- [ ] Dependencies installed (`npm install`)
- [ ] Environment file created (`.env` from `.env.example`)
- [ ] MongoDB URI configured in `.env`
- [ ] JWT secret configured in `.env`

## Database Setup

- [ ] MongoDB service is running
- [ ] Seed script executed (`node database/seed.js`)
- [ ] Verified 5 users created
- [ ] Verified 5 KPIs created
- [ ] Verified 3 evaluations created

## Backend Verification

- [ ] Backend starts without errors (`npm run dev`)
- [ ] Server listening on port 5000
- [ ] MongoDB connection successful
- [ ] Health check endpoint works (`curl http://localhost:5000/api`)
- [ ] API returns success message

## Frontend Installation

- [ ] Navigate to frontend directory (`cd frontend`)
- [ ] Dependencies installed (`npm install`)
- [ ] Frontend starts without errors (`npm run dev`)
- [ ] Application accessible at http://localhost:3000
- [ ] No console errors in browser

## Functionality Testing

### Login Tests
- [ ] Can access login page (http://localhost:3000)
- [ ] Login form displays correctly
- [ ] Can login with admin account (admin@ictu.edu.vn / admin123)
- [ ] Can login with teacher account (giangvien1@ictu.edu.vn / gv123456)
- [ ] Invalid credentials show error message
- [ ] Successful login redirects to dashboard

### Dashboard Tests
- [ ] Dashboard loads after login
- [ ] User name displays in header
- [ ] Statistics cards show correct numbers
- [ ] Navigation menu is visible
- [ ] Logout button works

### KPI List Tests
- [ ] Can view KPI list
- [ ] All 5 seed KPIs display
- [ ] Table shows correct columns
- [ ] KPI details are accurate

### Evaluation List Tests
- [ ] Can view evaluation list
- [ ] Evaluations display correctly
- [ ] Status shows properly
- [ ] Correct evaluations for logged-in user

## Docker Testing (Optional)

- [ ] Docker installed (`docker --version`)
- [ ] Docker Compose installed (`docker-compose --version`)
- [ ] Can build images (`docker-compose build`)
- [ ] Can start containers (`docker-compose up -d`)
- [ ] All containers running (`docker ps`)
- [ ] Frontend accessible at http://localhost:3000
- [ ] Backend accessible at http://localhost:5000

## Documentation Check

- [ ] README.md is clear and complete
- [ ] QUICKSTART.md guides 5-minute setup
- [ ] API.md documents all endpoints
- [ ] USER_GUIDE.md explains all features
- [ ] DEPLOYMENT.md covers production setup

## Security Check

- [ ] Passwords are hashed (not plain text in DB)
- [ ] JWT tokens required for protected routes
- [ ] CORS configured properly
- [ ] Environment variables used for secrets
- [ ] .gitignore excludes .env files

## Final Checks

- [ ] No errors in backend console
- [ ] No errors in frontend console
- [ ] No errors in browser console
- [ ] All test accounts work
- [ ] System is responsive
- [ ] UI looks professional

## Troubleshooting

If any checks fail, refer to:
- docs/DEPLOYMENT.md for installation issues
- docs/QUICKSTART.md for setup issues
- README.md for general information
- GitHub Issues for known problems

## Success!

If all checks pass:
✅ Your KPI ICTU system is fully installed and operational!

You can now:
1. Create new users
2. Define KPIs for the academic year
3. Begin the evaluation process
4. Generate reports

---

**Need Help?**
- Email: support@ictu.edu.vn
- GitHub: https://github.com/Tituslefebvre/KPI-CNTT/issues
