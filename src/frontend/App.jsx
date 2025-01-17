import React, { useState } from 'react';
    import axios from 'axios';

    function App() {
      const [url, setUrl] = useState('');
      const [result, setResult] = useState(null);
      const [loading, setLoading] = useState(false);

      const handleScrape = async () => {
        setLoading(true);
        try {
          const response = await axios.post('http://localhost:3001/scrape', { url });
          setResult(response.data);
        } catch (error) {
          console.error('Error:', error);
          setResult({ error: 'Failed to scrape the URL' });
        }
        setLoading(false);
      };

      return (
        <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
          <h1>Workbench Scraper</h1>
          <div style={{ marginBottom: '20px' }}>
            <input
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="Enter URL to scrape"
              style={{ width: '300px', padding: '8px', marginRight: '10px' }}
            />
            <button 
              onClick={handleScrape}
              disabled={loading || !url}
              style={{ padding: '8px 16px' }}
            >
              {loading ? 'Scraping...' : 'Scrape'}
            </button>
          </div>

          {result && (
            <div style={{ marginTop: '20px' }}>
              {result.error ? (
                <div style={{ color: 'red' }}>{result.error}</div>
              ) : (
                <>
                  <h2>Scraped Data</h2>
                  <div style={{ marginBottom: '10px' }}>
                    <strong>Title:</strong> {result.title}
                  </div>
                  <div style={{ marginBottom: '10px' }}>
                    <strong>URL:</strong> {result.url}
                  </div>
                  <div>
                    <strong>Content Preview:</strong>
                    <div style={{
                      maxHeight: '200px',
                      overflowY: 'auto',
                      border: '1px solid #ccc',
                      padding: '10px',
                      marginTop: '10px'
                    }}>
                      {result.content.substring(0, 1000)}...
                    </div>
                  </div>
                </>
              )}
            </div>
          )}
        </div>
      );
    }

    export default App;
