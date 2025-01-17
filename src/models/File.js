const Database = require('../database/db');
    const fs = require('fs');
    const path = require('path');
    const { v4: uuidv4 } = require('uuid');

    const UPLOAD_DIR = path.join(__dirname, '../../uploads');

    class File {
      constructor() {
        this.db = new Database();
        this.initializeTable();
        this.ensureUploadDirectory();
      }

      async initializeTable() {
        await this.db.run(`
          CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            original_name TEXT NOT NULL,
            file_path TEXT NOT NULL,
            file_size INTEGER NOT NULL,
            mime_type TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
          )
        `);
      }

      ensureUploadDirectory() {
        if (!fs.existsSync(UPLOAD_DIR)) {
          fs.mkdirSync(UPLOAD_DIR, { recursive: true });
        }
      }

      async create(fileData) {
        const { filename, originalName, filePath, fileSize, mimeType } = fileData;
        return this.db.run(
          `INSERT INTO files 
           (filename, original_name, file_path, file_size, mime_type)
           VALUES (?, ?, ?, ?, ?)`,
          [filename, originalName, filePath, fileSize, mimeType]
        );
      }

      async listFiles() {
        return this.db.all(
          `SELECT id, filename, original_name, file_size, mime_type, created_at
           FROM files`
        );
      }

      async deleteFile(fileId) {
        const file = await this.db.get(
          `SELECT file_path FROM files WHERE id = ?`,
          [fileId]
        );

        if (file) {
          fs.unlinkSync(file.file_path);
          await this.db.run(
            `DELETE FROM files WHERE id = ?`,
            [fileId]
          );
        }
      }
    }

    module.exports = File;
