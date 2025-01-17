const sqlite3 = require('sqlite3').verbose();

    class Database {
      constructor() {
        this.db = new sqlite3.Database('./workbench.db', (err) => {
          if (err) {
            console.error('Database connection error:', err.message);
          } else {
            console.log('Connected to the workbench database');
            this.initializeDatabase();
          }
        });
      }

      initializeDatabase() {
        this.db.run(`
          CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            title TEXT,
            content TEXT,
            timestamp DATETIME
          )
        `);
      }

      async saveScrapedData(data) {
        return new Promise((resolve, reject) => {
          this.db.run(
            `INSERT INTO scraped_data (url, title, content, timestamp)
             VALUES (?, ?, ?, ?)`,
            [data.url, data.title, data.content, data.timestamp],
            function(err) {
              if (err) return reject(err);
              resolve(this.lastID);
            }
          );
        });
      }
    }

    module.exports = Database;
