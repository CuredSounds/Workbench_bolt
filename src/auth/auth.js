const jwt = require('jsonwebtoken');
    const bcrypt = require('bcryptjs');
    const { v4: uuidv4 } = require('uuid');

    const SECRET_KEY = process.env.JWT_SECRET || 'workbench-secret-key';
    const SALT_ROUNDS = 10;

    class AuthService {
      static async hashPassword(password) {
        return bcrypt.hash(password, SALT_ROUNDS);
      }

      static async comparePassword(password, hash) {
        return bcrypt.compare(password, hash);
      }

      static generateToken(user) {
        return jwt.sign({
          userId: user.id,
          role: user.role
        }, SECRET_KEY, { expiresIn: '1h' });
      }

      static verifyToken(token) {
        return jwt.verify(token, SECRET_KEY);
      }

      static generateApiKey() {
        return uuidv4();
      }
    }

    module.exports = AuthService;
