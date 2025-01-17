const express = require('express');
    const WebScraper = require('./web-scraper/scraper');
    const Database = require('./database/db');

    const app = express();
    const port = 3001;
    const scraper = new WebScraper();
    const db = new Database();

    app.use(express.json());

    app.post('/scrape', async (req, res) => {
      const { url } = req.body;
      if (!url) {
        return res.status(400).json({ error: 'URL is required' });
      }

      try {
        const scrapedData = await scraper.scrape(url);
        if (scrapedData) {
          const recordId = await db.saveScrapedData(scrapedData);
          res.json({ ...scrapedData, id: recordId });
        } else {
          res.status(500).json({ error: 'Failed to scrape the URL' });
        }
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    });

    app.listen(port, () => {
      console.log(`Workbench API running on port ${port}`);
    });
