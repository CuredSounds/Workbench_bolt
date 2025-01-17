const express = require('express');
    const SearchEngine = require('../search/search');
    const router = express.Router();
    const searchEngine = new SearchEngine();

    router.post('/', async (req, res) => {
      try {
        const { query, options } = req.body;
        const results = await searchEngine.search(query, options);
        res.json(results);
      } catch (error) {
        console.error('Search API error:', error);
        res.status(500).json({ error: 'Failed to perform search' });
      }
    });

    module.exports = router;
