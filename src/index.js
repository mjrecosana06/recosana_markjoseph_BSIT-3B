require('dotenv').config();
const express = require('express');
const authRoutes = require('./routes/auth');

const app = express();
app.use(express.json());

app.use('/api/auth', authRoutes);

// sample protected route
app.get('/api/protected', require('./middleware/auth'), (req, res) => {
  res.json({ message: `Hello ${req.user.email}, secure world!` });
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
