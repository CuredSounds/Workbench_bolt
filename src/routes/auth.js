const express = require('express');
    const router = express.Router();
    const { v4: uuidv4 } = require('uuid');
    const User = require('../models/User');

    router.post('/generate-key', async (req, res) => {
      try {
        const apiKey = uuidv4();
        await new User().create(apiKey);
        res.status(201).json({ apiKey });
      } catch (error) {
        res.status(500).json({ error: 'Failed to generate API key' });
      }
    });

    module.exports = router;
