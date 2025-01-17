const Database = require('../database/db');

    class User {
      constructor() {
        this.db = new Database();
        this.initializeTable();
      }

      async initializeTable() {
        await this.db.run(`
          CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_key TEXT UNIQUE NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
          )
        `);
      }

      async create(apiKey) {
        return this.db.run(
          `INSERT INTO users (api_key) VALUES (?)`,
          [apiKey]
        );
      }

      async findByApiKey(apiKey) {
        return this.db.get(
          `SELECT * FROM users WHERE api_key = ?`,
          [apiKey]
        );
      }
    }

    module.exports = User;
