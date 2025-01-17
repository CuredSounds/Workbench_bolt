const Database = require('../database/db');
    const natural = require('natural');
    const db = new Database();

    class SearchEngine {
      constructor() {
        this.tokenizer = new natural.WordTokenizer();
        this.stemmer = natural.PorterStemmer;
      }

      async search(query, options = {}) {
        const { limit = 10, offset = 0 } = options;
        const tokens = this.tokenizer.tokenize(query);
        const stems = tokens.map(token => this.stemmer.stem(token));

        const searchQuery = `
          SELECT * FROM scraped_data
          WHERE content LIKE ?
          ORDER BY timestamp DESC
          LIMIT ? OFFSET ?
        `;

        return new Promise((resolve, reject) => {
          db.db.all(searchQuery, [`%${stems.join('%')}%`, limit, offset], (err, rows) => {
            if (err) return reject(err);
            resolve(rows);
          });
        });
      }
    }

    module.exports = SearchEngine;
