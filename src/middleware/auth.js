const User = require('../models/User');

    const apiKeyAuth = async (req, res, next) => {
      try {
        const apiKey = req.headers['x-api-key'];
        if (!apiKey) {
          return res.status(401).json({ error: 'API key missing' });
        }

        const user = await new User().findByApiKey(apiKey);
        if (!user) {
          return res.status(401).json({ error: 'Invalid API key' });
        }

        req.user = user;
        next();
      } catch (error) {
        res.status(500).json({ error: 'Authentication failed' });
      }
    };

    module.exports = { apiKeyAuth };
