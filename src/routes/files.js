const express = require('express');
    const router = express.Router();
    const multer = require('multer');
    const File = require('../models/File');
    const path = require('path');
    const { v4: uuidv4 } = require('uuid');

    const storage = multer.diskStorage({
      destination: (req, file, cb) => {
        cb(null, path.join(__dirname, '../../uploads'));
      },
      filename: (req, file, cb) => {
        const ext = path.extname(file.originalname);
        cb(null, `${uuidv4()}${ext}`);
      }
    });

    const upload = multer({ storage });

    router.post('/upload', upload.single('file'), async (req, res) => {
      try {
        const fileData = {
          filename: req.file.filename,
          originalName: req.file.originalname,
          filePath: req.file.path,
          fileSize: req.file.size,
          mimeType: req.file.mimetype
        };

        await new File().create(fileData);
        res.status(201).json({ message: 'File uploaded successfully' });
      } catch (error) {
        res.status(500).json({ error: 'File upload failed' });
      }
    });

    router.get('/list', async (req, res) => {
      try {
        const files = await new File().listFiles();
        res.json(files);
      } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve files' });
      }
    });

    router.delete('/:id', async (req, res) => {
      try {
        await new File().deleteFile(req.params.id);
        res.json({ message: 'File deleted successfully' });
      } catch (error) {
        res.status(500).json({ error: 'Failed to delete file' });
      }
    });

    module.exports = router;
