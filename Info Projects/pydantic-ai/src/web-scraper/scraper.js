const cheerio = require('cheerio');
    const axios = require('axios');

    class WebScraper {
      async scrape(url) {
        try {
          const { data } = await axios.get(url);
          const $ = cheerio.load(data);
          
          // Extract basic information
          const title = $('title').text();
          const content = $('body').text().replace(/\s+/g, ' ').trim();
          
          return {
            url,
            title,
            content,
            timestamp: new Date().toISOString()
          };
        } catch (error) {
          console.error(`Error scraping ${url}:`, error);
          return null;
        }
      }
    }

    module.exports = WebScraper;
